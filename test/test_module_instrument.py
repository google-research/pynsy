import re
import sys
from types import ModuleType, CodeType

from dis import opname
from bytecode import Compare

from instrumentation.module_loader import PatchingPathFinder
from instrumentation.event_receiver import EventReceiver

from typing import List

def cleanup_elem(e):
  if isinstance(e, ModuleType):
    return "<module " + e.__name__ + ">"
  else:
    return re.sub(
      "0x[a-zA-Z0-9]+",
      "SOME ADDRESS",
      re.sub(
        "file \"(.|[-/])*\"",
        "file \"some-file\"",
        str(e)
      )
    )

class LoggingReceiver(EventReceiver):
  log: List[object]
  is_in_receiver = False

  def __init__(self) -> None:
    self.log = []
    super().__init__()

  def on_event(self, stack, opcode, arg, opindex, code_id, is_post, id_to_orig_bytecode):
    if self.is_in_receiver:
      return # stringifying can result in recursion
    self.is_in_receiver = True
    if opcode == "JUMP_TARGET":
      self.log.append({ "arrive_at": arg["label"] })
    else:
      self.log.append({
        "arg": { "cmp": str(arg) } if (isinstance(arg, Compare)) else 
               cleanup_elem(str(arg)) if isinstance(arg, CodeType) else arg,
        "is_post": is_post,
        "opcode": opcode if isinstance(opcode, str) else opname[opcode],
        "stack": list(map(cleanup_elem, stack)),
      })
    self.is_in_receiver = False

def test_calls_to_module_function(snapshot):
  patcher = PatchingPathFinder()
  patcher.install()
  logger = LoggingReceiver()
  with logger:
    from .simple_module_to_import import hello
    hello()
  snapshot.assert_match(logger.log)
  patcher.uninstall()

def test_calls_to_numpy_function(snapshot):
  patcher = PatchingPathFinder()
  patcher.install()

  import numpy as np

  logger = LoggingReceiver()
  with logger:
    np.linalg.eigvals(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
  snapshot.assert_match(logger.log, name=str((snapshot.snapshot_counter, sys.version_info.major, sys.version_info.minor)))
  snapshot.snapshot_counter += 1
  patcher.uninstall()
