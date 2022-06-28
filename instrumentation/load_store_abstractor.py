from typing import Any, Dict, List, Union, Optional

from .util import ObjectId, get_instrumented_program_frame

def stringify_maybe_object_id(self, maybe_id: Union[int, ObjectId]) -> \
    Optional[str]:
  if isinstance(maybe_id, ObjectId):
    obj = self.heap_object_tracking.get_by_id(maybe_id.id)
    if hasattr(obj, "shape"):
      shape = obj.shape
      return " #" + str(maybe_id.id) + ":" + str(shape)
    else:
      return None
  elif isinstance(maybe_id, int):
    return " int(" + str(maybe_id) + ")"
  else:
    return None
