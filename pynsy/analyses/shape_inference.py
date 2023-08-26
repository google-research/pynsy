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
import dataclasses
from datetime import datetime
import io
import itertools
from typing import Any

import pandas as pd
from rich.text import Text

from pynsy.analyses import util
from pynsy.instrumentation import logging_utils
from pynsy.instrumentation import module_loader

log = logging_utils.logger(__name__)
print_panel = logging_utils.print_panel
styled = logging_utils.styled

record_list = []

now = datetime.now()
timestamp = int(round(now.timestamp()))


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
    name = CommonUtils.get_nickname(self.opcode, self.name)
    concrete_shape_str = " ".join(str(x) for x in self.concrete_shape)
    msg = f"# ↳ {name}: {self.symbolic_shape} · {concrete_shape_str}"
    out.write(msg)
    s = out.getvalue()
    if color:
      s = styled(s, style="bold magenta")
    return s




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


class FreshVarId:

  def __init__(self):
    self.var_id_to_value = list()
    self.var_id_annotation = None

  def get_fresh_id(self, value):
    self.var_id_to_value.append(value)
    return len(self.var_id_to_value) - 1

  def get_value(self, id):
    return self.var_id_to_value[id]

  def num_ids(self):
    return len(self.var_id_to_value)

  def set_annotations(self, equivalence_classes, name_space, formatter):
    var_id_to_name = [None] * self.num_ids()
    for i, s in enumerate(equivalence_classes):
      done = False
      if s is not None:
        for n in name_space:
          if n in s:
            done = True
            for e in s:
              var_id_to_name[e] = name_space[n]
            break
        if not done:
          min_e = min(s)
          for e in s:
            var_id_to_name[e] = formatter(min_e)
    self.var_id_to_name = var_id_to_name

  def get_annotation(self, id):
    return self.var_id_to_name[id]




class TemplateInstance:

  def __init__(self, template, vars):
    self.template = template
    self.vars = vars

  def get_name(self):
    return self.template.get_name()

  def get_template(self):
    return self.template

  def __repr__(self):
    return f"{self.template.repr(self.vars)}"


class Template:

  def __init__(self, name, n_vars, predicate, repr):
    self.name = name
    self.n_vars = n_vars
    self.predicate = predicate
    self.repr = repr

  def get_name(self):
    return self.name

  def get_instance(self, vars):
    return TemplateInstance(self, vars)


class CommonUtils:
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

  @classmethod
  def get_equivalence_classes(cls, solution):
    equivalence_classes = [{i} for i in range(len(solution))]
    for i, template_instance in enumerate(solution):
      if template_instance.get_name() == "=":
        lhs = i
        rhs = template_instance.vars[0]
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

  @classmethod
  def get_nickname(cls, opcode, name):
    if isinstance(name, str) and name:
      return name
    else:
      return cls.nicknames.get(opcode, f"<{opcode}>")

  @classmethod
  def count_leading_spaces(cls, s: str) -> int:
    return len(s) - len(s.lstrip(" "))



class TensorShapeInferenceUtils:
  def __init__(self):
    self.templates = [
        Template(
            "=",
            2,
            lambda state, vars: state.get(vars[0], 0) == state.get(vars[1], 0),
            lambda vars: vars[0],
        ),
        Template(
            "*",
            3,
            lambda state, vars: False
            if state.get(vars[1], 0) == 1 or state.get(vars[2], 0) == 1
            else state.get(vars[0], 0)
                 == state.get(vars[1], 0) * state.get(vars[2], 0),
            lambda vars: f"{vars[0]}*{vars[1]}",
        ),
    ]


  def is_type_value(self, value):
    return self.is_shape(value["abs"])

  def is_shape(self, s):
    return isinstance(s, list) or isinstance(s, tuple)

  def get_var_ids(self, abs, vars, location_id):
    var_ids = []
    for _ in abs:
      var_ids.append(vars.get_fresh_id(location_id))
    return var_ids

  def get_state_update(self, vars_and_values, value):
    var_ids = vars_and_values.var_ids
    state_update = dict(zip(var_ids, value["abs"]))
    return state_update

  def set_annotation(self, row, var_ids, var_id_to_annotation):
    if "special" in row:
      names = row["special"]
      for var_id, name in zip(var_ids, names):
        var_id_to_annotation[var_id] = name

  def set_var_ids(self, location_id_to_vars_and_values, fresh_var_generator, global_state):
    for location_id, vars_and_values in location_id_to_vars_and_values.items():
      value = next(iter(vars_and_values.abstraction_set))
      vars_and_values.var_ids = self.get_var_ids(value, fresh_var_generator, location_id)
      if len(vars_and_values.abstraction_set) == 1:
        global_state.update(zip(vars_and_values.var_ids, value))

  def print_solution(self, location_id_to_var_ids_and_values, location_to_id, fresh_var_generator, solution, identity_template):
    for location_id, vars_and_values in location_id_to_var_ids_and_values.items():
      if all(solution[x].get_template() != identity_template for x in vars_and_values.var_ids):
        print(
            f"{location_id}{location_to_id.get_key(location_id)} :"
            f" {[fresh_var_generator.get_annotation(x) for x in vars_and_values.var_ids]}"
        )



def abstraction(obj):
  if hasattr(obj, "shape"):
    try:
      return True, obj.shape
    except:
      return True, None
  return True, None


@dataclasses.dataclass
class VarIdsAndValues:
  values: list[Any]

  def __init__(self):
    self.var_ids = None
    self.values = []
    self.abstraction_set = set()

  def add_to_abstraction_set(self, value):
    self.abstraction_set.add(value)

  def add_value(self, value):
    self.values.append(value)

  def get_last_value(self):
    return self.values[-1]


class TypeInference:

  def __init__(self, type_utils):
    self.keys = ["module_name", "method_id", "instruction_id", "lineno", "type"]
    self.location_id_to_state_list = dict()
    self.location_id_to_var_ids_and_values = dict()
    self.location_to_id = UniqueIdForKey()
    self.var_id_to_annotation = dict()
    self.location_id_to_name = dict()
    self.fresh_var_generator = FreshVarId()
    self.global_state = dict()
    self.method_id_to_var_ids = dict()
    self.identity_template = Template(
        "identity", 1, lambda state, vars: True, lambda vars: vars[0]
    )
    self.type_utils: TensorShapeInferenceUtils = type_utils

  def get_data(self):
    return (
        self.location_id_to_state_list,
        self.global_state,
        self.location_id_to_var_ids_and_values,
        self.location_to_id,
        self.fresh_var_generator,
        self.var_id_to_annotation,
        self.location_id_to_name,
        self.method_id_to_var_ids,
    )

  def get_var_ids_in_method(self, method_id):
    if method_id not in self.method_id_to_var_ids:
      self.method_id_to_var_ids[method_id] = set()
    return self.method_id_to_var_ids[method_id]


  def create_var_ids_and_global_state(self, record_list):
    rlen = len(record_list)
    for i in range(rlen):
      row = record_list[i]
      value = row["result_and_args"][0]
      if self.type_utils.is_type_value(value):
        location = tuple([row[x] for x in self.keys])
        location_id = self.location_to_id.get_id(location)
        if location_id not in self.location_id_to_var_ids_and_values:
          vars_and_values = VarIdsAndValues()
          vars_and_values.add_to_abstraction_set(value["abs"])
          self.location_id_to_var_ids_and_values[location_id] = vars_and_values
        else:
          self.location_id_to_var_ids_and_values[location_id].add_to_abstraction_set(value["abs"])
    self.type_utils.set_var_ids(self.location_id_to_var_ids_and_values, self.fresh_var_generator, self.global_state)


  def create_states(self, record_list):
    state_stack = []
    state = dict()

    rlen = len(record_list)
    for i in range(rlen):
      row = record_list[i]
      name = ""
      if "name" in row:
        name = row["name"]
      elif "function_name" in row:
        name = str(row["function_name"]) + "()"
      name = CommonUtils.get_nickname(row["type"], name)

      if row["type"].startswith("RETURN_") and not record_list[i - 1][
          "type"
      ].startswith("CALL_"):
        state = state_stack.pop()
      if not row["type"].startswith("RETURN_") and record_list[i - 1][
          "type"
      ].startswith("CALL_"):
        method_id = row["method_id"]
        state_stack.append(state)
        var_ids_in_method = self.get_var_ids_in_method(method_id)
        state = {key: state[key] for key in state if key not in var_ids_in_method}
      value = row["result_and_args"][0]
      if self.type_utils.is_type_value(value):
        location = tuple([row[x] for x in self.keys])
        location_id = self.location_to_id.get_id(location)
        self.location_id_to_name[location_id] = name
        var_ids = self.location_id_to_var_ids_and_values[location_id].var_ids
        self.location_id_to_var_ids_and_values[location_id].add_value(value)

        method_id = row["method_id"]
        var_ids_in_method = self.get_var_ids_in_method(method_id)
        var_ids_in_method.update(var_ids)

        self.type_utils.set_annotation(row, var_ids, self.var_id_to_annotation)

        value = self.location_id_to_var_ids_and_values[location_id].get_last_value()
        state_update = self.type_utils.get_state_update(self.location_id_to_var_ids_and_values[location_id], value)
        state.update(state_update)
        if location_id not in self.location_id_to_state_list:
          self.location_id_to_state_list[location_id] = list()
        self.location_id_to_state_list[location_id].append(dict(state))

  def find_solution(self):
    n_symbols = self.fresh_var_generator.num_ids()
    solution = [
        TemplateInstance(self.identity_template, [i]) for i in range(n_symbols)
    ]
    for location_id, state_list in self.location_id_to_state_list.items():
      exclude = self.location_id_to_var_ids_and_values[location_id].var_ids
      for template in self.type_utils.templates:
        for var in exclude:
          vars_list = [
              i
              for i in range(n_symbols)
              if i != var and solution[i].get_template() == self.identity_template
          ]
          vars_iter = itertools.combinations(vars_list, template.n_vars - 1)
          for vars in vars_iter:
            vars = [var] + list(vars)
            holds = True
            for state in state_list:
              if not template.predicate(state|self.global_state, vars):
                holds = False
                break
            if holds:
              solution[var] = template.get_instance(vars[1:])
              break
    return solution




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

  type_utils = TensorShapeInferenceUtils()
  type_inference = TypeInference(type_utils)
  type_inference.create_var_ids_and_global_state(record_list)
  type_inference.create_states(record_list)

  (
      location_id_to_state_list,
      global_state,
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
      var_id_to_annotation,
      location_id_to_name,
      method_id_to_var_ids,
  ) = type_inference.get_data()

  for k, v in location_id_to_var_ids_and_values.items():
    print(f"{k}{location_to_id.get_key(k)} : {v}")
  solution = type_inference.find_solution()
  print(var_id_to_annotation)
  equivalence_classes = CommonUtils.get_equivalence_classes(solution)
  fresh_var_generator.set_annotations(equivalence_classes, var_id_to_annotation, lambda x: f"d{x}")
  type_utils.print_solution(location_id_to_var_ids_and_values, location_to_id, fresh_var_generator, solution, type_inference.identity_template)

  annotations_by_line_by_module: dict[str, dict[int, list]] = (
      collections.defaultdict(lambda: collections.defaultdict(list))
  )
  for location_id, vars_and_values in location_id_to_var_ids_and_values.items():
    module_name, method_id, instruction_id, line_number, opcode = (
        location_to_id.get_key(location_id)
    )
    name = location_id_to_name[location_id]
    del method_id, instruction_id
    line_number = int(line_number)

    symbolic_shape = [fresh_var_generator.get_annotation(x) for x in vars_and_values.var_ids]
    concrete_shapes = vars_and_values.values

    annotation = Annotation(
        opcode=opcode,
        name=name,
        symbolic_shape=symbolic_shape,
        concrete_shape=[
            concrete_shape["abs"] for concrete_shape in concrete_shapes
        ],
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
      indent = CommonUtils.count_leading_spaces(annotated_line)
      annotations = annotations_by_line[line_number]
      for annotation in annotations:
        s = annotation.to_string(indent=indent, color=True)
        annotated_lines.append(s)

    end_index = transform_line_number(last_line_number)
    annotated_lines.extend(module_lines[end_index:])
    annotated_source = "\n".join(annotated_lines)
    if verbose:
      annotated_text = Text(annotated_source)
      annotated_text.highlight_regex(r"\s*# ↳.+", style="bold magenta")
      print_panel(annotated_text, title=f"Shape annotations: [b]{module_name}")

    annotations_file = util.get_output_path(
        "shape_inference", f"annotations/{module_name}.py"
    )
    log(f"Saving annotated source file: {annotations_file}.")
    with open(annotations_file, "w") as out:
      out.write("# Auto-generated file with array shape annotations.\n")
      out.write(f"# Original file: {module_path}\n\n")
      out.write(annotated_source)

  annotations_file = util.get_output_path("shape_inference", "annotations.txt")
  with open(annotations_file, "w") as out:
    log(f"Saving annotations to {annotations_file}.")
    for (
        module_name,
        annotations_by_line,
    ) in annotations_by_line_by_module.items():
      for line_number, annotations in annotations_by_line.items():
        s = []
        for annotation in annotations:
          name = CommonUtils.get_nickname(annotation.opcode, annotation.name)
          shape = tuple(annotation.symbolic_shape)
          concrete = annotation.concrete_shape
          s.append((name, shape, concrete))
        out.write(f"{module_name}@{line_number}:\n")
        for name, shape, concrete in s:
          out.write(f"    {name}: {shape} {concrete}\n")


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
