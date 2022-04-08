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

class StackTrackingReceiver(EventReceiver):
  loop_stack: List[Any]
  function_call_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  frame_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  pre_op_stack: List[Any]

  def __init__(self) -> None:
    self.loop_stack = []
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.pre_op_stack = []
    super().__init__()

  def show_op_index(self, code_id: int, op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> str:
    return "op #" + str(op_index) + " (" + str(id_to_orig_bytecode[code_id][op_index]) + ")"

  def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> str:
    if isinstance(maybe_id, ObjectId):
      return "obj #" + str(maybe_id.id) + " (" + str(self.heap_object_tracking.get_by_id(maybe_id.id)) + ")"
    else:
      return str(maybe_id)

  def stringify_frame_id(self, frame_id: Union[FrameType, int]) -> str:
    return "frame #" + str(frame_id)# + " (" + str(self.frame_tracking.get_by_id(frame_id)) + ")"

  def print_stack_indent(self) -> None:
    print("\t" * (len(self.loop_stack) + len(self.function_call_stack)), end="")

  def handle_jump_target(self, code_id: int, target_op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if target_op_index in self.loop_stack:
      while self.loop_stack[-1] != target_op_index:
        del self.loop_stack[-1]
      del self.loop_stack[-1] # drop the last element for real

      self.print_stack_indent()
      print("end loop")
    else:
      self.print_stack_indent()
      print("arrived at:", self.show_op_index(code_id, target_op_index, id_to_orig_bytecode))

  def convert_stack_elem_to_heap_id(self, elem: Any) -> Any:
    if self.heap_object_tracking.is_heap_object(elem):
      return ObjectId(self.heap_object_tracking.get_object_id(elem))
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

  def on_event(self, stack: List[Any], opcode: Union[Literal["JUMP_TARGET"], int], arg: Any, opindex: int, code_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if self.already_in_receiver:
      return
    self.already_in_receiver = True
    
    cur_frame = get_instrumented_program_frame()

    if opcode == "JUMP_TARGET":
      self.handle_jump_target(code_id, arg["label"], id_to_orig_bytecode)
    elif opname[opcode] == "CALL_FUNCTION":
      if not is_post:
        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        self.print_stack_indent()
        print(
          "begin function call - function:",
          self.stringify_maybe_object_id(function_args_id_stack[0]),
          "on args",
          "(" + ", ".join(map(self.stringify_maybe_object_id, stack[1:])) + ")"
        )

        self.function_call_stack.append(function_args_id_stack[0])
      else:
        function_args_id_stack = self.convert_stack_to_heap_id(stack)
        called_function = self.function_call_stack.pop()

        self.print_stack_indent()
        print(
          "end function call - function:",
          self.stringify_maybe_object_id(called_function),
          "result:",
          self.stringify_maybe_object_id(function_args_id_stack[0])
        )
    elif opname[opcode] == "RETURN_VALUE":
      self.print_stack_indent()
      print(f"return value -> {self.stringify_maybe_object_id(stack[0])}")
    else:
      object_id_stack = self.convert_stack_to_heap_id(stack)

      if opname[opcode] == "POP_TOP" or opname[opcode] == "POP_JUMP_IF_FALSE" or opname[opcode] == "POP_JUMP_IF_TRUE":
        if not is_post:
          self.print_stack_indent()
          print(f"pop top -> {self.stringify_maybe_object_id(stack[0])}")
      elif opname[opcode] == "ROT_TWO":
        pass
      elif opname[opcode] == "LOAD_CONST":
        self.print_stack_indent()
        print(
          "load const ->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_GLOBAL":
        self.print_stack_indent()
        print(
          "load global ->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        self.print_stack_indent()
        print(
          "load", arg,
          "from", self.stringify_frame_id(self.frame_tracking.get_object_id(cur_frame)),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        self.print_stack_indent()
        print(
          "store", arg,
          "in", self.stringify_frame_id(self.frame_tracking.get_object_id(cur_frame)),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_DEREF":
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]

        self.print_stack_indent()
        print(
          "load", var_name,
          "from", self.stringify_frame_id(resolved_frame),
          "->", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "STORE_DEREF":
        resolved_frame = self.get_var_reference_frame(cur_frame, arg)
        var_name = arg["cell"] if "cell" in arg else arg["free"]

        self.print_stack_indent()
        print(
          "store", var_name,
          "in", self.stringify_frame_id(resolved_frame),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "BINARY_SUBSCR":
        if not is_post:
          index = object_id_stack[0]
          collection = object_id_stack[1]
          self.pre_op_stack.append((collection, index))
        else:
          collection, index = self.pre_op_stack.pop()

          self.print_stack_indent()
          print(
            "load from", self.stringify_maybe_object_id(collection),
            "at index", self.stringify_maybe_object_id(index),
            "->", self.stringify_maybe_object_id(object_id_stack[0])
          )
      elif opname[opcode] == "STORE_SUBSCR":
        self.print_stack_indent()
        print(
          "store into", self.stringify_maybe_object_id(object_id_stack[1]),
          "at index", self.stringify_maybe_object_id(object_id_stack[2]),
          "=", self.stringify_maybe_object_id(object_id_stack[0])
        )
      elif opname[opcode] == "LOAD_CLOSURE":
        if not object_id_stack[0].id in self.cell_to_frame:
          self.cell_to_frame[object_id_stack[0].id] = self.frame_tracking.get_object_id(cur_frame)
          self.print_stack_indent()
          print(
            "prepare closure cell for variable " + arg["cell"] +
            " in " + self.stringify_frame_id(self.cell_to_frame[object_id_stack[0].id]) +
            " -> " + self.stringify_maybe_object_id(object_id_stack[0])
          )
      elif opname[opcode] == "SETUP_LOOP":
        self.print_stack_indent()
        print("begin loop", id_to_orig_bytecode[code_id][opindex])
        self.loop_stack.append(arg["label"])
      elif opname[opcode] in binary_ops:
        if not is_post:
          self.pre_op_stack.append((object_id_stack[0], object_id_stack[1]))
        else:
          cur_inputs = self.pre_op_stack.pop()

          self.print_stack_indent()
          print(
            "binary op",
            self.stringify_maybe_object_id(cur_inputs[0]),
            opname[opcode],
            self.stringify_maybe_object_id(cur_inputs[1]),
            "->", self.stringify_maybe_object_id(object_id_stack[0])
          )
      else:
        self.print_stack_indent()
        print("UNKNOWN OPCODE:")
        self.print_stack_indent()
        print("stack:", stack, "| opcode:", opname[opcode], "| arg:", arg, "| orig op:", id_to_orig_bytecode[code_id][opindex])

    self.already_in_receiver = False
