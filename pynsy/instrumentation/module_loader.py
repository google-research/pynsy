import json
from importlib.abc import Loader
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import Any
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

from pynsy import handle
import sys

from .operator_apply import OperatorApply
from .instrument_nested import extract_all_codeobjects
from .instrument_nested import instrument_extracted

_Path = Union[bytes, str]


def get_longest_filter(path, rules):
  action = None
  depth = -1
  for filter, filter_action in rules:
    if path.startswith(filter):
      filter_depth = filter.count(".")
      if filter_depth > depth:
        depth = filter_depth
        action = filter_action
  return action, depth


def need_instrumentation(pkg_name: str) -> bool:
  action, depth = get_longest_filter(pkg_name, handle.instrumentation_rules)
  return action == "include" and depth >= 0


class PynsyLoader(Loader):
  name: str
  existing_loader: Loader
  finder: "PynsyPathFinder"

  def __init__(
      self, name: str, existing_loader: Loader, finder: "PynsyPathFinder"
  ) -> None:
    self.name = name
    self.existing_loader = existing_loader
    self.finder = finder
    # extra attributes that are dynamically checked for by module import system
    if hasattr(existing_loader, "get_filename"):
      setattr(self, "get_filename", lambda fullname: existing_loader.get_filename(fullname))  # type: ignore
    if hasattr(existing_loader, "is_package"):
      setattr(self, "is_package", lambda fullname: existing_loader.is_package(fullname))  # type: ignore

  def set_event_handler(self, handler: Any) -> None:
    self.event_handler = handler

  def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
    return self.existing_loader.create_module(spec)

  def load_module(self, fullname: str) -> ModuleType:
    return self.existing_loader.load_module(fullname)

  def module_repr(self, module: ModuleType) -> str:
    return self.existing_loader.module_repr(module)

  def exec_module(self, module: ModuleType) -> None:
    if hasattr(self.existing_loader, "get_code") and need_instrumentation(
        self.name
    ):
      module_code = self.existing_loader.get_code(self.name)  # type: ignore
      if module_code:
        print("[Python Analysis] Instrumenting module " + self.name)
        id_to_bytecode, code_to_id = extract_all_codeobjects(module_code)
        id_to_bytecode_new_codeobjects = instrument_extracted(
            id_to_bytecode, code_to_id
        )
        if not hasattr(handle, "bytecode"):
          handle.bytecode = dict()
        if self.name not in handle.bytecode:
          handle.bytecode[self.name] = id_to_bytecode
        instrumented = id_to_bytecode_new_codeobjects[code_to_id[module_code]]
        module_name = self.name

        def pynsy_receiver(
            stack: List[Any], instr_id: int, method_id: int, is_post: bool
        ) -> None:
          # print(method_id, instr_id, id_to_bytecode[method_id][instr_id])
          self.event_handler.on_event(
              stack, instr_id, method_id, module_name, is_post, id_to_bytecode
          )

        module.__dict__["pynsy_receiver"] = pynsy_receiver
        exec(instrumented.to_code(), module.__dict__)
        self.finder.patched_modules.append(module.__name__)
      else:
        self.existing_loader.exec_module(module)
    else:
      self.existing_loader.exec_module(module)


class PynsyPathFinder(MetaPathFinder):
  existing_importers: List[MetaPathFinder]
  current_path: Optional[Sequence[_Path]]
  patched_modules: List[str]

  def __init__(self, event_handler: OperatorApply) -> None:
    self.existing_importers = sys.meta_path.copy()
    self.patched_modules = []
    self.event_handler = event_handler

  def install(self) -> None:
    sys.meta_path.insert(0, self)

  def uninstall(self) -> None:
    sys.meta_path.remove(self)
    for module in self.patched_modules:
      del sys.modules[module]
    self.patched_modules = []

  def find_spec(
      self,
      fullname: str,
      path: Optional[Sequence[_Path]],
      target: Optional[ModuleType] = None,
  ) -> Optional[ModuleSpec]:
    for importer in self.existing_importers:
      if hasattr(importer, "find_spec"):
        existing_spec = importer.find_spec(fullname, path, target)
        if existing_spec is not None and existing_spec.loader is not None:
          existing_spec.loader = PynsyLoader(
              fullname, existing_spec.loader, self  # type: ignore
          )
          existing_spec.loader.set_event_handler(self.event_handler)
          return existing_spec

    return None


class HookManager:

  def __init__(self, event_handler: OperatorApply) -> None:
    self.path_finder = None
    self.event_handler = event_handler
    pass

  def __enter__(self) -> "HookManager":
    self.path_finder = PynsyPathFinder(self.event_handler)
    self.path_finder.install()
    return self

  def __exit__(self, *args: Any) -> None:
    self.path_finder.uninstall()
    for m in handle.custom_analyzer:
      m.process_termination()


def import_method_from_module(s):
  return __import__(s, globals(), locals(), [None], 0)


def instrument_imports() -> HookManager:
  event_handler = OperatorApply()
  print(f"loading config at {sys.argv[1]}")
  with open(sys.argv[1], "r") as f:
    handle.config = json.load(f)
  handle.instrumentation_rules = handle.config["instrumentation_rules"]
  handle.custom_analyzer = [
      import_method_from_module(m) for m in handle.config["analyzers"]
  ]
  sys.argv = sys.argv[2:]
  return HookManager(event_handler)
