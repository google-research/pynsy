import sys
from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec
from types import ModuleType

from .instrument_nested import extract_all_codeobjects, instrument_extracted
from .event_receiver import call_all_receivers

from typing import Any, List, Optional, Sequence, Union
from typing_extensions import Literal

_Path = Union[bytes, str]

class PatchingLoader(Loader):
  name: str
  existing_loader: Loader
  finder: "PatchingPathFinder"

  def __init__(self, name: str, existing_loader: Loader, finder: "PatchingPathFinder") -> None:
    self.name = name
    self.existing_loader = existing_loader
    self.finder = finder

    # extra attributes that are dynamically checked for by module import system
    if hasattr(existing_loader, "get_filename"):
      setattr(self, "get_filename", lambda fullname: existing_loader.get_filename(fullname)) # type: ignore
    if hasattr(existing_loader, "is_package"):
      setattr(self, "is_package", lambda fullname: existing_loader.is_package(fullname)) # type: ignore

  def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
    return self.existing_loader.create_module(spec)

  def load_module(self, fullname: str) -> ModuleType:
    return self.existing_loader.load_module(fullname)

  def module_repr(self, module: ModuleType) -> str:
    return self.existing_loader.module_repr(module)

  def exec_module(self, module: ModuleType) -> None:
    if hasattr(self.existing_loader, "get_code") and self.name.startswith("demos."):
      module_code = self.existing_loader.get_code(self.name) # type: ignore
      if module_code:
        print("[Python Analysis] Instrumenting module " + self.name)
        id_to_bytecode, code_to_id = extract_all_codeobjects(module_code)
        id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

        instrumented = id_to_bytecode_new_codeobjects[code_to_id[module_code]]

        def py_instrument_receiver(stack: List[Any], opindex: int, code_id: int, is_post: bool) -> None:
          # print(code_id, opindex, id_to_bytecode[code_id][opindex])
          call_all_receivers(stack, opindex, code_id, is_post, id_to_bytecode)
        module.__dict__["py_instrument_receiver"] = py_instrument_receiver
        exec(instrumented.to_code(), module.__dict__)
        self.finder.patched_modules.append(module.__name__)
      else:
        self.existing_loader.exec_module(module)
    else:
      self.existing_loader.exec_module(module)

modules_to_skip: List[str] = []

class PatchingPathFinder(MetaPathFinder):
  existing_importers: List[MetaPathFinder]
  current_path: Optional[Sequence[_Path]]
  patched_modules: List[str]

  def __init__(self) -> None:
    self.existing_importers = sys.meta_path.copy()
    self.patched_modules = []

  def install(self) -> None:
    sys.meta_path.insert(0, self)

  def uninstall(self) -> None:
    sys.meta_path.remove(self)
    for module in self.patched_modules:
      del sys.modules[module]
    self.patched_modules = []

  def find_spec(self, fullname: str, path: Optional[Sequence[_Path]], target: Optional[ModuleType] = None) -> Optional[ModuleSpec]:
    for importer in self.existing_importers:
      if hasattr(importer, "find_spec"):
        existing_spec = importer.find_spec(fullname, path, target)
        if existing_spec is not None and existing_spec.loader is not None and fullname not in modules_to_skip:
          existing_spec.loader = PatchingLoader(
            fullname,
            existing_spec.loader, # type: ignore
            self
          )

          return existing_spec

    return None
