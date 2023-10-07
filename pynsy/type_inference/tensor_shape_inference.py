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

import pandas as pd
from rich.text import Text

from pynsy.analyses import util
from pynsy.instrumentation import logging_utils
from pynsy.instrumentation import module_loader
from pynsy.type_inference import inference_engine

AbstractState = inference_engine.AbstractState
Template = inference_engine.Template
CommonUtils = inference_engine.CommonUtils

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

  def to_string(
      self, indent: int = 0, *, color: bool = True, latex: bool = True
  ) -> str:
    out = io.StringIO()
    out.write(" " * indent)
    name = CommonUtils.get_nickname(self.opcode, self.name)
    concrete_shape_str = " ".join(str(x) for x in self.concrete_shape)
    if latex:
      msg = (
          f"# {name}: {self.symbolic_shape} => {concrete_shape_str}"
      )
    else:
      msg = f"# ↳ {name}: {self.symbolic_shape} => {concrete_shape_str}"
    out.write(msg)
    s = out.getvalue()
    if color:
      s = styled(s, style="bold magenta")
    return s


class TensorShapeInferenceUtils:
  templates = [
      Template(
          "=",
          2,
          lambda state, vars: state.get(vars[0], 0) == state.get(vars[1], 0),
          lambda vars: f"{vars[0]}",
      ),
      Template(
          "+",
          3,
          lambda state, vars: False
          if state.get(vars[0], 0) == 0
             or state.get(vars[1], 0) == 0
             or state.get(vars[2], 0) == 0
          else state.get(vars[0], 0)
               == state.get(vars[1], 0) + state.get(vars[2], 0),
          lambda vars: f"{vars[0]} + {vars[1]}",
      ),
      Template(
          "*",
          3,
          lambda state, vars: False
          if state.get(vars[0], 0) == 0
             or state.get(vars[0], 0) == 1
             or state.get(vars[1], 0) == 0
             or state.get(vars[1], 0) == 1
             or state.get(vars[2], 0) == 0
             or state.get(vars[2], 0) == 1
          else state.get(vars[0], 0)
               == state.get(vars[1], 0) * state.get(vars[2], 0),
          lambda vars: f"{vars[0]} * {vars[1]}",
      ),
      Template(
          "/",
          3,
          lambda state, vars: False
          if state.get(vars[0], 0) == 0
          or state.get(vars[0], 0) == 1
          or state.get(vars[1], 0) == 0
          or state.get(vars[1], 0) == 1
          or state.get(vars[2], 0) == 0
          or state.get(vars[2], 0) == 1
          else state.get(vars[0], 0)
          == state.get(vars[1], 0) / state.get(vars[2], 0),
          lambda vars: f"{vars[0]} / {vars[1]}",
      ),
  ]

  @classmethod
  def to_consider(cls, value):
    return cls._is_shape(value["abs"])

  @classmethod
  def _is_shape(cls, s):
    return isinstance(s, list) or isinstance(s, tuple)

  @classmethod
  def create_var_ids(cls, abs, fresh_var_generator, location_id):
    var_ids = []
    for _ in abs:
      var_ids.append(fresh_var_generator.get_fresh_id(location_id))
    return var_ids

  @classmethod
  def get_state_update(cls, vars_and_values, value):
    var_ids = vars_and_values.var_ids
    state_update = dict(zip(var_ids, value["abs"]))
    return state_update

  @classmethod
  def set_annotation(cls, row, var_ids, var_id_to_annotation):
    if "special" in row:
      names = row["special"]
      for var_id, name in zip(var_ids, names):
        var_id_to_annotation[var_id] = name

  @classmethod
  def create_var_ids_and_global_state(
      cls, location_id_to_vars_and_values, fresh_var_generator, global_state
  ):
    for location_id, vars_and_values in location_id_to_vars_and_values.items():
      value = next(iter(vars_and_values.abstraction_set))
      vars_and_values.var_ids = cls.create_var_ids(
          value, fresh_var_generator, location_id
      )
      if len(vars_and_values.abstraction_set) == 1:
        global_state.update(zip(vars_and_values.var_ids, value))

  @classmethod
  def print_solution(
      cls,
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
      solution,
      identity_template,
  ):
    for (
        location_id,
        vars_and_values,
    ) in location_id_to_var_ids_and_values.items():
      # if all(
      #     solution[x].get_template() != identity_template
      #     for x in vars_and_values.var_ids
      # ):
        annotation = [solution[x] for x in vars_and_values.var_ids]
        print(
            f"{location_id}{location_to_id.get_key(location_id)} : {annotation}"
        )


def abstraction(obj):
  try:
    if hasattr(obj, "shape"):
      return True, obj.shape
  except:
    return True, None
  return True, None


def process_event(record):
  record_list.append(record)


def process_termination():
  verbose = True
  if not record_list:
    log("No instructions were instrumented.")
    return

  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("tensor_shape_inference", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)

  abstract_state = AbstractState(TensorShapeInferenceUtils)
  abstract_state.create_var_ids_and_global_state(record_list)
  abstract_state.create_local_states(record_list)

  (
      location_id_to_state_list,
      global_state,
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
      var_id_to_annotation,
      location_id_to_name,
      location_id_to_record_list_index,
  ) = abstract_state.get_data()

  for lid, state_list in location_id_to_state_list.items():
    for state in state_list:
      print(f"state({lid}: {state}")

  for k, v in location_id_to_var_ids_and_values.items():
    print(f"{k}{location_to_id.get_key(k)} : {v}")
  solution = CommonUtils.find_solution(
      fresh_var_generator.num_ids(),
      TensorShapeInferenceUtils.templates,
      global_state,
      location_id_to_state_list,
      location_id_to_var_ids_and_values,
  )
  print(var_id_to_annotation)
  equivalence_classes = CommonUtils.get_equivalence_classes(solution)
  fresh_var_generator.set_annotations(
      equivalence_classes, var_id_to_annotation, lambda x: f"d{x}"
  )

  for rhs in solution:
#    if rhs.get_template() != CommonUtils.identity_template:
      rhs.vars = [
          fresh_var_generator.get_annotation(var_id) for var_id in rhs.vars
      ]

  TensorShapeInferenceUtils.print_solution(
      location_id_to_var_ids_and_values,
      location_to_id,
      fresh_var_generator,
      solution,
      CommonUtils.identity_template,
  )

  total_dimensions_count = 0
  shown_dimensions_count = 0
  unified_dimensions = set()
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

    symbolic_shape = [solution[x] for x in vars_and_values.var_ids]
    concrete_shapes = vars_and_values.values

    total_dimensions_count += len(symbolic_shape)
    # if not all(
    #     solution[x].get_template() != CommonUtils.identity_template
    #     for x in vars_and_values.var_ids
    # ):
    #   continue

    annotation = Annotation(
        opcode=opcode,
        name=name,
        symbolic_shape=symbolic_shape,
        concrete_shape=[
            concrete_shape["abs"] for concrete_shape in concrete_shapes
        ],
    )
    shown_dimensions_count += len(symbolic_shape)
    unified_dimensions.update(repr(dim) for dim in symbolic_shape)
    annotations_by_line_by_module[module_name][line_number].append(annotation)

  log(f"Annotation count: {len(location_id_to_var_ids_and_values)}.")
  log(f"Dimensions count: {total_dimensions_count}.")
  log(f"Shown dimensions variable count: {shown_dimensions_count}.")
  log(
      f"Anti-unified dimension variables ({len(unified_dimensions)}): "
      f"{sorted(unified_dimensions)}."
  )

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
      annotated_text.highlight_regex(
          r"\s*# (↳|@\$\\triangleright\$@).+", style="bold magenta"
      )
      print_panel(annotated_text, title=f"Shape annotations: [b]{module_name}")

    annotations_file = util.get_output_path(
        "tensor_shape_inference", f"annotations/{module_name}.py"
    )
    log(f"Saving annotated source file: {annotations_file}.")
    with open(annotations_file, "w") as out:
      out.write("# Auto-generated file with array shape annotations.\n")
      out.write(f"# Original file: {module_path}\n\n")
      out.write(annotated_source)

  annotations_file = util.get_output_path(
      "tensor_shape_inference", "annotations.txt"
  )
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
