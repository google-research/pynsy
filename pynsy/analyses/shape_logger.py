import logging
from datetime import datetime

import itertools
import numpy as np
import pandas as pd

curr_dt = datetime.now()

timestamp = int(round(curr_dt.timestamp()))
columns = ['operand', 'operand1', 'operand2', 'args_list', 'base', 'index']
keys = ['module_name', 'method_id', 'instruction_id', 'lineno', 'type']

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
    "RETURN_METHOD": "call"

}

object_name_space = dict()
name_space = dict()
last_oid = -1
log_file = f"trace.csv"
locationToDimension = dict()
objectIdToDimension = dict()
state = dict()
states = []


def is_non_None_row(row):
  for col in columns:
    if isinstance(row[col], tuple):
      return True
  if row['args_list'] is not None and isinstance(row['args_list'], list):
    curr_value = row['args_list']
    for arg in curr_value:
      if isinstance(arg, tuple):
        return True
  return False

def has_result(row):
  return isinstance(row['result'], tuple)

def is_blank(val):
  return val != val

def result_and_args(row):
  if row['type'] == 'LOAD_ATTR':
    row['result_and_args'] = [row['result'], row['base'], row['attr_name']]
  elif row['type'] == 'STORE_ATTR':
    row['result_and_args'] = [row['result'], row['base'], row['attr_name'], row['operand']]
  elif row['type'] == 'BINARY_SUBSCR':
    row['result_and_args'] = [row['result'], row['base'], row['index']]
  elif row['type'] == 'STORE_SUBSCR':
    row['result_and_args'] = [row['result'], row['base'], row['index'], row['operand']]
  elif not is_blank(row['operand']):
    row['result_and_args'] = [row['result'], row['operand']]
  elif not is_blank(row['operand1']) or not is_blank(row['operand2']):
    row['result_and_args'] = [row['result'], row['operand1'], row['operand2']]
  elif not is_blank(row['args_list']):
    row['result_and_args'] = [row['result']] + row['args_list']
  else:
    row['result_and_args'] = [row['result']]
  return row

def wrap_result(row):
  if isinstance(row['result'], tuple):
    row['result_and_args'] = [row['result']]
  return row

class DimensionSymbol:
  counter = 0

  def __init__(self):
    self.val = DimensionSymbol.counter
    DimensionSymbol.counter += 1

  def __repr__(self):
    return 'd' + str(self.val)


def trim_locations():
  global locationToDimension
  locationToDimension = {k:v for k, v in locationToDimension.items() if is_shape(v[0])}

def flatten(l):
  ret = []
  for t in l:
    if isinstance(t, tuple):
      if isinstance(t[2], tuple) or isinstance(t[2], list):
        ret = ret + list(t[2])
  return ret

def is_shape_value(value):
  return isinstance(value, tuple) and len(value) == 3 and is_shape(value[2])

def is_shape(s):
  return isinstance(s, list) or isinstance(s, tuple)

def get_constraints(row):
  name = ''
  if not is_blank(row['var_name']):
    name = row['var_name']
  elif not is_blank(row['function_name']):
    name = str(row['function_name']) + '()'
  elif not is_blank(row['attr_name']):
    name = '.' + row['attr_name']
  key = tuple([row[x] for x in keys] + [name])
  value = row['result']
  type = None
  if key not in locationToDimension:
    if is_shape_value(value):
      oid = value[0]
      if oid in objectIdToDimension:
        shape = objectIdToDimension[oid][1]
        if shape != value[2]:
          logging.warning("Inference algorithm's assumption that a tensor's shape is invariant is invalid.")
          raise Exception
        type = objectIdToDimension[oid][0]
      else:
        shape = value[2]
        shape_type = []
        for d in shape:
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
    state_update = dict(zip(symbolic_dimensions, value[2]))
    if not (state_update.items() <= state.items()):
      state.update(state_update)
      states.append(dict(state))

def format_dimension(i):
  if i in name_space:
    return name_space[i]
  else:
    return f"d{i}"

def str_solution(solution):
  ret = [""]*len(solution)
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
  non_zero_indices = (np_data!=0).argmax(axis=0)
  max_variables = 4
  solution = [i for i in range(n_symbols)]
  coeffs = [1, 2, 3]
  for n_vars in range(2, max_variables + 1):
    domain = range(0, n_symbols)
    pick_n_vars = itertools.combinations(domain, n_vars)
    for vars in pick_n_vars:
      if all(map(lambda x: isinstance(solution[x], int), vars)):
        coeff_iterator = itertools.combinations_with_replacement(coeffs, n_vars - 1)
        for cs in coeff_iterator:
          b = np.zeros((n_symbols,), dtype=int)
          for c, var in itertools.zip_longest(cs, vars, fillvalue = -1):
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
  if hasattr(obj, 'shape'):
    return False, obj.shape
  elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
    return False, obj
  return True, None

def process_event(record):
  global last_oid
  if 'result' in record and is_shape_value(record['result']):
    last_oid = record['result'][0]
  return record


def process_names():
  for oid in object_name_space.keys():
    for d, n in zip(objectIdToDimension[oid][0], object_name_space[oid]):
      name_space[d.val] = n

def process_termination(record_list):
  df = pd.DataFrame(record_list)
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
  indices = df.apply(has_result, axis=1)
  df = df[indices]
  df = df.drop(columns, axis=1)
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
#    row = [float("NaN")] * n_symbols
    row = [0] * n_symbols
    for i, v in state.items():
      row[i.val] = v
    data.append(row)
  np_data = np.array(data)
#  print(np_data)
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
    line_annotations[key].append((k[4], k[5], v[0], v[1][0][2]))
  with open("annotations_"+log_file, "w") as out:
    print("Saving annotations ...\n")
    for line, annot in line_annotations.items():
      s = [(get_name(t, n), tuple([f"{solution[d.val]}" for d in a]), c) for t, n, a, c in annot]
      out.write(f"{line[0]}@{line[1]}:\n")
      for name, shape, concrete in s:
        out.write(f"    {name}: {shape} {concrete}\n")


def annotate_shape(obj, shape):
  object_name_space[last_oid] = shape

