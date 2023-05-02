from dis import opname
from types import FrameType
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from pynsy import handle
from bytecode import Bytecode
from bytecode import CellVar
from bytecode import FreeVar
from bytecode import Label

from .event_receiver import EventReceiver
from .heap_object_tracking import HeapObjectTracker
from .instrument import binary_ops
from .instrument import unary_ops
from .util import ObjectId
from .util import get_instrumented_program_frame


def getlineno(id_to_orig_bytecode, method_id, instr_id):
  return str(id_to_orig_bytecode[method_id][instr_id].lineno)

class OperatorApply(EventReceiver):
  loop_stack: List[Any]
  function_call_stack: List[Any]
  function_name_stack: List[Any]
  heap_object_tracking: HeapObjectTracker
  cell_to_frame: Dict[int, Union[FrameType, int]]
  already_in_receiver: bool = False
  pre_op_stack: List[Any]

  def __init__(self) -> None:
    self.loop_stack = []
    self.function_call_stack = []
    self.function_name_stack = []
    self.heap_object_tracking = HeapObjectTracker()
    self.pre_op_stack = []
    self.trace_logger = []
    self.cell_to_frame = {}
    self.exec_len_key = "exec_len"
    self.novalue = {'id': -1, 'type': None, 'abs': None}
    super().__init__()

  def get_wrapped_repr(self, obj):
    return {'id': 0, 'type': type(obj), 'abs': obj}

  def get_repr(self, obj):
    ignore, repr = handle.custom_analyzer.abstraction(obj)
    if not ignore:
      return {'id': ObjectId(self.heap_object_tracking.get_object_id(obj)), 'type': type(obj), 'abs': repr}
    else:
      return {'id': 0, 'type': type(obj), 'abs': repr}

  def get_special_object_repr(self, obj):
    return {'id': ObjectId(self.heap_object_tracking.get_object_id(obj)), 'type': type(obj), 'abstraction': None}


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
    if not len(self.function_call_stack) == 0:
      fn_object = self.function_call_stack[-1]
    else:
      fn_object = cur_frame
    if not hasattr(fn_object, "__code__"):
      return self.heap_object_tracking.get_object_id(cur_frame)
    else:
      if isinstance(instr.arg, CellVar):
        return self.heap_object_tracking.get_object_id(cur_frame)
      elif isinstance(instr.arg, FreeVar):
        free_vars = fn_object.__code__.co_freevars
        var_index = free_vars.index(instr.arg.name)
        cell = fn_object.__closure__[var_index]
        return self.cell_to_frame[self.heap_object_tracking.get_object_id(cell)]      #   if isinstance(arg, CellVar):
      #   emit_kv("cell", arg.name)
      # elif isinstance(arg, FreeVar):
      #   emit_kv("free", arg.name)
      # cell_vars = fn_object.__code__.co_cellvars
      # free_vars = fn_object.__code__.co_freevars
      # var_index = free_vars.index(instr.name)
      # cell = fn_object.__closure__[var_index]
      # return self.heap_object_tracking.get_object_id(cell)

  def append_to_trace_logger(self, loc, rest: Dict = None, opcode = -1, type = None):
    if bool(opcode == -1) == bool(type == None):
      raise Exception("Internal error: Either opcode or type argument must be set")
    record = {
        "module_name": loc[0],
        "method_id": loc[1],
        "instruction_id": loc[2],
        "lineno": loc[3],
        "type": type if type else opname[opcode],
        "execution_index": len(self.trace_logger),
        "indentation": (len(self.loop_stack) + len(self.function_call_stack))
    }
    if rest:
      for k, v in rest.items():
        record[k] = v
    record = handle.custom_analyzer.process_event(record)
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
          self.function_call_stack.append(stack[0])
          self.function_name_stack.append(stack[0].__name__ if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, {
              "name": function_name,
              "result_and_args": [self.novalue] + object_id_stack[1:],
              "indentation": (len(self.loop_stack) + len(self.function_name_stack)) - 1
          }, opcode)
        else:
          self.function_call_stack.pop()
          object_id_stack = self.convert_stack_to_heap_id(stack)
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, {
              "type": "RETURN_FUNCTION",
              "name": function_name,
              "result_and_args": object_id_stack}, opcode)
      elif opname[opcode] == "CALL_METHOD":
        if not is_post:
          self.function_call_stack.append(stack[0])
          self.function_name_stack.append(stack[0].__name__ if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, {
              "name": function_name,
              "result_and_args": [self.novalue] + object_id_stack[1:],
              "indentation": (len(self.loop_stack) + len(self.function_name_stack)) - 1
          }, opcode)
        else:
          self.function_call_stack.pop()
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, {
              "type": "RETURN_METHOD",
              "name": function_name,
              "result_and_args": object_id_stack}, opcode)
      elif opname[opcode] == "CALL_FUNCTION_KW":
        if not is_post:
          keys = stack[-1]
          self.function_call_stack.append(stack[0])
          self.function_name_stack.append(stack[0].__name__  if hasattr(stack[0], "__name__") else type(stack[0]))
          function_name = self.function_name_stack[-1]
          self.append_to_trace_logger(loc, {
              "function_name": function_name,
              "result_and_args": object_id_stack[1:-1] + [keys,],
              "indentation": (len(self.loop_stack) + len(self.function_call_stack)) - 1
          }, opcode)
        else:
          self.function_call_stack.pop()
          function_name = self.function_name_stack.pop()
          self.append_to_trace_logger(loc, {
              "type": "RETURN_FUNCTION_KW",
              "name": function_name,
              "result_and_args": object_id_stack}, opcode)
      elif opname[opcode] == "LOAD_CONST":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "result_and_args":  [rep]
        }, opcode)
      elif opname[opcode] == "LOAD_GLOBAL":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "name": instr.arg,
            "result_and_args": [rep, self.get_wrapped_repr(instr.arg)],
        }, opcode)
      elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "name": instr.arg,
            "result_and_args": [rep, self.get_special_object_repr(cur_frame), self.get_wrapped_repr(instr.arg)]
        }, opcode)
      elif opname[opcode] == "LOAD_CLOSURE":
        rep = self.get_special_object_repr(stack[0])
        if not rep['id'].id in self.cell_to_frame:
          self.cell_to_frame[rep['id'].id] = self.get_special_object_repr(cur_frame)['id'].id
        self.append_to_trace_logger(loc, {
            "name": instr.arg,
            "result_and_args": [rep, self.get_special_object_repr(cur_frame), self.get_wrapped_repr(instr.arg)]
        }, opcode)
      elif opname[opcode] == "LOAD_DEREF":
        rep = object_id_stack[0]
        var_name = instr.arg.name
        resolved_frame = self.get_var_reference_frame(cur_frame, instr)
        self.append_to_trace_logger(loc, {
            "name": var_name,
            "result_and_args": [rep,  self.get_special_object_repr(resolved_frame), self.get_wrapped_repr(var_name)],
        }, opcode)
      elif opname[opcode] == "LOAD_ATTR":
        rep = object_id_stack[0]
        if not is_post:
          self.pre_op_stack.append(rep)
        else:
          collection = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, {
              "result_and_args": (rep, collection, self.get_wrapped_repr(instr.arg))
          }, opcode)
      elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "result_and_args": [self.novalue, self.get_special_object_repr(cur_frame), self.get_wrapped_repr(instr.arg), rep],
            "name": instr.arg,
        }, opcode)
      elif opname[opcode] == "STORE_ATTR":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "operand": [self.novalue, rep, self.get_wrapped_repr(instr.arg), object_id_stack[1]],
            "name": instr.arg,
        }, opcode)
      elif opname[opcode] == "STORE_DEREF":
        rep = self.get_special_object_repr(stack[0])
        var_name = instr.arg.name
        resolved_frame = self.get_var_reference_frame(cur_frame, instr)
        self.append_to_trace_logger(loc, {
            "name": var_name,
            "result_and_args": [rep, self.get_special_object_repr(resolved_frame), self.get_wrapped_repr(var_name)],
        }, opcode)
      elif opname[opcode] == "BINARY_SUBSCR":
        rep = object_id_stack[0]
        if not is_post:
          index = object_id_stack[0]
          collection = object_id_stack[1]
          self.pre_op_stack.append((collection, index))
        else:
          collection, index = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, {
              "result_and_args": [rep, collection, self.get_wrapped_repr(index)],
          }, opcode)
      elif opname[opcode] == "STORE_SUBSCR":
        rep = object_id_stack[0]
        self.append_to_trace_logger(loc, {
            "result_and_args": [object_id_stack[1], object_id_stack[2], rep],
        }, opcode)
      elif opname[opcode] == "SETUP_LOOP":
        self.loop_stack.append(instr.arg)
      elif opname[opcode] in binary_ops:
        if not is_post:
          self.pre_op_stack.append((object_id_stack[0], object_id_stack[1]))
        else:
          cur_inputs = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, {
              "result_and_args": [object_id_stack[0], cur_inputs[0], cur_inputs[1]],
          }, opcode)
      elif opname[opcode] in unary_ops:
        if not is_post:
          self.pre_op_stack.append(object_id_stack[0])
        else:
          cur_input = self.pre_op_stack.pop()
          self.append_to_trace_logger(loc, {
              "result_and_args": [object_id_stack[0], cur_input],
          }, opcode)
    self.already_in_receiver = False
