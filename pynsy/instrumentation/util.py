# Copyright 2023 The pynsy Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import json
from types import CodeType
from types import FrameType
from typing import Any

from bytecode import Bytecode
from bytecode import Instr


def get_instrumented_program_frame() -> FrameType:
  is_next_frame = False
  frame = inspect.currentframe()
  for frame_container in inspect.getouterframes(frame, context=0):
    if is_next_frame:
      return frame_container.frame
    elif frame_container.function == "pynsy_receiver":
      is_next_frame = True
  raise Exception("Frame in instrumented code not found")


def serialize(obj):
  if isinstance(obj, ObjectId):
    serial = obj.id
    return serial
  elif isinstance(obj, type):
    serial = str(obj)
    return serial
  else:
    return json.dumps(obj)


# newtype to track object IDs
class ObjectId(object):

  def __init__(self, id: int) -> None:
    self.id = id

  def __hash__(self):
    return self.id

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, ObjectId):
      return self.id == other.id
    return False

  def __repr__(self):
    return "#" + str(self.id)


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
  return (
      isinstance(instr, Instr)
      and instr.name == "LOAD_CONST"
      and isinstance(instr.arg, CodeType)
  )
