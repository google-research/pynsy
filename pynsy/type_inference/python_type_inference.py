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
from typing import Any
from abc import ABC, abstractmethod

import pandas as pd
from rich.text import Text

from pynsy.analyses import util
from pynsy.instrumentation import logging_utils
from pynsy.instrumentation import module_loader
from pynsy.type_inference.inference_engine import AbstractState, Template, CommonUtils


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

  def to_string(self, indent: int = 0, *, show_concrete_shape: bool = True, color: bool = True) -> str:
    out = io.StringIO()
    out.write(" " * indent)
    name = CommonUtils.get_nickname(self.opcode, self.name)
    out.write(f"# ↳ {name}: {self.symbolic_shape}")
    if show_concrete_shape:
      out.write(" · ")
      concrete_shape_str = " ".join(str(x) for x in self.concrete_shape)
      out.write(concrete_shape_str)
    s = out.getvalue()
    if color:
      s = styled(s, style="bold magenta")
    return s


class PythonTypeInferenceUtils:
  templates = [
      Template(
          "=",
          2,
          lambda state, vars: state.get(vars[0], None)
          == state.get(vars[1], None),
          lambda vars: vars[0],
      )
  ]

  @classmethod
  def to_consider(cls, value):
    return isinstance(value["abs"], PType)

  @classmethod
  def get_state_update(cls, vars_and_values, value):
    var_ids = vars_and_values.var_ids
    common_type_value = vars_and_values.common_type_value
    type_values = common_type_value.extract_values_for_var_ids(value["abs"])
    state_update = dict(zip(var_ids, type_values))
    return state_update

  @classmethod
  def set_annotation(cls, row, var_ids, var_id_to_annotation):
    pass

  @classmethod
  def create_var_ids_and_global_state(
      cls, location_id_to_vars_and_values, fresh_var_generator, global_state
  ):
    for location_id, vars_and_values in location_id_to_vars_and_values.items():
      abstraction_set_iter = iter(vars_and_values.abstraction_set)
      common_type_value = next(iter(vars_and_values.abstraction_set))
      for type_value in abstraction_set_iter:
        common_type_value = common_type_value.find_common_subtree(type_value)
      var_ids = []
      common_type_value.assign_var_ids(
          var_ids, location_id, fresh_var_generator
      )
      vars_and_values.var_ids = var_ids
      vars_and_values.common_type_value = common_type_value

  @classmethod
  def print_solution(
      cls,
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
  ):
    for (
        location_id,
        vars_and_values,
    ) in location_id_to_var_ids_and_values.items():
      print(
          f"{location_id}{location_to_id.get_key(location_id)} :"
          f" {vars_and_values.common_type_value.get_repr(fresh_var_generator)}"
          .replace("Union[NoneType, ", "Optional[")
      )


class PType(ABC):

  def __init__(self, name):
    self.name = name
    self.repr = None

  def __hash__(self):
    return hash(repr(self))

  def __eq__(self, other):
    if not isinstance(other, PType):
      return False
    if repr(self) == repr(other):
      return True
    else:
      return False

  def __repr__(self):
    if self.repr is None:
      self.repr = self.get_repr(None)
    return self.repr

  @abstractmethod
  def get_repr(self, fresh_var_generator):
    pass

  @abstractmethod
  def find_common_subtree(self, other):
    return

  @abstractmethod
  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    return

  @abstractmethod
  def extract_values_for_var_ids(self, type_value):
    return


class PTypeVar(PType):

  @classmethod
  def get_ptype(cls):
    return PTypeVar()

  def __init__(self):
    super().__init__("TypeVar")
    self.var_id = -1

  def set_var_id(self, var_id):
    self.var_id = var_id

  def find_common_subtree(self, other):
    return self

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    self.var_id = fresh_var_generator.get_fresh_id(location_id)
    var_ids.append(self.var_id)

  def extract_values_for_var_ids(self, type_value):
    return [type_value]

  def get_repr(self, fresh_var_generator):
    if fresh_var_generator is None:
      ret = f"{self.name}({self.var_id})"
    else:
      ret = f"{fresh_var_generator.get_annotation(self.var_id)}"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PTupleType(PType):

  @classmethod
  def get_ptype(cls, element_types):
    return PTupleType(element_types)

  def __init__(self, element_types):
    super().__init__("tuple")
    self.element_types = element_types

  def find_common_subtree(self, other):
    if self == other:
      return self
    elif not isinstance(other, PTupleType):
      return PTypeVar()
    elif len(self.element_types) != len(other.element_types):
      return PTypeVar()
    else:
      return PTupleType.get_ptype(
          [
              c1.find_common_subtree(c2)
              for c1, c2 in zip(self.element_types, other.element_types)
          ]
      )

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    for c1 in self.element_types:
      c1.assign_var_ids(var_ids, location_id, fresh_var_generator)

  def extract_values_for_var_ids(self, type_value):
    ret = []
    for c1 in self.element_types:
      ret.extend(c1.extract_values_for_var_ids(type_value))
    return ret

  def get_repr(self, fresh_var_generator):
    element_types_repr = [
        c.get_repr(fresh_var_generator) for c in self.element_types
    ]
    if len(element_types_repr) == 0:
      repr = PNominalType.get_ptype("Any").get_repr(fresh_var_generator)
      ret = f"{self.name}[{repr}]"
    elif len(set(element_types_repr)) == 1:
      ret = f"{self.name}[{element_types_repr[0]},...]"
    else:
      ret = f"{self.name}[{', '.join(element_types_repr)}]"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PListType(PType):

  @classmethod
  def get_ptype(cls, element_type):
    return PListType(element_type)

  def __init__(self, element_type):
    super().__init__("list")
    self.element_type = element_type

  def find_common_subtree(self, other):
    if self == other:
      return self
    elif not isinstance(other, PListType):
      return PTypeVar()
    else:
      return PListType.get_ptype(
          self.element_type.find_common_subtree(other.element_type)
      )

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    self.element_type.assign_var_ids(var_ids, location_id, fresh_var_generator)

  def extract_values_for_var_ids(self, type_value):
    return self.element_type.extract_values_for_var_ids(type_value)

  def get_repr(self, fresh_var_generator):
    ret = f"{self.name}[{self.element_type.get_repr(fresh_var_generator)}]"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PSetType(PType):

  @classmethod
  def get_ptype(cls, element_type):
    return PSetType(element_type)

  def __init__(self, element_type):
    super().__init__("set")
    self.element_type = element_type

  def find_common_subtree(self, other):
    if self == other:
      return self
    elif not isinstance(other, PSetType):
      return PTypeVar()
    else:
      return PSetType.get_ptype(
          self.element_type.find_common_subtree(other.element_type)
      )

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    self.element_type.assign_var_ids(var_ids, location_id, fresh_var_generator)

  def extract_values_for_var_ids(self, type_value):
    return self.element_type.extract_values_for_var_ids(type_value)

  def get_repr(self, fresh_var_generator):
    ret = f"{self.name}[{self.element_type.get_repr(fresh_var_generator)}]"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PDictType(PType):

  @classmethod
  def get_ptype(cls, key_type, value_type):
    return PDictType(key_type, value_type)

  def __init__(self, key_type, value_type):
    super().__init__("dict")
    self.key_type = key_type
    self.value_type = value_type

  def find_common_subtree(self, other):
    if self == other:
      return self
    elif not isinstance(other, PDictType):
      return PTypeVar()
    else:
      return PDictType.get_ptype(
          self.key_type.find_common_subtree(other.key_type),
          self.value_type.find_common_subtree(other.value_type),
      )

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    self.key_type.assign_var_ids(var_ids, location_id, fresh_var_generator)
    self.value_type.assign_var_ids(var_ids, location_id, fresh_var_generator)

  def extract_values_for_var_ids(self, type_value):
    return self.key_type.extract_values_for_var_ids(
        type_value
    ) + self.value_type.extract_values_for_var_ids(type_value)

  def get_repr(self, fresh_var_generator):
    key_repr = self.key_type.get_repr(fresh_var_generator)
    value_repr = self.value_type.get_repr(fresh_var_generator)
    ret = f"{self.name}[{key_repr}, {value_repr}]"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PNominalType(PType):
  name_to_ptype = {}

  @classmethod
  def get_ptype(cls, name):
    if name in cls.name_to_ptype:
      return cls.name_to_ptype[name]
    else:
      ret = PNominalType(name)
      cls.name_to_ptype[name] = ret
      return ret

  def extract_values_for_var_ids(self, type_value):
    return []

  def __init__(self, name):
    super().__init__(name)

  def find_common_subtree(self, other):
    if self == PNominalType.get_ptype("Any") or other == PNominalType.get_ptype(
        "Any"
    ):
      return PNominalType.get_ptype("Any")
    elif self == other:
      return self
    else:
      return PTypeVar.get_ptype()

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    pass

  def get_repr(self, fresh_var_generator):
    ret = f"{self.name}"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


class PUnionType(PType):
  max_children = 2

  @classmethod
  def get_ptype(cls, possible_types):
    possible_types_set = set(possible_types)
    if len(possible_types_set) == 0:
      return PNominalType.get_ptype("Any")
    elif len(possible_types_set) == 1:
      return possible_types[0]
    elif len(possible_types_set) <= cls.max_children:
      tmp = sorted(
          [(c, repr(c)) for c in possible_types_set], key=lambda x: x[1]
      )
      return PUnionType([e[0] for e in tmp])
    else:
      return PNominalType.get_ptype("Any")

  def __init__(self, possible_types):
    super().__init__("Union")
    self.possible_types = possible_types

  def find_common_subtree(self, other):
    if self == other:
      return self
    elif not isinstance(other, PUnionType):
      return PTypeVar()
    elif len(self.possible_types) != len(other.possible_types):
      return PTypeVar()
    else:
      return PUnionType.get_ptype(
          [
              c1.find_common_subtree(c2)
              for c1, c2 in zip(self.possible_types, other.possible_types)
          ]
      )

  def assign_var_ids(self, var_ids, location_id, fresh_var_generator):
    for c in self.possible_types:
      c.assign_var_ids(var_ids, location_id, fresh_var_generator)

  def extract_values_for_var_ids(self, type_value):
    return [
        c
        for l in self.possible_types
        for c in l.extract_values_for_var_ids(type_value)
    ]

  def get_repr(self, fresh_var_generator):
    possible_types_repr = [
        c.get_repr(fresh_var_generator) for c in self.possible_types
    ]
    ret = f"{self.name}[{', '.join(possible_types_repr)}]"
    if fresh_var_generator is None and self.repr is None:
      self.repr = ret
    return ret


def abstraction(obj):
  # if isinstance(obj, list):
  #   ignore = False
  # elif isinstance(obj, tuple):
  #   ignore = False
  # elif isinstance(obj, dict):
  #   ignore = False
  # elif isinstance(obj, set):
  #   ignore = False
  # elif isinstance(obj, int):
  #   ignore = True
  # elif isinstance(obj, float):
  #   ignore = True
  # elif isinstance(obj, str):
  #   ignore = True
  # elif isinstance(obj, bool):
  #   ignore = True
  # elif isinstance(obj, bytes):
  #   ignore = True
  # elif isinstance(obj, type(None)):
  #   ignore = True
  # else:
  #   ignore = False
  return True, get_type(obj)


def get_type(obj):
  if isinstance(obj, bool):
    ret = PNominalType.get_ptype("bool")
  elif isinstance(obj, int):
    ret = PNominalType.get_ptype("int")
  elif isinstance(obj, float):
    ret = PNominalType.get_ptype("float")
  elif isinstance(obj, bytes):
    ret = PNominalType.get_ptype("bytes")
  elif isinstance(obj, str):
    ret = PNominalType.get_ptype("str")
  elif isinstance(obj, type(None)):
    ret = PNominalType.get_ptype("NoneType")
  elif isinstance(obj, tuple):
    ret = PTupleType.get_ptype([get_type(o) for o in obj])
  elif isinstance(obj, set):
    child = PUnionType.get_ptype([get_type(o) for o in obj])
    ret = PSetType.get_ptype(child)
  elif isinstance(obj, list):
    child = PUnionType.get_ptype([get_type(o) for o in obj])
    ret = PListType.get_ptype(child)
  elif isinstance(obj, dict):
    key_type = PUnionType.get_ptype([get_type(k) for k in obj.keys()])
    value_type = PUnionType.get_ptype([get_type(v) for v in obj.values()])
    ret = PDictType.get_ptype(key_type, value_type)
  else:
    ret = PNominalType.get_ptype(type(obj).__name__)
  return ret


def process_event(record):
  record_list.append(record)


def process_termination():
  verbose = True
  if not record_list:
    log("No instructions were instrumented.")
    return

  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("python_type_inference", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)

  abstract_states = AbstractState(PythonTypeInferenceUtils)
  abstract_states.create_var_ids_and_global_state(record_list)
  abstract_states.create_local_states(record_list)

  (
      location_id_to_state_list,
      global_state,
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
      var_id_to_annotation,
      location_id_to_name,
      location_id_to_record_list_index,
  ) = abstract_states.get_data()

  for k, v in location_id_to_var_ids_and_values.items():
    print(f"{k}{location_to_id.get_key(k)} : {v}")
  solution = CommonUtils.find_solution(
      fresh_var_generator.num_ids(),
      PythonTypeInferenceUtils.templates,
      global_state,
      location_id_to_state_list,
      location_id_to_var_ids_and_values,
  )
  equivalence_classes = CommonUtils.get_equivalence_classes(solution)
  fresh_var_generator.set_annotations(
      equivalence_classes, var_id_to_annotation, lambda x: f"T{x}"
  )

  print(solution)
  PythonTypeInferenceUtils.print_solution(
      location_id_to_var_ids_and_values, location_to_id, fresh_var_generator
  )

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

    symbolic_shape = vars_and_values.common_type_value.get_repr(fresh_var_generator)
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
        s = annotation.to_string(indent=indent, show_concrete_shape=False, color=True)
        annotated_lines.append(s)

    end_index = transform_line_number(last_line_number)
    annotated_lines.extend(module_lines[end_index:])
    annotated_source = "\n".join(annotated_lines)
    if verbose:
      annotated_text = Text(annotated_source)
      annotated_text.highlight_regex(r"\s*# ↳.+", style="bold magenta")
      print_panel(annotated_text, title=f"Type annotations: [b]{module_name}")

    annotations_file = util.get_output_path(
        "python_type_inference", f"annotations/{module_name}.py"
    )
    log(f"Saving annotated source file: {annotations_file}.")
    with open(annotations_file, "w") as out:
      out.write("# Auto-generated file with array shape annotations.\n")
      out.write(f"# Original file: {module_path}\n\n")
      out.write(annotated_source)

  annotations_file = util.get_output_path("python_type_inference", "annotations.txt")
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
