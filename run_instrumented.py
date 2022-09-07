#from builtins import function
from dis import opname

from instrumentation.module_loader import PatchingPathFinder
from instrumentation.shape_logging_receiver import ShapeLoggingReceiver
import importlib.machinery
import importlib.util
import os, sys
import importlib

# Import module
def load_main_python_program(filepath):
  modulename = os.path.basename(filepath)
  loader = importlib.machinery.SourceFileLoader(modulename, filepath)
  spec = importlib.util.spec_from_loader( modulename, loader )
  mymodule = importlib.util.module_from_spec( spec )
  return loader, mymodule

#loader, mymodule = load_main_python_program(sys.argv[1])


patcher = PatchingPathFinder()
patcher.install()

p_m_f = sys.argv[1].split(".")
m = p_m_f[-2]
f = p_m_f[-1]
p = '.'.join(p_m_f[:-1])
print(p, m, f)
PUT = __import__(p, globals(), locals(), [], 0)
module_under_test = getattr(PUT, m)
function_under_test = getattr(module_under_test, f)

receiver = ShapeLoggingReceiver()

with receiver:
  function_under_test()


for record in receiver.trace_logger:
  print(record)


# Run ./run_instrumented.py demo.mnist.init_fun