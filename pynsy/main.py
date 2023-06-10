from pynsy.instrumentation.module_loader import instrument_imports, import_method_from_module
import sys

pgm = sys.argv[2]
print(pgm)

with instrument_imports():
  import_method_from_module(pgm)
