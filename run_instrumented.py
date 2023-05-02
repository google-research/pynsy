import json

from pynsy.instrumentation.module_loader import PatchingPathFinder
from pynsy.instrumentation.operator_apply import OperatorApply
import sys
from pynsy import handle



patcher = PatchingPathFinder()
patcher.install()


def import_method_from_module(s):
  return __import__(s, globals(), locals(), [None], 0)


receiver = OperatorApply()
print(f"loading config at {sys.argv[1]}")
with open(sys.argv[1], "r") as f:
  handle.config = json.load(f)
handle.custom_analyzer = import_method_from_module(handle.config["analyzer"])
receiver.__enter__()
pgm = sys.argv[2]
sys.argv = sys.argv[2:]
print(pgm)
module_under_test = import_method_from_module(pgm)
handle.custom_analyzer.process_termination(receiver.trace_logger)

