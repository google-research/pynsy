from bytecode import Bytecode, Instr
import inspect

from types import CodeType, FrameType
from typing import Any


# newtype to track object IDs
class ObjectId(object):
  def __init__(self, id: int) -> None:
    self.id = id

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, ObjectId):
      return self.id == other.id
    return False

  def __repr__(self):
    return '#' + str(self.id)

def get_instrumented_program_frame() -> FrameType:
  is_next_frame = False
  for frame_container in inspect.getouterframes(inspect.currentframe()):
    if is_next_frame:
      return frame_container.frame
    elif frame_container.function == "py_instrument_receiver":
      is_next_frame = True
  raise Exception("Frame in instrumented code not found")


def clone_bytecode_empty_body(code: Bytecode) -> Bytecode:
  instrumented = Bytecode()
  instrumented.argcount = code.argcount
  instrumented.kwonlyargcount = code.kwonlyargcount
  instrumented.first_lineno = code.first_lineno
  instrumented.name = code.name
  instrumented.filename = code.filename
  instrumented.docstring = code.docstring
  instrumented.cellvars = code.cellvars
  instrumented.freevars = code.freevars
  instrumented.flags = code.flags

  instrumented.argnames = code.argnames

  return instrumented


def is_const_load_function(instr: object) -> bool:
  return isinstance(instr, Instr) and instr.name == "LOAD_CONST" and isinstance(
      instr.arg, CodeType)
