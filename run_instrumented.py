from pynsy.instrumentation.module_loader import PatchingPathFinder
from pynsy.instrumentation.operator_apply import OperatorApply
import sys
import config



patcher = PatchingPathFinder()
patcher.install()


def import_method_from_module(s):
  return __import__(s, globals(), locals(), [None], 0)


receiver = OperatorApply()
print(sys.argv[1])
config.custom_analyzer = import_method_from_module(sys.argv[1])
receiver.__enter__()
pgm = sys.argv[2]
sys.argv = sys.argv[2:]
print(pgm)
module_under_test = import_method_from_module(pgm)
config.custom_analyzer.process_termination(receiver.trace_logger)

