from dis import Instruction
from dis import opname
from types import FrameType
from typing import Any
from typing import Dict
from typing import List
from typing import Union

import config
from bytecode import Bytecode
from bytecode import Label

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops
from .instrument import unary_ops
from .util import ObjectId
from .util import get_instrumented_program_frame


def getlineno(id_to_orig_bytecode, method_id, instr_id):
  return str(id_to_orig_bytecode[method_id][instr_id].lineno)

class LoadStoreApplyReceiver(EventReceiver):
  loop_stack: List[Any]
  function_call_stack: List[Any]
  function_name_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  frame_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  pre_op_stack: List[Any]
  label_to_instr_id: Dict[int, Dict[Instruction,int]]

  def __init__(self) -> None:
    self.loop_stack = []
    self.function_call_stack = []
    self.function_name_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.frame_tracking = HeapObjectTracker()
    self.cell_to_frame = {}
    self.pre_op_stack = []
    self.trace_logger = []
    self.exec_len_key = "exec_len"
    self.label_to_instr_id = dict()
    super().__init__()

  def get_repr(self, obj):
    ignore, repr = config.custom_analyzer.abstraction(obj)
    if not ignore:
      return ObjectId(self.heap_object_tracking.get_object_id(obj)), type(obj), repr
    else:
      return None

  def handle_jump_target(self, target_op_index: int) -> None:
    if target_op_index in self.loop_stack:
      while self.loop_stack[-1] != target_op_index:
        del self.loop_stack[-1]
      del self.loop_stack[-1]

  def convert_stack_to_heap_id(self, stack: List[Any]) -> List[Any]:
    object_id_stack = []
    for elem in stack:
      object_id_stack.append(self.get_repr(elem))
    return object_id_stack

  def get_var_reference_frame(self, cur_frame: FrameType, instr: Any) -> Union[FrameType, int]:
    if not hasattr(instr, "__code__"):
      return cur_frame
    else:
      fn_object = self.heap_object_tracking.get_by_id(self.function_call_stack[-1].id)
      cell_vars = fn_object.__code__.co_cellvars
      free_vars = fn_object.__code__.co_freevars
      var_index = free_vars.index(instr.name)
      cell = fn_object.__closure__[var_index]
      return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]

  def append_to_trace_logger(self, loc, before, rest: Dict = None, opcode = -1, type = None):
    if bool(opcode == -1) == bool(type == None):
      raise Exception("Internal error: Either opcode or type argument must be set")
    record = {
        "module_name": loc[0],
        "method_id": loc[1],
        "instruction_id": loc[2],
        "lineno": loc[3],
        "before": before,
        "type": type if type else opname[opcode],
        "execution_index": len(self.trace_logger),
        "indentation": (len(self.loop_stack) + len(self.function_call_stack))
    }
    if rest:
      for k, v in rest.items():
        record[k] = v
    record = config.custom_analyzer.process_event(record)
    if record is not None:
      self.trace_logger.append(record)


  def on_event(self, stack: List[Any], instr_id: int,
      method_id: int, module_name: str, is_post: bool,
      id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    if self.already_in_receiver:
      return
    self.already_in_receiver = True

    cur_frame = get_instrumented_program_frame()
    instr = id_to_orig_bytecode[method_id][instr_id]

    if isinstance(instr, Label):
      self.handle_jump_target(instr_id + 1)
    else:
      opcode = instr.opcode
      object_id_stack = self.convert_stack_to_heap_id(stack)
      loc = (module_name, method_id, instr_id, getlineno(id_to_orig_bytecode ,method_id, instr_id))
      if opname[opcode] == "CALL_FUNCTION":
        if not is_post:
          self.function_call_stack.append(object_id_stack[0])
          called_function = self.function_call_stack[-1]
          self.function_name_stack.append(stack[0].__name__ if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, True, {
              "function": called_function,
              "function_name": function_name,
              "args_list": object_id_stack[1:],
              "indentation": (len(self.loop_stack) + len(self.function_call_stack)) - 1
          }, opcode)
        else:
          object_id_stack = self.convert_stack_to_heap_id(stack)
          called_function = self.function_call_stack.pop()
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "type": "RETURN_FUNCTION",
              "function": called_function,
              "function_name": function_name,
              "result": object_id_stack[0]}, opcode)
      elif opname[opcode] == "CALL_METHOD":
        if not is_post:
          self.function_call_stack.append(object_id_stack[0])
          called_function = self.function_call_stack[-1]
          self.function_name_stack.append(stack[0].__name__ if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, True, {
              "function": called_function,
              "function_name": function_name,
              "args_list": object_id_stack[1:],
              "indentation": (len(self.loop_stack) + len(self.function_call_stack)) - 1
          }, opcode)
        else:
          object_id_stack = self.convert_stack_to_heap_id(stack)
          called_function = self.function_call_stack.pop()
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "type": "RETURN_METHOD",
              "function": called_function,
              "function_name": function_name,
              "result": object_id_stack[0]}, opcode)
      elif opname[opcode] == "CALL_FUNCTION_KW":
        if not is_post:
          keys = stack[-1]
          self.function_call_stack.append(object_id_stack[0])
          called_function = self.function_call_stack[-1]
          self.function_name_stack.append(stack[0].__name__ if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, True, {
              "function": called_function,
              "function_name": function_name,
              "args_list": object_id_stack[1:-1] + [keys,],
              "indentation": (len(self.loop_stack) + len(self.function_call_stack)) - 1
          }, opcode)
        else:
          called_function = self.function_call_stack.pop()
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "type": "RETURN_FUNCTION_KW",
              "function": called_function,
              "function_name": function_name,
              "result": object_id_stack[0]}, opcode)
      elif opname[opcode] == "LOAD_CONST":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, False, {
            "result":  rep
        }, opcode)
      elif opname[opcode] == "LOAD_GLOBAL":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, False, {
            "var_name": instr.arg,
            "result": rep,
        }, opcode)
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        rep = object_id_stack[0]
        resolved_frame = self.get_var_reference_frame(cur_frame, instr)
        self.append_to_trace_logger(loc, False, {
            "frame": self.get_repr(resolved_frame),
            "var_name": instr.arg,
            "result": rep
        }, opcode)
      elif opname[opcode] == "LOAD_ATTR":
        rep = object_id_stack[0]
        if not is_post:
          self.pre_op_stack.append(rep)
        else:
          collection = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "base": collection,
              "attr_name": instr.arg,
              "result": rep,
          }, opcode)
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        rep = object_id_stack[0]
        resolved_frame = self.get_var_reference_frame(cur_frame, instr)
        self.append_to_trace_logger(loc, True, {
            "frame": self.get_repr(resolved_frame),
            "var_name": instr.arg,
            "operand": rep
        }, opcode)
      elif opname[opcode] == "STORE_ATTR":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, True, {
            "operand": object_id_stack[1],
            "attr_name": instr.arg,
            "base": rep
        }, opcode)
      elif opname[opcode] == "LOAD_DEREF":
        rep = object_id_stack[0]
        var_name = instr.arg.name
        self.append_to_trace_logger(loc, False, {
            "var_name": var_name,
            "result": rep,
        }, opcode)
      elif opname[opcode] == "STORE_DEREF":
        rep = object_id_stack[0]
        var_name = instr.arg.name
        self.append_to_trace_logger(loc, True, {
            "var_name": var_name,
            "operand": rep,
        }, opcode)
      elif opname[opcode] == "BINARY_SUBSCR":
        rep = object_id_stack[0]
        if not is_post:
          index = object_id_stack[0]
          collection = object_id_stack[1]
          self.pre_op_stack.append((collection, index))
        else:
          collection, index = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "base": collection,
              "index": index,
              "result": rep,
          }, opcode)
      elif opname[opcode] == "STORE_SUBSCR":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, True, {
            "index": object_id_stack[2],
            "base": object_id_stack[1],
            "operand": rep,
        }, opcode)
      elif opname[opcode] == "LOAD_CLOSURE":
        rep = object_id_stack[0]
        if rep is not None and isinstance(rep[0], ObjectId):
          if not object_id_stack[0][0].id in self.cell_to_frame:
            self.cell_to_frame[object_id_stack[0][0].id] = self.frame_tracking.get_object_id(cur_frame)
      elif opname[opcode] == "SETUP_LOOP":
        self.loop_stack.append(instr.arg)
      elif opname[opcode] in binary_ops:
        if not is_post:
          self.pre_op_stack.append((object_id_stack[0], object_id_stack[1]))
        else:
          cur_inputs = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "operand1": cur_inputs[0],
              "operand2": cur_inputs[1],
              "result": object_id_stack[0],
            }, opcode)
      elif opname[opcode] in unary_ops:
        if not is_post:
          self.pre_op_stack.append(object_id_stack[0])
        else:
          cur_input = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, False, {
              "operand": cur_input,
              "result": object_id_stack[0],
          }, opcode)
    self.already_in_receiver = False
