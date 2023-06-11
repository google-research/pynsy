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

def quicksort_return(a):
  quick1(a)
  return a


def quick1(a, st=0, en=None):
  if en is None:
    en = len(a)
  if en - st <= 1:
    return
  pivot = a[st]
  start = st + 1
  end = en - 1
  while end > start:
    while a[start] <= pivot and start < en - 1:
      start += 1
    while pivot <= a[end] and end >= start:
      end -= 1
    if end >= start:
      a[start], a[end] = a[end], a[start]
  if a[end] > pivot:
    a[end - 1], a[st] = a[st], a[end - 1]
    quick1(a, st, end - 1)
    quick1(a, end, en)
  elif a[end] <= pivot:
    a[end], a[st] = a[st], a[end]
    quick1(a, st, end)
    quick1(a, end + 1, en)


print(quicksort_return([3, 4, 1, -5, 2, 10, -6]))
