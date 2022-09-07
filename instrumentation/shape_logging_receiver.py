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
    self.trace_logger = []
    self.exec_len_key = "exec_len"
    self.label_to_instr_id = dict()
    super().__init__()

  # def get_label_to_instr_id(self, id_to_orig_bytecode, code_id, instr_arg):
  #   if code_id not in self.label_to_instr_id:
  #     self.label_to_instr_id[code_id] = dict()
  #     for id, instr in enumerate(id_to_orig_bytecode[code_id]):
  #       if isinstance(instr, Label):
  #         self.label_to_instr_id[code_id][instr] = id + 1
  #   #print(f'target_id = {code_id}, {instr_arg}')
  #   target_id = self.label_to_instr_id[code_id][instr_arg]
  #   return target_id



  def show_op_index(self, code_id: int, op_index: int, id_to_orig_bytecode: Dict[int, Bytecode]) -> str:
    return "op #" + str(op_index) + " (" + str(id_to_orig_bytecode[code_id][op_index]) + ")"

  def my_abstraction(self, obj):
    if hasattr(obj, 'shape'):
      return str(obj.shape)
    elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
      return str(obj)
    else:
      return 'obj'

  def get_repr(self, obj):
    if hasattr(obj, '__dict__'):
      return ObjectId(self.heap_object_tracking.get_object_id(obj)), type(obj), self.my_abstraction(obj)
    else:
      return ObjectId(0), type(obj), self.my_abstraction(obj)


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

  # def setup_trace_logger(self, code_id, opindex, id_to_orig_bytecode):
  #   key = (code_id, opindex, getlineno(id_to_orig_bytecode, code_id, opindex))
  #   if key not in self.trace_logger:
  #     self.trace_logger[key] = []
  #   if self.exec_len_key not in self.trace_logger:
  #     self.trace_logger[self.exec_len_key] = 0
  #   self.trace_logger[self.exec_len_key] += 1
  #   return key

  def append_to_trace_logger(self, loc, rest: Dict = None, opcode = -1, type = None):
    if bool(opcode == -1) == bool(type == None):
      raise Exception("Internal error: Either opcode or type argument must be set")
    record = {
        "loc": loc, # (method id, instruction id, line number)
        "type": type if type else opname[opcode],
        "exec_idx": len(self.trace_logger),
        "indentation": (len(self.loop_stack) + len(self.function_call_stack))
    }
    if rest:
      for k, v in rest.items():
        record[k] = v
    self.trace_logger.append(record)


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
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "fun_id": called_function,
              "args_id": function_args_id_stack}, opcode)
      else:
        object_id_stack = self.convert_stack_to_heap_id(stack)
        if opname[opcode] == "LOAD_CONST":
          rep = object_id_stack[0]
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "obj_id":  rep
          }, opcode)
        elif opname[opcode] == "LOAD_GLOBAL":
          rep = object_id_stack[0]
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "obj_id": rep,
              "var_name": instr.arg
          }, opcode)
        elif opname[opcode] == "LOAD_NAME" or opname[opcode] == "LOAD_FAST":
          rep = object_id_stack[0]
          resolved_frame = self.get_var_reference_frame(cur_frame, instr)
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "var_name": instr.arg,
              "frame_id": self.get_repr(resolved_frame),
              "obj_id": rep
          }, opcode)
        elif opname[opcode] == "STORE_NAME" or opname[opcode] == "STORE_FAST":
          rep = object_id_stack[0]
          resolved_frame = self.get_var_reference_frame(cur_frame, instr)
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "var_name": instr.arg,
              "frame_id": self.get_repr(resolved_frame),
              "obj_id": rep
          }, opcode)
        elif opname[opcode] == "LOAD_DEREF" or opname[opcode] == "STORE_DEREF":
          rep = object_id_stack[0]
          var_name = instr.arg.name
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "obj_id": rep,
              "var_name": var_name
          }, opcode)
        elif opname[opcode] == "BINARY_SUBSCR":
          rep = object_id_stack[0]
          if not is_post:
            index = object_id_stack[0]
            collection = object_id_stack[1]
            self.pre_op_stack.append((collection, index))
          else:
            collection, index = self.pre_op_stack.pop()
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
                "obj_id": rep,
                "idx_id": index,
                "base_id": collection
            }, opcode)
        elif opname[opcode] == "STORE_SUBSCR":
          rep = object_id_stack[0]
          loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
          self.append_to_trace_logger(loc, {
              "obj_id": rep,
              "idx_id": object_id_stack[2],
              "base_id": object_id_stack[1]
          }, opcode)
        elif opname[opcode] == "LOAD_CLOSURE":
          rep = object_id_stack[0]
          if isinstance(rep[0], ObjectId):
            if not object_id_stack[0][0].id in self.cell_to_frame:
              self.cell_to_frame[object_id_stack[0][0].id] = self.frame_tracking.get_object_id(cur_frame)
        elif opname[opcode] == "SETUP_LOOP":
          self.loop_stack.append(instr.arg)
        elif opname[opcode] in binary_ops:
          if not is_post:
            self.pre_op_stack.append((object_id_stack[0], object_id_stack[1]))
          else:
            cur_inputs = self.pre_op_stack.pop()
            loc = (code_id, opindex, getlineno(id_to_orig_bytecode ,code_id, opindex))
            self.append_to_trace_logger(loc, {
                  "obj_id": object_id_stack[0],
                  "oper1_id": cur_inputs[0],
                  "oper2_id": cur_inputs[1],
              }, opcode)
    self.already_in_receiver = False
