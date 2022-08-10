from dis import opname, opmap
from types import FrameType
from typing import Optional

from bytecode import Bytecode
import inspect

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops
from .util import ObjectId, get_instrumented_program_frame

from typing import Any, Dict, List, Union, Optional
from typing_extensions import Literal
from bytecode import Bytecode, CellVar, FreeVar, Instr, Label, UNSET
from dis import Instruction


def getlineno(id_to_orig_bytecode, code_id, opindex):
  return str(id_to_orig_bytecode[code_id][opindex].lineno)

class ShapeLoggingReceiver(EventReceiver):
  loop_stack: List[Any]
  function_call_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  frame_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  pre_op_stack: List[Any]
  label_to_instr_id: Dict[int, Dict[Instruction,int]]

  def __init__(self) -> None:
    self.loop_stack = []
    self.function_call_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.pre_op_stack = []
    self.trace_logger = dict()
    self.exec_len_key = "exec_len"
    self.label_to_instr_id = dict()
    super().__init__()

  def get_label_to_instr_id(self, id_to_orig_bytecode, code_id, instr_arg):
    if code_id not in self.label_to_instr_id:
      self.label_to_instr_id[code_id] = dict()
      for id, instr in enumerate(id_to_orig_bytecode[code_id]):
        if isinstance(instr, Label):
          self.label_to_instr_id[code_id][instr] = id + 1
    #print(f'target_id = {code_id}, {instr_arg}')
    target_id = self.label_to_instr_id[code_id][instr_arg]
    return target_id



  def show_op_index(self, code_id: int, op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> str:
    return "op #" + str(op_index) + " (" + str(id_to_orig_bytecode[code_id][op_index]) + ")"

  def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> \
      Optional[str]:
    if isinstance(maybe_id, ObjectId):
      obj = self.heap_object_tracking.get_by_id(maybe_id.id)
      if hasattr(obj, "shape"):
        shape = obj.shape
        return " #" + str(maybe_id.id) + ":" + str(shape)
      else:
        return None
    else:
      return None

  def stringify_frame_id(self, frame_id: Union[FrameType, int]) -> str:
    return "frame #" + str(frame_id)

  def print_stack_indent(self, key) -> None:
    self.trace_logger[key].append({"indentation": (len(self.loop_stack) + len(self.function_call_stack)),
                                   "type": "indent",
                                   "exec_idx": self.trace_logger["exec_len"]
                                   })

  def handle_jump_target(self, target_op_index: int) -> None:
    if target_op_index in self.loop_stack:
      while self.loop_stack[-1] != target_op_index:
        del self.loop_stack[-1]
      del self.loop_stack[-1]
    else:
      pass

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

  def setup_trace_logger(self, code_id, opindex, id_to_orig_bytecode):
    key = (code_id, opindex, getlineno(id_to_orig_bytecode, code_id, opindex))
    if key not in self.trace_logger:
      self.trace_logger[key] = []
    if self.exec_len_key not in self.trace_logger:
      self.trace_logger[self.exec_len_key] = 0
    self.trace_logger[self.exec_len_key] += 1
    return key

  def on_event(self, stack: List[Any], opindex: int,
      code_id: int, is_post: bool,
      id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if self.already_in_receiver:
      return
    self.already_in_receiver = True

    cur_frame = get_instrumented_program_frame()
    instr = id_to_orig_bytecode[code_id][opindex]

    if isinstance(instr, Label):
      self.handle_jump_target(opindex + 1)
    else:
      opcode = instr.opcode
      if opname[opcode] == "CALL_FUNCTION":
        if not is_post:
          function_args_id_stack = self.convert_stack_to_heap_id(stack)
          self.function_call_stack.append(function_args_id_stack[0])
        else:
          function_args_id_stack = self.convert_stack_to_heap_id(stack)
          called_function = self.function_call_stack.pop()

      elif opname[opcode] == "RETURN_VALUE":
        pass
      else:
        object_id_stack = self.convert_stack_to_heap_id(stack)

        if opname[opcode] == "POP_TOP" or opname[opcode] == "POP_JUMP_IF_FALSE" or opname[opcode] == "POP_JUMP_IF_TRUE":
          if not is_post:
            pass
        #         self.print_stack_indent()
        #print(f"pop top -> {self.stringify_maybe_object_id(stack[0])}")
        elif opname[opcode] == "ROT_TWO":
          pass
        elif opname[opcode] == "LOAD_CONST":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "load",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger["exec_len"],
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "LOAD_GLOBAL":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "load",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger["exec_len"],
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "load",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger["exec_len"],
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "store",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger[self.exec_len_key],
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "LOAD_DEREF":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            resolved_frame = self.get_var_reference_frame(cur_frame, instr.arg)
            var_name = instr.arg_name
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "load",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger[self.exec_len_key],
                "var_name": var_name,
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "STORE_DEREF":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            resolved_frame = self.get_var_reference_frame(cur_frame, instr.arg)
            var_name = instr.arg_name
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "store",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger[self.exec_len_key],
                "var_name": var_name,
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "BINARY_SUBSCR":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            if not is_post:
              index = object_id_stack[0]
              collection = object_id_stack[1]
              self.pre_op_stack.append((collection, index))
            else:
              collection, index = self.pre_op_stack.pop()

              key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
              #self.print_stack_indent(key)
              self.trace_logger[key].append({
                  "type": "load",
                  "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                  "exec_idx": self.trace_logger[self.exec_len_key],
                  "idx_id": self.stringify_maybe_object_id(index),
                  "base_id": self.stringify_maybe_object_id(collection),
                  "indentation": (len(self.loop_stack) + len(self.function_call_stack))
              }
              )
        elif opname[opcode] == "STORE_SUBSCR":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            #          self.print_stack_indent(key)
            self.trace_logger[key].append({
                "type": "store",
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "exec_idx": self.trace_logger[self.exec_len_key],
                "idx_id": self.stringify_maybe_object_id(object_id_stack[2]),
                "base_id": self.stringify_maybe_object_id(object_id_stack[1]),
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        elif opname[opcode] == "LOAD_CLOSURE":
          rep = self.stringify_maybe_object_id(object_id_stack[0])
          if rep:
            if not object_id_stack[0].id in self.cell_to_frame:
              self.cell_to_frame[object_id_stack[0].id] = self.frame_tracking.get_object_id(cur_frame)
        elif opname[opcode] == "SETUP_LOOP":
          self.loop_stack.append(instr.arg)
        elif opname[opcode] in binary_ops:
          if not is_post:
            self.pre_op_stack.append((object_id_stack[0], object_id_stack[1]))
          else:
            cur_inputs = self.pre_op_stack.pop()

            key = self.setup_trace_logger(code_id, opindex, id_to_orig_bytecode)
            self.trace_logger[key].append({
                "type": "binary",
                "exec_idx": self.trace_logger[self.exec_len_key],
                "oper1_id": self.stringify_maybe_object_id(cur_inputs[0]),
                "op": opname[opcode],
                "oper2_id": self.stringify_maybe_object_id(cur_inputs[1]),
                "obj_id": self.stringify_maybe_object_id(object_id_stack[0]),
                "indentation": (len(self.loop_stack) + len(self.function_call_stack))
            }
            )
        else:
          pass
    self.already_in_receiver = False
