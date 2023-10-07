import dataclasses
import itertools
from typing import Any


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


class FreshVarIdGenerator:

  def __init__(self):
    self.var_id_to_value = list()
    self.var_id_to_annotation = None

  def get_fresh_id(self, value):
    self.var_id_to_value.append(value)
    return len(self.var_id_to_value) - 1

  def get_value(self, id):
    return self.var_id_to_value[id]

  def num_ids(self):
    return len(self.var_id_to_value)

  def set_annotations(self, equivalence_classes, name_space, formatter):
    var_id_to_annotation = [None] * self.num_ids()
    for i, s in enumerate(equivalence_classes):
      done = False
      if s is not None:
        for n in name_space:
          if n in s:
            done = True
            for e in s:
              var_id_to_annotation[e] = name_space[n]
            break
        if not done:
          min_e = min(s)
          for e in s:
            var_id_to_annotation[e] = formatter(min_e)
    self.var_id_to_annotation = var_id_to_annotation

  def get_annotation(self, id):
    return self.var_id_to_annotation[id]


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
      "RETURN_VALUE": "return",
  }

  identity_template = Template(
      "identity", 1, lambda state, vars: True, lambda vars: vars[0]
  )

  @classmethod
  def find_solution(
      cls,
      n_var_ids,
      templates,
      global_state,
      location_id_to_state_list,
      location_id_to_var_ids_and_values,
  ):
    solution = [
        TemplateInstance(cls.identity_template, [i]) for i in range(n_var_ids)
    ]
    for template in templates:
      for location_id, state_list in location_id_to_state_list.items():
        exclude = location_id_to_var_ids_and_values[location_id].var_ids
        for var in exclude:
          if solution[var].get_template() == cls.identity_template:
            vars_list = [
                i
                for i in range(n_var_ids)
                if i != var
                and solution[i].get_template() == cls.identity_template
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


@dataclasses.dataclass
class VarIdsAndValues:
  var_ids: list[int]
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


class AbstractState:

  def __init__(self, type_utils):
    self.keys = ["module_name", "method_id", "instruction_id", "lineno", "type"]
    self.location_id_to_state_list = dict()
    self.location_id_to_var_ids_and_values = dict()
    self.location_to_id = UniqueIdForKey()
    self.var_id_to_annotation = dict()
    self.location_id_to_name = dict()
    self.location_id_to_record_list_index = dict()
    self.fresh_var_generator = FreshVarIdGenerator()
    self.global_state = dict()
    self.method_id_to_var_ids = dict()
    self.type_utils = type_utils

  def get_data(self):
    return (
        self.location_id_to_state_list,
        self.global_state,
        self.location_id_to_var_ids_and_values,
        self.location_to_id,
        self.fresh_var_generator,
        self.var_id_to_annotation,
        self.location_id_to_name,
        self.location_id_to_record_list_index,
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
      if self.type_utils.to_consider(value):
        location = tuple([row[x] for x in self.keys])
        location_id = self.location_to_id.get_id(location)
        print(f"line [{row['lineno']}]: trace({location_id}) = {value['abs']}")
        if location_id not in self.location_id_to_var_ids_and_values:
          vars_and_values = VarIdsAndValues()
          vars_and_values.add_to_abstraction_set(value["abs"])
          self.location_id_to_var_ids_and_values[location_id] = vars_and_values
        else:
          self.location_id_to_var_ids_and_values[
              location_id
          ].add_to_abstraction_set(value["abs"])
    self.type_utils.create_var_ids_and_global_state(
        self.location_id_to_var_ids_and_values,
        self.fresh_var_generator,
        self.global_state,
    )

  def create_local_states(self, record_list):
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

      if row["type"].startswith("EXIT_") and not record_list[i - 1][
          "type"
      ].startswith("CALL_") \
          and not name == "annotate_shape" \
          and not name == "hyper_parameter":
        state = state_stack.pop()
      if not row["type"].startswith("EXIT_") and record_list[i - 1][
          "type"
      ].startswith("CALL_") \
          and not name == "annotate_shape" \
          and not name == "hyper_parameter":
        method_id = row["method_id"]
        state_stack.append(state)
        var_ids_in_method = self.get_var_ids_in_method(method_id)
        state = {
            key: state[key] for key in state if key not in var_ids_in_method
        }

      value = row["result_and_args"][0]
      if self.type_utils.to_consider(value):
        location = tuple([row[x] for x in self.keys])
        location_id = self.location_to_id.get_id(location)
        self.location_id_to_name[location_id] = name
        self.location_id_to_record_list_index[location_id] = i
        var_ids = self.location_id_to_var_ids_and_values[location_id].var_ids
        self.location_id_to_var_ids_and_values[location_id].add_value(value)

        method_id = row["method_id"]
        var_ids_in_method = self.get_var_ids_in_method(method_id)
        var_ids_in_method.update(var_ids)

        self.type_utils.set_annotation(row, var_ids, self.var_id_to_annotation)

        value = self.location_id_to_var_ids_and_values[
            location_id
        ].get_last_value()
        state_update = self.type_utils.get_state_update(
            self.location_id_to_var_ids_and_values[location_id], value
        )
        state.update(state_update)
        if location_id not in self.location_id_to_state_list:
          self.location_id_to_state_list[location_id] = list()
        self.location_id_to_state_list[location_id].append(dict(state))
