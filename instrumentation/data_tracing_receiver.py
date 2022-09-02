from dis import opname, opmap
from types import FrameType
from bytecode import Bytecode
import inspect

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops
from .util import ObjectId, get_instrumented_program_frame

from typing import Any, Dict, List, Union, Optional
from typing_extensions import Literal

class StackElement(object):
  is_cow_pointer: bool
  cow_latest_value: Optional["StackElement"]
  collection_elems: Optional[Union[List["StackElement"], Dict["StackElement", "StackElement"]]]

  def __init__(
    self,
    concrete: Any, opcode: int,
    deps: List["StackElement"],
    is_cow_pointer: bool = False,
    cow_latest_value: Optional["StackElement"] = None,
    collection_elems: Optional[Union[List["StackElement"], Dict["StackElement", "StackElement"]]] = None
  ):
    self.concrete = concrete
    self.opcode = opcode
    self.deps = deps
    self.is_cow_pointer = is_cow_pointer
    self.cow_latest_value = cow_latest_value
    self.collection_elems = collection_elems
  
  def collection_updated(self, i: Any, value: "StackElement") -> "StackElement":
    if isinstance(self.collection_elems, list):
      # elems_copy = [StackElement(
      #   e.concrete,
      #   opmap["BINARY_SUBSCR"],
      #   [self, i],
      # ) for i, e in enumerate(self.collection_elems)]
      elems_copy_list = [e for i, e in enumerate(self.collection_elems)]
      elems_copy_list[i] = value
      return StackElement(self.concrete, self.opcode, self.deps, self.is_cow_pointer, self.cow_latest_value, elems_copy_list)
    elif isinstance(self.collection_elems, dict):
      elems_copy_dict = {k: StackElement(
        e.concrete,
        opmap["BINARY_SUBSCR"],
        [self, k],
      ) for k, e in self.collection_elems.items()}
      elems_copy_dict[i] = value
      return StackElement(self.concrete, self.opcode, self.deps, self.is_cow_pointer, self.cow_latest_value, elems_copy_dict)
    else:
      raise Exception("Invalid collection type")

class FunctionCallHandled(object):
  return_on_stack: bool
  arg_mapping: Dict[str, StackElement]

  def __init__(self, arg_mapping: Dict[str, StackElement]) -> None:
    self.return_on_stack = False
    self.arg_mapping = arg_mapping

class DataTracingReceiver(EventReceiver):
  function_call_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  frame_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  symbolic_stack: List[StackElement]
  frame_variables: Dict[Union[FrameType, int], Dict[str, StackElement]]
  pre_op_stack: List[Any]
  frame_stack: List[FrameType]

  def __init__(self) -> None:
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.symbolic_stack = []
    self.frame_variables = {}
    self.pre_op_stack = []
    self.frame_stack = []
    super().__init__()

  def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> str:
    if isinstance(maybe_id, ObjectId):
      return "obj #" + str(maybe_id.id) + " (" + str(self.heap_object_tracking.get_by_id(maybe_id.id)) + ")"
    else:
      return str(maybe_id)

  def stringify_frame_id(self, frame_id: Union[FrameType, int]) -> str:
    return "frame #" + str(frame_id)

  def convert_stack_elem_to_heap_id(self, elem: Any) -> Any:
    if self.heap_object_tracking.is_heap_object(elem):
      return self.heap_object_tracking.get_object_id(elem)
    else:
      return elem

  def convert_stack_to_heap_id(self, stack: List[Any]) -> List[Any]:
    object_id_stack = []
    for elem in stack:
      object_id_stack.append(self.convert_stack_elem_to_heap_id(elem))

    return object_id_stack

  def get_var_reference_frame(self, cur_frame: FrameType, arg: Any) -> Union[FrameType, int]:
    if "cell" in arg:
      return self.frame_tracking.get_object_id(cur_frame)
    else:
      fn_object = self.heap_object_tracking.get_by_id(self.function_call_stack[-1].id)
      cell_vars = fn_object.__code__.co_cellvars
      free_vars = fn_object.__code__.co_freevars
      var_index = free_vars.index(arg["free"])
      cell = fn_object.__closure__[var_index]
      return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]

  def load_onto_symbolic_stack(self, object_id_stack: List[Any], resolved_frame: Union[FrameType, int], var_name: str) -> None:
    if var_name in self.frame_variables[resolved_frame]:
      if not self.frame_variables[resolved_frame][var_name].concrete == object_id_stack[0]:
        raise Exception(
          "Variable " + var_name + " has changed from " + \
            self.stringify_maybe_object_id(self.frame_variables[resolved_frame][var_name].concrete) + \
              " to " + self.stringify_maybe_object_id(object_id_stack[0]))
    else:
      raise Exception(f"Cannot create tracing value for previously unseen variable {var_name} in {self.stringify_frame_id(self.frame_tracking.get_object_id(resolved_frame))}")

    self.symbolic_stack.append(self.frame_variables[resolved_frame][var_name])

  def store_from_symbolic_stack(self, resolved_frame: Union[FrameType, int], var_name: str) -> None:
    if resolved_frame not in self.frame_variables:
      self.frame_variables[resolved_frame] = {}
    self.frame_variables[resolved_frame][var_name] = self.symbolic_stack.pop()

  def convert_concrete_to_symbolic(self, concrete_value: Any) -> StackElement:
    if isinstance(concrete_value, list):
      heap_id = self.convert_stack_elem_to_heap_id(concrete_value)
      underlying = StackElement(
        heap_id,
        -1,
        [],
        collection_elems=[self.convert_concrete_to_symbolic(e) for e in concrete_value],
      )

      return StackElement(
        heap_id,
        -1,
        [],
        is_cow_pointer=True,
        cow_latest_value=underlying,
      )
    elif isinstance(concrete_value, dict):
      raise Exception("TODO")
    else:
      return StackElement(
        self.convert_stack_elem_to_heap_id(concrete_value),
        -1,
        []
      )

  def on_event(self, stack: List[Any], opcode: int, arg: Any, opindex: int, code_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if self.already_in_receiver:
      return
    self.already_in_receiver = True
    
    cur_frame = get_instrumented_program_frame()
    if len(self.frame_stack) == 0 or not self.frame_stack[-1] == cur_frame:
      # first time entering this instrumented frame
      self.frame_stack.append(cur_frame)
      self.frame_variables[cur_frame] = {}

      if len(self.frame_stack) == 1 or not self.frame_stack[-2] == cur_frame.f_back:
        # this frame was called from a non-instrumented frame, or is the top-level frame,
        # so we have to populate locals without symbolic traces
        for local, value in cur_frame.f_locals.items():
          self.frame_variables[cur_frame][local] = self.convert_concrete_to_symbolic(value)
      else:
        for name, value in self.pre_op_stack[-1].arg_mapping.items():
          self.frame_variables[cur_frame][name] = value

        # handle default arguments
        for local, value in cur_frame.f_locals.items():
          if local not in self.frame_variables[cur_frame]:
            # TODO: handle mutable default arguments
            self.frame_variables[cur_frame][local] = self.convert_concrete_to_symbolic(value)

    # if opcode == -2: # -2 denotes JUMP_TARGET
    #   pass
    # el
    if opname[opcode] == "CALL_FUNCTION":
      if not is_post:
        symbolic_stack_args = self.symbolic_stack[len(self.symbolic_stack) - len(stack) + 1:]
        self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - len(stack)]

        function_args_id_stack = self.convert_stack_to_heap_id(stack)

        args_mapping = {}
        function_object = self.heap_object_tracking.get_by_id(function_args_id_stack[0].id)

        if hasattr(function_object, "__code__"):
          code_object = function_object.__code__
          positional_arg_names = list(code_object.co_varnames)[:code_object.co_argcount]
          # TODO: handle non-positional calls
          for i, arg in enumerate(positional_arg_names):
            if i < len(symbolic_stack_args):
              args_mapping[arg] = symbolic_stack_args[i]

        self.function_call_stack.append(function_args_id_stack[0])
        self.pre_op_stack.append(FunctionCallHandled(args_mapping))
      else:
        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        called_function = self.function_call_stack.pop()
        return_on_stack = self.pre_op_stack.pop().return_on_stack

        if not return_on_stack:
          self.symbolic_stack.append(StackElement(
            function_args_id_stack[0],
            opcode,
            [] # TODO: add approximate dependencies
          ))
    elif opname[opcode] == "RETURN_VALUE":
      self.frame_stack.pop()
      # if there is no frame on the stack, then we are at the top level, so we don't drop the return value
      if len(self.frame_stack) > 0:
        if not self.frame_stack[-1] == cur_frame.f_back:
          # this frame was called from a non-instrumented frame, so we drop the return value
          self.symbolic_stack.pop()
        else:
          self.pre_op_stack[-1].return_on_stack = True
    else:
      object_id_stack = self.convert_stack_to_heap_id(stack)

      if not is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

      if opname[opcode] == "POP_TOP" or opname[opcode] == "POP_JUMP_IF_FALSE" or opname[opcode] == "POP_JUMP_IF_TRUE":
        if not is_post:
          self.symbolic_stack = self.symbolic_stack[:len(self.symbolic_stack) - 1]
      elif opname[opcode] == "ROT_TWO":
        tos = self.symbolic_stack.pop()
        tos1 = self.symbolic_stack.pop()
        self.symbolic_stack.append(tos)
        self.symbolic_stack.append(tos1)
      elif opname[opcode] == "LOAD_CONST":
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))
      elif opname[opcode] == "LOAD_GLOBAL":
        # TODO: implement correctly
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        self.load_onto_symbolic_stack(object_id_stack, cur_frame, arg)
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        self.store_from_symbolic_stack(cur_frame, arg)
      elif opname[opcode] == "LOAD_DEREF":
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.load_onto_symbolic_stack(object_id_stack, resolved_frame, var_name)
      elif opname[opcode] == "STORE_DEREF":
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]
        self.store_from_symbolic_stack(resolved_frame, var_name)
      elif opname[opcode] == "BINARY_SUBSCR":
        if not is_post:
          index = self.symbolic_stack.pop()
          collection = self.symbolic_stack.pop()
          self.pre_op_stack.append((collection, index))
        else:
          collection, index = self.pre_op_stack.pop()

          index_reified = index.concrete
          if collection.is_cow_pointer and collection.cow_latest_value and collection.cow_latest_value.collection_elems:
            loaded_symbolic = collection.cow_latest_value.collection_elems[index_reified]
            self.symbolic_stack.append(StackElement(
              loaded_symbolic.concrete,
              opcode,
              [collection.cow_latest_value, index_reified],
            ))
          else:
            raise Exception(f"Cannot store into non-cow collection: {self.stringify_maybe_object_id(collection.concrete)}")
      elif opname[opcode] == "STORE_SUBSCR":
        index = self.symbolic_stack.pop()
        collection = self.symbolic_stack.pop()
        value = self.symbolic_stack.pop()

        index_reified = index.concrete # TODO: handle non-integer indices
        if collection.is_cow_pointer and collection.cow_latest_value:
          orig_collection = collection.cow_latest_value
          new_collection = orig_collection.collection_updated(index_reified, value)
          collection.cow_latest_value = new_collection
        else:
          raise Exception("Cannot store into non-cow collection")
      elif opname[opcode] == "LOAD_CLOSURE":
        if not object_id_stack[0].id in self.cell_to_frame:
          self.cell_to_frame[object_id_stack[0].id] = (self.frame_tracking.get_object_id(cur_frame), self.myabstraction(cur_frame))
        self.symbolic_stack.append(StackElement(object_id_stack[0], opcode, []))
      elif opname[opcode] == "SETUP_LOOP":
        pass
      elif opname[opcode] in binary_ops:
        if not is_post:
          tos = self.symbolic_stack.pop()
          tos1 = self.symbolic_stack.pop()
          self.pre_op_stack.append((tos1, tos))
        else:
          cur_inputs = self.pre_op_stack.pop()

          self.symbolic_stack.append(StackElement(
            object_id_stack[0],
            opcode,
            [cur_inputs[0], cur_inputs[1]]
          ))
      else:
        raise NotImplementedError(opname[opcode])
      
      if is_post:
        self.check_symbolic_stack(object_id_stack, opcode)

    self.already_in_receiver = False

  def check_symbolic_stack(self, object_id_stack: List[Any], opcode: int) -> None:
    for i, e in enumerate(object_id_stack):
      index_from_end = i - len(object_id_stack)
      try:
        if not self.symbolic_stack[index_from_end].concrete == e:
          print(opname[opcode])
          print("symbolic:", [self.stringify_maybe_object_id(e.concrete) for e in self.symbolic_stack])
          print("concrete:", [self.stringify_maybe_object_id(e) for e in object_id_stack])
          raise Exception(
            "Stack element " + str(i) + " is symbolically " + \
              self.stringify_maybe_object_id(self.symbolic_stack[index_from_end].concrete) + \
                " but concretely " + self.stringify_maybe_object_id(e))
      except IndexError:
        print(opname[opcode])
        print("symbolic:", [self.stringify_maybe_object_id(e.concrete) for e in self.symbolic_stack])
        print("concrete:", [self.stringify_maybe_object_id(e) for e in object_id_stack])
        raise Exception("Stack element at index " + str(i) + " is not in symbolic stack")
