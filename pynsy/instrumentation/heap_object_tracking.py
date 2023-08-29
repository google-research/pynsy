# Copyright 2023 The pynsy Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any
from typing import Dict


class HeapObjectTracker(object):
  special_key = "_pajama_76538321_"
  objects_to_id: Dict[Any, int]
  id_to_objects: Dict[int, Any]

  def __init__(self) -> None:
    self.objects_to_id = {}  # WeakKeyDictionary() does not support list, dict
    self.id_to_objects = {}  # WeakValueDictionary() does not support list, dict
    self.next_object_id = 1

  def is_heap_object(self, obj: Any) -> bool:
    return hasattr(obj, "__dict__")

  def get_object_id(self, obj: Any) -> int:
    if (
        hasattr(obj, "__dict__")
        and HeapObjectTracker.special_key in obj.__dict__
    ):
      oid = obj.__dict__[HeapObjectTracker.special_key]
    else:
      oid = id(obj)

    if oid in self.objects_to_id:
      return self.objects_to_id[oid]
    else:
      try:
        if hasattr(obj, "__dict__"):
          obj.__dict__[HeapObjectTracker.special_key] = oid
      except:
        pass
      self.objects_to_id[oid] = self.next_object_id
      self.id_to_objects[self.next_object_id] = obj
      self.next_object_id += 1
      return self.objects_to_id[oid]

  def get_object_by_id(self, object_id: int) -> Any:
    if object_id in self.id_to_objects:
      return self.id_to_objects[object_id]
    else:
      return None
