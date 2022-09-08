import importlib.machinery
import importlib.util
import os

# Import mymodule
def load_main_python_program(filepath):
  modulename = os.path.basename(filepath)
  loader = importlib.machinery.SourceFileLoader(modulename, filepath)
  spec = importlib.util.spec_from_loader( modulename, loader )
  mymodule = importlib.util.module_from_spec( spec )
  loader.exec_module( mymodule )

