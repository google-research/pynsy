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

from datetime import datetime
import itertools
import logging
import numpy as np
import pandas as pd

from pynsy.instrumentation import util

record_list = []

curr_dt = datetime.now()

timestamp = int(round(curr_dt.timestamp()))
keys = ["module_name", "method_id", "instruction_id", "lineno", "type"]

nick_names = {
    "UNARY_POSITIVE": "+",
    "UNARY_NEGATIVE": "-",
    "UNARY_NOT": "not",
    "UNARY_INVERT": "invert",
    "GET_ITER": "iter",
    "GET_YIELD_FROM_ITER": "yield",
    "BINARY_POWER": "**",
    "BINARY_MULTIPLY": "*",
    "BINARY_MATRIX_MULTIPLY": "matmul",
    "BINARY_FLOOR_DIVIDE": "//",
    "BINARY_TRUE_DIVIDE": "/",
    "BINARY_MODULO": "%",
    "BINARY_ADD": "+",
    "BINARY_SUBTRACT": "-",
    "BINARY_SUBSCR": "[]",
    "BINARY_LSHIFT": "<<",
    "BINARY_RSHIFT": ">>",
    "BINARY_AND": "&",
    "BINARY_XOR": "^",
    "BINARY_OR": "|",
    "COMPARE_OP": "cmp",
    "INPLACE_POWER": "**",
    "INPLACE_MULTIPLY": "*",
    "INPLACE_MATRIX_MULTIPLY": "matmul",
    "INPLACE_FLOOR_DIVIDE": "//",
    "INPLACE_TRUE_DIVIDE": "/",
    "INPLACE_MODULO": "%",
    "INPLACE_ADD": "+",
    "INPLACE_SUBTRACT": "-",
    "INPLACE_LSHIFT": "<<",
    "INPLACE_RSHIFT": ">>",
    "INPLACE_AND": "&",
    "INPLACE_XOR": "^",
    "INPLACE_OR": "|",
    "MAKE_FUNCTION": "def",
    "LOAD_NAME": "load",
    "LOAD_FAST": "load",
    "LOAD_DEREF": "load",
    "LOAD_CLOSURE": "load",
    "LOAD_ATTR": "load",
    "LOAD_CONST": "load",
    "LOAD_GLOBAL": "load",
    "CALL_FUNCTION": "call",
    "CALL_FUNCTION_KW": "call",
    "CALL_METHOD": "call",
    "RETURN_FUNCTION": "call",
    "RETURN_FUNCTION_KW": "call",
    "RETURN_METHOD": "call",
}

object_name_space = dict()
name_space = dict()
last_oid = -1
log_file = f"trace.csv"
locationToDimension = dict()
objectIdToDimension = dict()
state = dict()
states = []


def has_result(row):
  return row["result_and_args"][0]["abs"] is not None


def is_blank(val):
  return val != val


def result_and_args(row):
  if row["type"] == "LOAD_ATTR":
    row["result_and_args"] = [row["result"], row["base"], row["attr_name"]]
  elif row["type"] == "STORE_ATTR":
    row["result_and_args"] = [
        row["result"],
        row["base"],
        row["attr_name"],
        row["operand"],
    ]
  elif row["type"] == "BINARY_SUBSCR":
    row["result_and_args"] = [row["result"], row["base"], row["index"]]
  elif row["type"] == "STORE_SUBSCR":
    row["result_and_args"] = [
        row["result"],
        row["base"],
        row["index"],
        row["operand"],
    ]
  elif not is_blank(row["operand"]):
    row["result_and_args"] = [row["result"], row["operand"]]
  elif not is_blank(row["operand1"]) or not is_blank(row["operand2"]):
    row["result_and_args"] = [row["result"], row["operand1"], row["operand2"]]
  elif not is_blank(row["args_list"]):
    row["result_and_args"] = [row["result"]] + row["args_list"]
  else:
    row["result_and_args"] = [row["result"]]
  return row


class DimensionSymbol:
  counter = 0

  def __init__(self):
    self.val = DimensionSymbol.counter
    DimensionSymbol.counter += 1

  def __repr__(self):
    return "d" + str(self.val)


def trim_locations():
  global locationToDimension
  locationToDimension = {
      k: v for k, v in locationToDimension.items() if is_shape(v[0])
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
  if not is_blank(row["name"]):
    name = row["name"]
  elif not is_blank(row["function_name"]):
    name = str(row["function_name"]) + "()"
  key = tuple([row[x] for x in keys] + [name])
  value = row["result_and_args"][0]
  type = None
  if key not in locationToDimension:
    if is_shape_value(value):
      oid = value["id"]
      shape = value["abs"]
      if oid in objectIdToDimension:
        old_shape = objectIdToDimension[oid][1]
        if old_shape != shape:
          logging.warning(
              "Inference algorithm's assumption that a tensor's shape is"
              " invariant is invalid."
          )
          raise Exception
        type = objectIdToDimension[oid][0]
      else:
        shape_type = []
        for _ in shape:
          shape_type.append(DimensionSymbol())
        objectIdToDimension[oid] = (shape_type, shape)
        type = shape_type
    else:
      type = None
    locationToDimension[key] = (type, [value])
  else:
    locationToDimension[key][1].append(value)
  symbolic_dimensions = locationToDimension[key][0]
  if is_shape(symbolic_dimensions):
    value = locationToDimension[key][1][-1]
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


def find_solution(np_data, n_symbols):
  non_zero_indices = (np_data != 0).argmax(axis=0)
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
          fr = max([non_zero_indices[var] for var in vars])
          r = np_data.dot(b)
          if not r[fr:].any():
            solution[vars[-1]] = (cs, vars[:-1])
            break
  return solution


def get_name(type, name):
  if isinstance(name, str) and len(name) > 0:
    return name
  else:
    return nick_names[type]


def abstraction(obj):
  if hasattr(obj, "shape"):
    return False, obj.shape
  elif isinstance(obj, int) or isinstance(obj, float):
    return False, obj
  return True, None


def process_event(record):
  global last_oid
  result_and_args = record.get("result_and_args", None)
  if result_and_args:
    result_id = result_and_args[0]["id"]
    if isinstance(result_id, util.ObjectId):
      last_oid = result_id
    record_list.append(record)


def process_names():
  for oid in object_name_space.keys():
    for d, n in zip(objectIdToDimension[oid][0], object_name_space[oid]):
      name_space[d.val] = n


def process_termination():
  df = pd.DataFrame(record_list)
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
  indices = df.apply(has_result, axis=1)
  df = df[indices]
  df = df.apply(get_constraints, axis=1)
  trim_locations()
  print("locationToDimension")
  for k, v in locationToDimension.items():
    print(f"{k} : {v}")
  print("objectIdToDimension")
  for k, v in objectIdToDimension.items():
    print(f"{k} : {v}")

  n_symbols = DimensionSymbol.counter
  data = []
  for state in states:
    row = [0] * n_symbols
    for i, v in state.items():
      row[i.val] = v
    data.append(row)
  np_data = np.array(data)
  pd.DataFrame(np_data).to_csv("matrix_" + log_file)

  process_names()
  solution = find_solution(np_data, n_symbols)
  for i, v in enumerate(solution):
    if i in name_space:
      if isinstance(v, tuple):
        assert len(v[0]) == 1
        name_space[v[1][0]] = name_space[i]
  solution = str_solution(solution)
  print("Printing solution ...")
  for d, e in enumerate(solution):
    print(f"d{d} -> {e}")

  line_annotations = dict()
  for k, v in locationToDimension.items():
    key = k[0], k[3]
    if key not in line_annotations:
      line_annotations[key] = []
    line_annotations[key].append((k[4], k[5], v[0], v[1][0]["abs"]))
  with open("annotations_" + log_file, "w") as out:
    print("Saving annotations ...\n")
    for line, annot in line_annotations.items():
      s = [
          (get_name(t, n), tuple([f"{solution[d.val]}" for d in a]), c)
          for t, n, a, c in annot
      ]
      out.write(f"{line[0]}@{line[1]}:\n")
      for name, shape, concrete in s:
        out.write(f"    {name}: {shape} {concrete}\n")


def annotate_shape(obj, shape):
  object_name_space[last_oid] = shape
