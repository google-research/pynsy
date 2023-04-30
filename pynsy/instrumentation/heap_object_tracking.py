from typing import Any
from typing import Dict


class HeapObjectTracker(object):
  special_key = '_pajama_76538321_'
  objects_to_id: Dict[Any, int]
  id_to_objects: Dict[int, Any]

  def __init__(self) -> None:
    self.objects_to_id = {} #WeakKeyDictionary() does not support list, dict
    self.id_to_objects = {} #WeakValueDictionary() does not support list, dict
    self.next_object_id = 1

  def is_heap_object(self, obj: Any) -> bool:
    return hasattr(obj, '__dict__')

  def get_object_id(self, obj: Any) -> int:
    if hasattr(obj, '__dict__') and HeapObjectTracker.special_key in obj.__dict__:
      oid = obj.__dict__[HeapObjectTracker.special_key]
    else:
      oid = id(obj)

    if oid in self.objects_to_id:
      return self.objects_to_id[oid]
    else:
      try:
        if hasattr(obj, '__dict__'):
          obj.__dict__[HeapObjectTracker.special_key] = oid
      except:
        pass
      self.objects_to_id[oid] = self.next_object_id
      self.id_to_objects[self.next_object_id] = obj
      self.next_object_id += 1
      return self.objects_to_id[oid]

  def get_by_id(self, id: int) -> Any:
    if id in self.id_to_objects:
      return self.id_to_objects[id]
    else:
      return None
