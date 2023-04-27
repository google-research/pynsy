from instrumentation.module_loader import PatchingPathFinder
from instrumentation.operator_apply import OperatorApply
import sys
import config



patcher = PatchingPathFinder()
patcher.install()


def import_method_from_module(s):
  module_path = s.split(".")
  m = module_path[-1]
  PUT = __import__(s, globals(), locals(), [], 0)
  module_to_load = getattr(PUT, m)
  return module_to_load


receiver = OperatorApply()
print(sys.argv[1])
config.custom_analyzer = import_method_from_module(sys.argv[1])
receiver.__enter__()
pgm = sys.argv[2]
sys.argv = sys.argv[2:]
print(pgm)
module_under_test = import_method_from_module(pgm)
config.custom_analyzer.process_termination(receiver.trace_logger)

