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

import dataclasses
from datetime import datetime
import io
import itertools
from typing import Any

import pandas as pd

from pynsy.analyses import util
from pynsy.instrumentation import logging_utils
from pynsy.instrumentation import util as instrumentation_util

ObjectId = instrumentation_util.ObjectId

log = logging_utils.logger(__name__)
styled = logging_utils.styled

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

  def to_string(self, indent: int = 0, *, color: bool = True) -> str:
    out = io.StringIO()
    out.write(" " * indent)
    name = get_name(self.opcode, self.name)
    msg = f"# {name}: {self.symbolic_shape} {self.concrete_shape}"
    out.write(msg)
    s = out.getvalue()
    if color:
      s = styled(s, style="bold magenta")
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
    "RETURN_FUNCTION": "<call>",
    "RETURN_FUNCTION_KW": "<call>",
    "RETURN_METHOD": "<call>",
}


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


class FreshVariableId:

  def __init__(self):
    self.id_to_value = list()

  def get_fresh_id(self, value):
    self.id_to_value.append(value)
    return len(self.id_to_value) - 1

  def get_value(self, id):
    return self.id_to_value[id]

  def num_ids(self):
    return len(self.id_to_value)



def find_solution(states, location_id_to_type_and_values, n_symbols):
  solution = [
      TemplateInstance(identity_template, [i]) for i in range(n_symbols)
  ]
  for location_id, state_list in states.items():
    exclude = location_id_to_type_and_values[location_id].get_type()
    for template in templates:
      for var in exclude:
        vars_list = [
            i
            for i in range(n_symbols)
            if i != var and solution[i].get_name() == "identity"
        ]
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


def get_name_from_name_space(i, name_space):
  if i in name_space:
    return name_space[i]
  else:
    return f"d{i}"


def get_equivalence_classes(solution):
  equivalence_classes = [{i} for i in range(len(solution))]
  for i, v in enumerate(solution):
    if v.get_name() == "=":
      lhs = i
      rhs = v.vars[0]
      lhs_index = None
      rhs_index = None
      for j, s in enumerate(equivalence_classes):
        if s is not None and lhs in s:
          lhs_index = j
        if s is not None and rhs in s:
          rhs_index = j
      if lhs_index != rhs_index:
        lhs_index, rhs_index = min(lhs_index, rhs_index), max(
            lhs_index, rhs_index
        )
        equivalence_classes[lhs_index].update(equivalence_classes[rhs_index])
        equivalence_classes[rhs_index] = None
  return equivalence_classes


def get_var_to_name(equivalence_classes, name_space):
  var_to_name = dict()
  for i, s in enumerate(equivalence_classes):
    done = False
    if s is not None:
      for n in name_space:
        if n in s:
          done = True
          for e in s:
            var_to_name[e] = name_space[n]
          break
      if not done:
        min_e = min(s)
        for e in s:
          var_to_name[e] = f"d{min_e}"
  return var_to_name


def replace_id_with_names(solution, name_space):
  equivalence_classes = get_equivalence_classes(solution)
  var_to_name = get_var_to_name(equivalence_classes, name_space)
  for i, v in enumerate(solution):
    v.vars = [var_to_name[i] for i in v.vars]


def get_name(opcode, name):
  if isinstance(name, str) and name:
    return name
  else:
    return nicknames.get(opcode, f"<{opcode}>")


def count_leading_spaces(s: str) -> int:
  return len(s) - len(s.lstrip(" "))


class TypeConstructor:

  def __init__(self, name):
    self.name = name
    self.symbolic_id = None
    self.children = []

  def add_children(self, children):
    self.children.extend(children)

  def __repr__(self):
    if len(self.children) == 0:
      return f"T:{self.name}"
    else:
      return f"T:{self.name}[{', '.join([repr(c) for c in self.children])}]"

  def __eq__(self, other):
    if self.name != other.name:
      return False
    if len(self.children) != len(other.children):
      return False
    for c1, c2 in zip(self.children, other.children):
      if c1 != c2:
        return False
    return True

  def find_common_subtree(self, other):
    if self.name == "Any":
      return self
    elif self.name == other.name:
      if len(self.children) == len(other.children):
        if len(self.children) == 0:
          return self
        else:
          ret = TypeConstructor(self.name)
          for c1, c2 in zip(self.children, other.children):
            ret.add_children([c1.find_common_subtree(c2)])
          return ret
      else:
        return TypeConstructor("Any")
    else:
      return TypeConstructor("Any")

  def assign_symbolic_vars(self, symbolic_type, location_id, fresh_variable_generator):
    if self.name == "Any":
      self.symbolic_id = fresh_variable_generator.get_fresh_id(location_id)
      symbolic_type.append(self.symbolic_id)
      return
    else:
      for c1 in self.children:
        c1.assign_symbolic_vars(symbolic_type, location_id, fresh_variable_generator)

  def extract_values_for_Any(self, type_value):
    if self.name == "Any":
      return [type_value]
    else:
      ret = []
      for c1 in self.children:
        ret.extend(self.extract_values_for_Any(c1))
      return ret

def assign_symbolic_types(type_and_values, location_id):
  fresh_variable_generator = FreshVariableId()
  values = type_and_values.get_values()
  common_subtree = None
  if len(values) > 1:
    common_subtree = values[0].findd_common_subtree(values[1])
  for value in values[2:]:
    common_subtree = common_subtree.find_common_subtree(value)
  if common_subtree is not None:
    symbolic_type = []
    common_subtree.assign_symbolic_vars(symbolic_type, location_id, fresh_variable_generator)
    type_and_values.set_type(symbolic_type)
    type_and_values.set_common(common_subtree)
    type_values = type_and_values.get_values()
    for i, type_value in enumerate(type_values):
      type_values[i] = common_subtree.extract_values_for_Any(type_value)


def abstraction(obj):
  if isinstance(obj, list):
    ignore = False
  elif isinstance(obj, tuple):
    ignore = False
  elif isinstance(obj, dict):
    ignore = False
  elif isinstance(obj, set):
    ignore = False
  elif isinstance(obj, int):
    ignore = True
  elif isinstance(obj, float):
    ignore = True
  elif isinstance(obj, str):
    ignore = True
  elif isinstance(obj, bool):
    ignore = True
  elif isinstance(obj, bytes):
    ignore = True
  elif isinstance(obj, type(None)):
    ignore = True
  else:
    ignore = False
  return ignore, get_type(obj)




def get_type(obj):
  if isinstance(obj, list):
    ret = TypeConstructor("list")
    ret.add_children([get_type(o) for o in obj])
  elif isinstance(obj, tuple):
    ret = TypeConstructor("tuple")
    ret.add_children([get_type(o) for o in obj])
  elif isinstance(obj, dict):
    ret = TypeConstructor("dict")
    ret.add_children(
        [[get_type(o) for o in obj.keys()], [get_type(o) for o in obj.values()]]
    )
  elif isinstance(obj, set):
    ret = TypeConstructor("set")
    ret.add_children([get_type(o) for o in obj])
  elif isinstance(obj, int):
    ret = TypeConstructor("int")
  elif isinstance(obj, float):
    ret = TypeConstructor("float")
  elif isinstance(obj, str):
    ret = TypeConstructor("str")
  elif isinstance(obj, bool):
    ret = TypeConstructor("bool")
  elif isinstance(obj, bytes):
    ret = TypeConstructor("bytes")
  elif isinstance(obj, type(None)):
    ret = TypeConstructor("none")
  else:
    ret = TypeConstructor(str(type(obj)).split("'")[1])
  return ret


def get_location_ids_in_method(method_id, method_id_to_location_ids):
  if method_id not in method_id_to_location_ids:
    method_id_to_location_ids[method_id] = set()
  return method_id_to_location_ids[method_id]


def get_symbolic_type(value, vars, location_id):
  abs = value["abs"]
  symbolic_shape_type = []
  for _ in abs:
    symbolic_shape_type.append(vars.get_fresh_id(location_id))
  return symbolic_shape_type


def get_state_update(symbolic_type, value):
  state_update = dict(zip(symbolic_type, value["abs"]))
  return state_update


class TypeAndValues:

  def __init__(self):
    self.type = None
    self.common = None
    self.values = []

  def add_value(self, value):
    self.values.append(value)

  def set_common(self, common):
    self.common = common

  def get_common(self):
    return self.common

  def get_type(self):
    return self.type

  def set_type(self, type):
    self.type = type

  def get_values(self):
    return self.values

  def get_last_value(self):
    return self.values[-1]

  def __repr__(self):
    return f"(type : {self.type}, values: {self.values})"


def create_states(record_list):
  states = dict()
  location_id_to_type_and_values = dict()
  state_stack = []
  method_id_to_location_ids = dict()
  state = dict()
  location_to_id = UniqueIdForKey()

  rlen = len(record_list)
  for i in range(rlen):
    row = record_list[i]
    name = ""
    if "name" in row:
      name = row["name"]
    elif "function_name" in row:
      name = str(row["function_name"]) + "()"
    name = get_name(row["type"], name)

    if row["type"].startswith("RETURN_") and not record_list[i - 1][
        "type"
    ].startswith("CALL_"):
      state = state_stack.pop()
    if not row["type"].startswith("RETURN_") and record_list[i - 1][
        "type"
    ].startswith("CALL_"):
      method_id = row["method_id"]
      state_stack.append(state)
      location_ids_in_method = get_location_ids_in_method(
          method_id, method_id_to_location_ids
      )
      state = {
          key: state[key] for key in state if key not in location_ids_in_method
      }
    value = row["result_and_args"][0]
    if isinstance(value["abs"], TypeConstructor):
      location = tuple([name] + [row[x] for x in keys])
      location_id = location_to_id.get_id(location)
      if location_id not in location_id_to_type_and_values:
        type_and_values = TypeAndValues()
        type_and_values.add_value(value)
        location_id_to_type_and_values[location_id] = type_and_values
      else:
        location_id_to_type_and_values[location_id].add_value(value)
      method_id = row["method_id"]
      location_ids_in_method = get_location_ids_in_method(
          method_id, method_id_to_location_ids
      )
      location_ids_in_method.add(location_id)

      value = location_id_to_type_and_values[location_id].get_last_value()
      state[location_id] = value
      if location_id not in states:
        states[location_id] = list()
      states[location_id].append(dict(state))
  return (
      states,
      location_id_to_type_and_values,
      location_to_id,
      method_id_to_location_ids,
  )


def process_event(record):
  record_list.append(record)


def process_termination():
  verbose = True
  if not record_list:
    log("No instructions were instrumented.")
    return

  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("shape_inference", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)

  states, location_id_to_type_and_values, location_to_id, method_id_to_types = (
      create_states(record_list)
  )
  for location_id, state in states.items():
    print(f"{location_id}{location_to_id.get_key(location_id)}: {state}")

  # n_symbols = fresh_vars.num_ids()
  # for k, v in location_id_to_type_and_values.items():
  #   print(f"{k}{location_to_id.get_key(k)} : {v}")
  # solution = find_solution(states, location_id_to_type_and_values, n_symbols)
  # print(name_space)
  # replace_id_with_names(solution, name_space)
  #
  # # for i, v in enumerate(solution):
  # #   print(f"{i} : {v}")
  # #
  # for location_id, type_and_values in location_id_to_type_and_values.items():
  #   symbolic_type = type_and_values.get_type()
  #   if all(map(lambda x: solution[x].get_name() != "identity", symbolic_type)):
  #     print(f"{location_id}{location_to_id.get_key(location_id)} : {[solution[x] for x in type_and_values.get_type()]}")


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
#         "shape_inference", f"annotations/{module_name}.py"
#     )
#     log(f"Saving annotated source file: {annotations_file}.")
#     with open(annotations_file, "w") as out:
#       out.write("# Auto-generated file with array shape annotations.\n")
#       out.write(f"# Original file: {module_path}\n\n")
#       out.write(annotated_source)
#
#   annotations_file = util.get_output_path("shape_inference", "annotations.txt")
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


observed_hyper_parameters = set()


def annotate_shape(shape_or_int, dim_names):
  for i in range(len(record_list) - 1, -1, -1):
    if record_list[i]["type"].startswith("CALL_"):
      record = dict(record_list[i])
      record["type"] = "LOAD_NAME"
      record["special"] = (
          (dim_names,) if isinstance(dim_names, str) else dim_names
      )
      record["result_and_args"] = [{
          "id": 0,
          "abs": (
              (shape_or_int,)
              if isinstance(shape_or_int, int)
              else shape_or_int.shape
          ),
      }]
      record_list.append(record)
      break


def hyper_parameter(dim_int, dim_name):
  while dim_int in observed_hyper_parameters:
    dim_int += 1
  observed_hyper_parameters.add(dim_int)
  annotate_shape(dim_int, dim_name)
  return dim_int
