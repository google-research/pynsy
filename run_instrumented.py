#from builtins import function
from dis import opname

from instrumentation.module_loader import PatchingPathFinder
from instrumentation.load_store_apply import LoadStoreApplyReceiver
import sys
import config



patcher = PatchingPathFinder()
patcher.install()


def import_method_from_module(s, isMethod=True):
  p_m_f = s.split(".")
  if isMethod:
    f = p_m_f.pop()
  else:
    f = None
  m = p_m_f[-1]
  p = '.'.join(p_m_f)
  print(p, f)
  PUT = __import__(p, globals(), locals(), [], 0)
  module_to_load = getattr(PUT, m)
  if isMethod:
    method_to_run = getattr(module_to_load, f)
    return method_to_run
  else:
    return module_to_load


receiver = LoadStoreApplyReceiver()
config.custom_analyzer = import_method_from_module(sys.argv[1], False)
#function_under_test = import_method_from_module(sys.argv[2], True)


with receiver:
  pgm = sys.argv[2]
  sys.argv = sys.argv[2:]
  function_under_test = import_method_from_module(pgm, False)
#  function_under_test()


config.custom_analyzer.process_termination(receiver.trace_logger)

