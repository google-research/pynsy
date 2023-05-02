from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

from bytecode import Bytecode


class EventReceiver(object):
  current_exit_func: Optional[Callable[[], None]] = None
  def on_event(self, stack: List[Any], instr_id: int, method_id: int, module_name: str, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]) -> None:
    pass

  def __enter__(self) -> None:
    assert self.current_exit_func is None
    self.current_exit_func = add_receiver(self)
  
  def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
    assert self.current_exit_func is not None
    self.current_exit_func()
    self.current_exit_func = None

_active_receivers: List[EventReceiver] = []

def add_receiver(receiver: EventReceiver) -> Callable[[], None]:
  _active_receivers.insert(0, receiver)
  return lambda: _active_receivers.remove(receiver)

def call_all_receivers(stack: List[Any], instr_id: int, method_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode], module_name: str) -> None:
  for receiver in _active_receivers:
    receiver.on_event(stack, instr_id, method_id, module_name, is_post, id_to_orig_bytecode)
