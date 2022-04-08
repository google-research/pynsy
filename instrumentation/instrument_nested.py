from types import CodeType
from bytecode import Bytecode, Instr

from .instrument import instrument_bytecode
from .util import clone_bytecode_empty_body, is_const_load_function

from typing import Any, Dict, List, Tuple

def extract_all_codeobjects(codeobject: CodeType) -> Tuple[Dict[int, Bytecode], Dict[CodeType, int]]:
  seen_objects: List[Any] = []
  next_code_id = 0

  code_id_to_bytecode = {}
  code_object_to_id = {}

  def explore(obj: CodeType) -> None:
    nonlocal next_code_id

    if obj in seen_objects or obj is None:
      pass
    else:
      current_id = next_code_id
      next_code_id += 1

      code_id_to_bytecode[current_id] = Bytecode.from_code(obj)
      code_object_to_id[obj] = current_id
      for elem in code_id_to_bytecode[current_id]:
        if is_const_load_function(elem):
          explore(elem.arg)

  explore(codeobject)
  return code_id_to_bytecode, code_object_to_id

def compile_and_swap(id_to_instrumented_bytecode: Dict[int, Bytecode], code_to_id: Dict[CodeType, int]) -> Dict[int, Bytecode]:
  seen_objects = []

  code_id_to_compiled: Dict[int, CodeType] = {}
  code_id_to_swapped: Dict[int, Bytecode] = {}

  def explore(code_id: int) -> CodeType:
    if code_id in seen_objects:
      return code_id_to_compiled[code_id]
    else:
      seen_objects.append(code_id)

      out = clone_bytecode_empty_body(id_to_instrumented_bytecode[code_id])
      for elem in id_to_instrumented_bytecode[code_id]:
        if is_const_load_function(elem) and elem.arg in code_to_id:
          out.append(Instr(
            name = "LOAD_CONST",
            arg = explore(code_to_id[elem.arg]),
            lineno = elem.lineno
          ))
        else:
          out.append(elem)

      code_id_to_compiled[code_id] = out.to_code()
      code_id_to_swapped[code_id] = out
      return code_id_to_compiled[code_id]

  for code_id in id_to_instrumented_bytecode.keys():
    explore(code_id)

  return code_id_to_swapped

def instrument_extracted(id_to_bytecode: Dict[int, Bytecode], code_to_id: Dict[CodeType, int]) -> Dict[int, Bytecode]:
  id_to_instrumented_bytecode = {}
  for code_id in id_to_bytecode.keys():
    id_to_instrumented_bytecode[code_id] = instrument_bytecode(id_to_bytecode[code_id], code_id)

  return compile_and_swap(id_to_instrumented_bytecode, code_to_id)

def instrument_nested_code(codeobject: CodeType) -> Bytecode:
  id_to_bytecode, code_to_id = extract_all_codeobjects(codeobject)
  id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

  return id_to_bytecode_new_codeobjects[code_to_id[codeobject]]
