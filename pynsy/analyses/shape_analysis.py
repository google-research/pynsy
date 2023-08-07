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

import collections
from collections.abc import Sequence
import dataclasses
from datetime import datetime
import io
import itertools
import logging
from typing import Any

import numpy as np
import pandas as pd
import termcolor

from pynsy.analyses import util
from pynsy.instrumentation import module_loader
from pynsy.instrumentation import logging
from pynsy.instrumentation import util as instrumentation_util

ObjectId = instrumentation_util.ObjectId
log = logging.logger(__name__)

record_list = []

now = datetime.now()
timestamp = int(round(now.timestamp()))
keys = ["module_name", "method_id", "instruction_id", "lineno", "type"]


@dataclasses.dataclass
class Annotation:
  """A Python object shape annotation.

  Args:
    opcode: The opcode of the Python bytecode instruction that produced the
      object.
    name: The name of the object, or the empty string if unknown.
    type: The type of the object.
    symbolic_shape: The symbolic shape of the object.
    concrete_shape: The concrete shape of the object.
  """

  opcode: str
  name: str
  symbolic_shape: Any
  concrete_shape: Any

  def to_string(
      self, indent: int = 0, *, short: bool = True, color: bool = True
  ) -> str:
    out = io.StringIO()
    out.write(" " * indent)
    name = get_name(self.opcode, self.name)
    msg = f"# {name}: {self.symbolic_shape} {self.concrete_shape}"
    out.write(msg)
    s = out.getvalue()
    if color:
      s = termcolor.colored(s, color="magenta", attrs=["bold"])
    return s


nicknames = {
    "UNARY_POSITIVE": "+",
    "UNARY_NEGATIVE": "-",
    "UNARY_NOT": "not",
    "UNARY_INVERT": "~",
    "GET_ITER": "iter",
    "GET_YIELD_FROM_ITER": "yield",
    "BINARY_POWER": "**",
    "BINARY_MULTIPLY": "*",
    "BINARY_MATRIX_MULTIPLY": "@",
    "BINARY_FLOOR_DIVIDE": "//",
    "BINARY_TRUE_DIVIDE": "/",
    "BINARY_MODULO": "%",
    "BINARY_ADD": "+",
    "BINARY_SUBTRACT": "-",
    "BINARY_SUBSCR": "__getitem__",
    "BINARY_LSHIFT": "<<",
    "BINARY_RSHIFT": ">>",
    "BINARY_AND": "&",
    "BINARY_XOR": "^",
    "BINARY_OR": "|",
    "COMPARE_OP": "cmp",
    "INPLACE_POWER": "**=",
    "INPLACE_MULTIPLY": "*=",
    "INPLACE_MATRIX_MULTIPLY": "@=",
    "INPLACE_FLOOR_DIVIDE": "//=",
    "INPLACE_TRUE_DIVIDE": "/=",
    "INPLACE_MODULO": "%=",
    "INPLACE_ADD": "+=",
    "INPLACE_SUBTRACT": "-=",
    "INPLACE_LSHIFT": "<<=",
    "INPLACE_RSHIFT": ">>=",
    "INPLACE_AND": "&=",
    "INPLACE_XOR": "^=",
    "INPLACE_OR": "|=",
    # "MAKE_FUNCTION": "<def>",
    # "LOAD_NAME": "<load>",
    # "LOAD_FAST": "<load>",
    # "LOAD_DEREF": "<load>",
    # "LOAD_CLOSURE": "<load>",
    # "LOAD_ATTR": "<load>",
    # "LOAD_CONST": "<load>",
    # "LOAD_GLOBAL": "<load>",
    # "CALL_FUNCTION": "<call>",
    # "CALL_FUNCTION_KW": "<call>",
    # "CALL_METHOD": "<call>",
    # "RETURN_FUNCTION": "<call>",
    # "RETURN_FUNCTION_KW": "<call>",
    # "RETURN_METHOD": "<call>",
}



# def has_result(row):
#   return row["result_and_args"][0]["abs"] is not None
#

class UniqueIdForKey:

  def __init__(self):
    self.counter = 0
    self.key_to_id = dict()
    self.id_to_key = list()

  def get_id(self, key):
    if key in self.key_to_id:
      return self.key_to_id[key]
    else:
      self.key_to_id[key] = self.counter
      self.id_to_key.append(key)
      self.counter += 1
      return self.counter - 1

  def get_key(self, id):
    return self.id_to_key[id] if id < len(self.id_to_key) else None


class UniqueId:
  def __init__(self, count):
    self.counter = count

  def get_fresh_id(self):
    self.counter += 1
    return self.counter - 1

  def num_ids(self):
    return self.counter

# def trim_locations():
#   global location_to_dimension
#   location_to_dimension = {
#       k: v for k, v in location_to_dimension.items() if is_shape(v[0])
#   }


def flatten(l):
  ret = []
  for t in l:
    if isinstance(t, tuple):
      if isinstance(t[2], tuple) or isinstance(t[2], list):
        ret = ret + list(t[2])
  return ret


def is_shape_value(value):
  return is_shape(value["abs"])


def is_shape(s):
  return isinstance(s, list) or isinstance(s, tuple)



# def format_dimension(i):
#   if i in name_space:
#     return name_space[i]
#   else:
#     return f"d{i}"


# def str_solution(solution):
#   ret = [""] * len(solution)
#   for i, v in enumerate(solution):
#     if isinstance(v, int):
#       ret[i] = format_dimension(i)
#     else:
#       s = ""
#       for c, var in zip(v[0], v[1]):
#         if c == 1:
#           s += format_dimension(var) + " +"
#         else:
#           s += f"{c}" + format_dimension(var) + " +"
#       if len(s) > 0:
#         s = s[0:-2]
#       ret[i] = f"{s}"
#   return ret

class TemplateInstance:
  def __init__(self, template, vars):
    self.template = template
    self.vars = vars

  def __str__(self):
    return f"{self.template.name}({self.vars})"

class Template:
  def __init__(self, name, n_vars, predicate):
    self.name = name
    self.n_vars = n_vars
    self.predicate = predicate

  def get_instance(self, vars):
    return TemplateInstance(self, vars)

templates = [
    Template("equality", 2, lambda state, vars: state.get(vars[0], 0) == state.get(vars[1])),
    Template("product", 3, lambda state, vars: state.get(vars[0], 0) == state.get(vars[1], 0) * state.get(vars[2], 0)),
]

def find_solution(states, location_id_to_type, n_symbols):
  solution = [i for i in range(n_symbols)]
  for location_id, state_list in states.items():
    exclude = location_id_to_type[location_id]
    for template in templates:
      for var in exclude[0]:
        vars_list = [i for i in range(n_symbols) if i != var and isinstance(solution[i], int)]
        vars_iter = itertools.combinations(vars_list, template.n_vars - 1)
        for vars in vars_iter:
          vars = [var] + list(vars)
          holds = True
          for state in state_list:
            if not template.predicate(state, vars):
              holds = False
              break
          if holds:
            solution[var] = template.get_instance(vars[1:])
            break
  return solution


def get_name(opcode, name):
  if isinstance(name, str) and name:
    return name
  else:
    return nicknames.get(opcode, f"<{opcode}>")


def count_leading_spaces(s: str) -> int:
  return len(s) - len(s.lstrip(" "))


def abstraction(obj):
  if hasattr(obj, "shape"):
    try:
      return True, obj.shape
    except:
      return True, None
  return True, None

def get_types_in_method(method_id, method_id_to_dimensions):
  if method_id not in method_id_to_dimensions:
    method_id_to_dimensions[method_id] = set()
  return method_id_to_dimensions[method_id]


def get_symbolic_type(value, vars):
  abs = value["abs"]
  symbolic_shape_type = []
  for _ in abs:
    symbolic_shape_type.append(vars.get_fresh_id())
  return symbolic_shape_type

def get_state_update(symbolic_type, value):
  state_update = dict(zip(symbolic_type, value["abs"]))
  return state_update


last_call_location_id = None
def create_states(record_list):
  states = dict()
  location_id_to_type = dict()
  state_stack = []
  method_id_to_types = dict()
  state = dict()
  indentation = -1
  location_to_id = UniqueIdForKey()
  vars = UniqueId(0)
  global last_call_location_id

  rlen = len(record_list)
  is_call = False
  for i in range(rlen):
    row = record_list[i]
    name = ""
    if "name" in row:
      name = row["name"]
    elif "function_name" in row:
      name = str(row["function_name"]) + "()"

    if row["type"].startswith("CALL_"):
      is_call = True
      indentation = row["indentation"]
      location = tuple([row[x] for x in keys] + [name])
      location_id = location_to_id.get_id(location)
      last_call_location_id = location_id
    else:
      if row["type"].startswith("RETURN_"):
        if is_call:
          is_call = False
        else:
          state = state_stack.pop()
      method_id = row["method_id"]
      if is_call:
        is_call = False
        if row["indentation"] == indentation + 1:
          state_stack.append(state)
          types_in_method = get_types_in_method(method_id, method_id_to_types)
          state = {key: state[key] for key in state if key not in types_in_method}
      value = row["result_and_args"][0]
      if is_shape_value(value):
        location = tuple([row[x] for x in keys] + [name])
        location_id = location_to_id.get_id(location)
        if location_id not in location_id_to_type:
          symbolic_type = get_symbolic_type(value, vars)
          location_id_to_type[location_id] = (symbolic_type, [value])
        else:
          symbolic_type = location_id_to_type[location_id][0]
          location_id_to_type[location_id][1].append(value)
        method_id = row["method_id"]
        types_in_method = get_types_in_method(method_id, method_id_to_types)
        types_in_method.update(symbolic_type)

        value = location_id_to_type[location_id][1][-1]
        state_update = get_state_update(symbolic_type, value)
        state.update(state_update)
        if location_id not in states:
          states[location_id] = list()
        states[location_id].append(dict(state))
  return states, location_id_to_type, location_to_id, method_id_to_types, vars.counter


def process_event(record):
  record_list.append(record)


# def process_names():
#   for object_id in object_name_space:
#     for d, n in zip(
#         object_id_to_dimension[object_id][0], object_name_space[object_id]
#     ):
#       name_space[d.val] = n


def process_termination():
  verbose = True
  if not record_list:
    log("No instructions were instrumented.")
    return

  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("shape_analysis", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)

  states, location_id_to_type, location_to_id, method_id_to_types, n_symbols = create_states(record_list)
  for k, v in location_id_to_type.items():
    print(f"{location_to_id.get_key(k)} : {v}")
  solution = find_solution(states, location_id_to_type, n_symbols)
  for i, v in enumerate(solution):
    print(f"{i} : {v}")

#   process_names()
#   solution = find_solution(np_data, n_symbols, change_mask)
#   for i, v in enumerate(solution):
#     if i in name_space:
#       if isinstance(v, tuple):
#         assert len(v[0]) == 1
#         name_space[v[1][0]] = name_space[i]
#   solution = str_solution(solution)
#   if verbose:
#     log("Printing solution...")
#     for d, e in enumerate(solution):
#       print(f"d{d} -> {e}")
#
#   annotations_by_line_by_module = collections.defaultdict(
#       lambda: collections.defaultdict(list)
#   )
#   for k, v in location_to_dimension.items():
#     module_name, _, _, line_number, opcode, name = k
#     line_number = int(line_number)
#
#     symbolic_shape, concrete_values = v
#     symbolic_shape = [solution[d.val] for d in symbolic_shape]
#     concrete_shapes = concrete_values
#
#     annotation = Annotation(
#         opcode=opcode,
#         name=name,
# #        type=concrete_shape["type"],
#         symbolic_shape=symbolic_shape,
#         concrete_shape=[concrete_shape["abs"] for concrete_shape in concrete_shapes],
#     )
#     annotations_by_line_by_module[module_name][line_number].append(annotation)
#
#   modules_by_name = {}
#   module_text_by_name = {}
#   for module_name, annotations_by_line in annotations_by_line_by_module.items():
#     module = module_loader.import_method_from_module(module_name)
#     modules_by_name[module_name] = module
#
#     module_path = module.__file__
#     with open(module_path, "r") as f:
#       module_text = f.read()
#     module_lines = module_text.split("\n")
#     module_text_by_name[module_name] = module_text
#     sorted_line_numbers = sorted(annotations_by_line)
#
#     def transform_line_number(line_number):
#       # Explanation:
#       # - The line numbers in the trace are one-indexed, so subtracting one is
#       #   necessary to get true line number for indexing into the Python list of
#       #   file content lines.
#       return max(0, line_number - 1)
#
#     annotated_lines = []
#     last_line_number = 0
#
#     for line_number in sorted_line_numbers:
#       if last_line_number == 0:
#         start_index = 0
#       else:
#         start_index = transform_line_number(last_line_number)
#       end_index = transform_line_number(line_number)
#       annotated_lines.extend(module_lines[start_index:end_index])
#       last_line_number = line_number
#
#       annotated_line = module_lines[end_index]
#       indent = count_leading_spaces(annotated_line)
#       annotations = annotations_by_line[line_number]
#       for annotation in annotations:
#         s = annotation.to_string(indent=indent)
#         annotated_lines.append(s)
#
#     end_index = transform_line_number(last_line_number)
#     annotated_lines.extend(module_lines[end_index:])
#
#     if verbose:
#       log(f"Shape annotations for: {module_name}")
#       print(termcolor.colored("=" * 80, attrs=["bold"]))
#       for line in annotated_lines:
#         print(line)
#       print(termcolor.colored("=" * 80, attrs=["bold"]))
#     annotated_source = "\n".join(annotated_lines)
#     annotations_file = util.get_output_path(
#         "shape_analysis", f"annotations/{module_name}.py"
#     )
#     log(f"Saving annotated source file: {annotations_file}.")
#     with open(annotations_file, "w") as out:
#       out.write("# Auto-generated file with array shape annotations.\n")
#       out.write(f"# Original file: {module_path}\n\n")
#       out.write(annotated_source)
#
#   annotations_file = util.get_output_path("shape_analysis", "annotations.txt")
#   with open(annotations_file, "w") as out:
#     log(f"Saving annotations to {annotations_file}.")
#     for (
#         module_name,
#         annotations_by_line,
#     ) in annotations_by_line_by_module.items():
#       for line_number, annotations in annotations_by_line.items():
#         s = []
#         for annotation in annotations:
#           name = get_name(annotation.opcode, annotation.name)
#           shape = tuple(annotation.symbolic_shape)
#           concrete = annotation.concrete_shape
#           s.append((name, shape, concrete))
#         out.write(f"{module_name}@{line_number}:\n")
#         for name, shape, concrete in s:
#           out.write(f"    {name}: {shape} {concrete}\n")


def annotate_shape(obj, shape):
  pass
  # This works because LOAD is executed right before calls to this function.
  # if isinstance(last_object_id, ObjectId):
  #   object_name_space[last_object_id] = shape
  # else:
  #   log(f"Failed shape annotation for {obj}: {shape}", color="red")
