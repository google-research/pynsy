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
handle.instrumentation_rules = handle.config["instrumentation_rules"]
handle.custom_analyzer = [import_method_from_module(m) for m in handle.config["analyzers"]]

receiver.__enter__()
pgm = sys.argv[2]
sys.argv = sys.argv[2:]
print(pgm)
module_under_test = import_method_from_module(pgm)
for m in handle.custom_analyzer: m.process_termination()


