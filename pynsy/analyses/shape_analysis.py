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

object_name_space = dict()
name_space = dict()
last_object_id = -1
location_to_dimension = dict()
object_id_to_dimension = dict()
state = dict()
states = []


def has_result(row):
  return row["result_and_args"][0]["abs"] is not None


class DimensionSymbol:
  counter = 0

  def __init__(self):
    self.val = DimensionSymbol.counter
    DimensionSymbol.counter += 1

  def __repr__(self):
    return "d" + str(self.val)


def trim_locations():
  global location_to_dimension
  location_to_dimension = {
      k: v for k, v in location_to_dimension.items() if is_shape(v[0])
  }


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


def get_constraints(row):
  name = ""
  missing_values = row.notna()
  if missing_values.get("name"):
    name = row["name"]
  elif missing_values.get("function_name"):
    name = str(row["function_name"]) + "()"
  key = tuple([row[x] for x in keys] + [name])
  value = row["result_and_args"][0]
  object_type = None
  if key not in location_to_dimension:
    if is_shape_value(value):
      object_id = value["id"]
      shape = value["abs"]
      if object_id in object_id_to_dimension:
        old_shape = object_id_to_dimension[object_id][1]
        if old_shape != shape:
          logging.warning(
              "Inference algorithm's assumption that a tensor's shape is "
              "invariant is invalid."
          )
          raise Exception
        object_type = object_id_to_dimension[object_id][0]
      else:
        shape_type = []
        for _ in shape:
          shape_type.append(DimensionSymbol())
        object_id_to_dimension[object_id] = (shape_type, shape)
        object_type = shape_type
    else:
      object_type = None
    location_to_dimension[key] = (object_type, [value])
  else:
    if is_shape_value(value):
      location_to_dimension[key][1].append(value)
      object_id = value["id"]
      shape = value["abs"]
      shape_type = location_to_dimension[key][0]
      object_id_to_dimension[object_id] = (shape_type, shape)
  symbolic_dimensions = location_to_dimension[key][0]
  if is_shape(symbolic_dimensions):
    value = location_to_dimension[key][1][-1]
    state_update = dict(zip(symbolic_dimensions, value["abs"]))
    if not (state_update.items() <= state.items()):
      state.update(state_update)
      states.append(dict(state))


def format_dimension(i):
  if i in name_space:
    return name_space[i]
  else:
    return f"d{i}"


def str_solution(solution):
  ret = [""] * len(solution)
  for i, v in enumerate(solution):
    if isinstance(v, int):
      ret[i] = format_dimension(i)
    else:
      s = ""
      for c, var in zip(v[0], v[1]):
        if c == 1:
          s += format_dimension(var) + " +"
        else:
          s += f"{c}" + format_dimension(var) + " +"
      if len(s) > 0:
        s = s[0:-2]
      ret[i] = f"{s}"
  return ret


def find_solution(np_data, n_symbols, change_mask):
#  non_zero_indices = (np_data != 0).argmax(axis=0)
  max_variables = 4
  solution = [i for i in range(n_symbols)]
  coeffs = [1, 2, 3]
  for n_vars in range(2, max_variables + 1):
    domain = range(0, n_symbols)
    pick_n_vars = itertools.combinations(domain, n_vars)
    for vars in pick_n_vars:
      if all(map(lambda x: isinstance(solution[x], int), vars)):
        coeff_iterator = itertools.combinations_with_replacement(
            coeffs, n_vars - 1
        )
        for cs in coeff_iterator:
          b = np.zeros((n_symbols,), dtype=int)
          for c, var in itertools.zip_longest(cs, vars, fillvalue=-1):
            b[var] = c
#          fr = max([non_zero_indices[var] for var in vars])
          r = np_data.dot(b)
          if not np.dot(r, change_mask[:, vars[-1]]).any():
            solution[vars[-1]] = (cs, vars[:-1])
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
      return False, obj.shape
    except:
      return True, None
  elif isinstance(obj, int) or isinstance(obj, float):
    return False, obj
  return True, None


def process_event(record):
  global last_object_id
  result_and_args = record.get("result_and_args", None)
  if result_and_args:
    result = result_and_args[0]
    result_id = result["id"]
    if isinstance(result_id, ObjectId):
      last_object_id = result_id
    record_list.append(record)


def process_names():
  for object_id in object_name_space:
    for d, n in zip(
        object_id_to_dimension[object_id][0], object_name_space[object_id]
    ):
      name_space[d.val] = n


def process_termination():
  verbose = True
  if not record_list:
    log("No instructions were instrumented.")
    return

  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("shape_analysis", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)
  indices = df.apply(has_result, axis=1)
  df = df[indices]
  _ = df.apply(get_constraints, axis=1)
  trim_locations()
  if verbose:
    log("location_to_dimension")
    for k, v in location_to_dimension.items():
      print(f"{k} : {v}")
    log("object_id_to_dimension")
    for k, v in object_id_to_dimension.items():
      print(f"{k} : {v}")

  n_symbols = DimensionSymbol.counter
  data = []
  data2 = []
  row = [-1] * n_symbols
  data2.append(row)
  for state in states:
    row = [0] * n_symbols
    for i, v in state.items():
      row[i.val] = v
    data.append(row)
    data2.append(row)
  if not data:
    log("No data was instrumented.")
    return
  np_data = np.array(data)
  data2.pop()
  np_data2 = np.array(data2)
  change_mask = np_data - np_data2
  change_mask[change_mask != 0] = 1
  matrix_file = util.get_output_path("shape_analysis", "matrix.csv")
  pd.DataFrame(np_data).to_csv(matrix_file)

  process_names()
  solution = find_solution(np_data, n_symbols, change_mask)
  for i, v in enumerate(solution):
    if i in name_space:
      if isinstance(v, tuple):
        assert len(v[0]) == 1
        name_space[v[1][0]] = name_space[i]
  solution = str_solution(solution)
  if verbose:
    log("Printing solution...")
    for d, e in enumerate(solution):
      print(f"d{d} -> {e}")

  annotations_by_line_by_module = collections.defaultdict(
      lambda: collections.defaultdict(list)
  )
  for k, v in location_to_dimension.items():
    module_name, _, _, line_number, opcode, name = k
    line_number = int(line_number)

    symbolic_shape, concrete_values = v
    symbolic_shape = [solution[d.val] for d in symbolic_shape]
    concrete_shapes = concrete_values

    annotation = Annotation(
        opcode=opcode,
        name=name,
#        type=concrete_shape["type"],
        symbolic_shape=symbolic_shape,
        concrete_shape=[concrete_shape["abs"] for concrete_shape in concrete_shapes],
    )
    annotations_by_line_by_module[module_name][line_number].append(annotation)

  modules_by_name = {}
  module_text_by_name = {}
  for module_name, annotations_by_line in annotations_by_line_by_module.items():
    module = module_loader.import_method_from_module(module_name)
    modules_by_name[module_name] = module

    module_path = module.__file__
    with open(module_path, "r") as f:
      module_text = f.read()
    module_lines = module_text.split("\n")
    module_text_by_name[module_name] = module_text
    sorted_line_numbers = sorted(annotations_by_line)

    def transform_line_number(line_number):
      # Explanation:
      # - The line numbers in the trace are one-indexed, so subtracting one is
      #   necessary to get true line number for indexing into the Python list of
      #   file content lines.
      return max(0, line_number - 1)

    annotated_lines = []
    last_line_number = 0

    for line_number in sorted_line_numbers:
      if last_line_number == 0:
        start_index = 0
      else:
        start_index = transform_line_number(last_line_number)
      end_index = transform_line_number(line_number)
      annotated_lines.extend(module_lines[start_index:end_index])
      last_line_number = line_number

      annotated_line = module_lines[end_index]
      indent = count_leading_spaces(annotated_line)
      annotations = annotations_by_line[line_number]
      for annotation in annotations:
        s = annotation.to_string(indent=indent)
        annotated_lines.append(s)

    end_index = transform_line_number(last_line_number)
    annotated_lines.extend(module_lines[end_index:])

    if verbose:
      log(f"Shape annotations for: {module_name}")
      print(termcolor.colored("=" * 80, attrs=["bold"]))
      for line in annotated_lines:
        print(line)
      print(termcolor.colored("=" * 80, attrs=["bold"]))
    annotated_source = "\n".join(annotated_lines)
    annotations_file = util.get_output_path(
        "shape_analysis", f"annotations/{module_name}.py"
    )
    log(f"Saving annotated source file: {annotations_file}.")
    with open(annotations_file, "w") as out:
      out.write("# Auto-generated file with array shape annotations.\n")
      out.write(f"# Original file: {module_path}\n\n")
      out.write(annotated_source)

  annotations_file = util.get_output_path("shape_analysis", "annotations.txt")
  with open(annotations_file, "w") as out:
    log(f"Saving annotations to {annotations_file}.")
    for (
        module_name,
        annotations_by_line,
    ) in annotations_by_line_by_module.items():
      for line_number, annotations in annotations_by_line.items():
        s = []
        for annotation in annotations:
          name = get_name(annotation.opcode, annotation.name)
          shape = tuple(annotation.symbolic_shape)
          concrete = annotation.concrete_shape
          s.append((name, shape, concrete))
        out.write(f"{module_name}@{line_number}:\n")
        for name, shape, concrete in s:
          out.write(f"    {name}: {shape} {concrete}\n")


def annotate_shape(obj, shape):
  # This works because LOAD is executed right before calls to this function.
  if isinstance(last_object_id, ObjectId):
    object_name_space[last_object_id] = shape
  else:
    log(f"Failed shape annotation for {obj}: {shape}", color="red")
