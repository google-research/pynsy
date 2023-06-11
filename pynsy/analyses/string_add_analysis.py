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

import pandas as pd

log_file = f"trace_compact.csv"

record_list = []


def is_blank(val):
  return val != val


def abstraction(obj):
  if isinstance(obj, str):
    return False, obj
  else:
    return True, None


def process_event(record):
  if record["type"] == "BINARY_ADD":
    if str(record["result_and_args"][0]["type"]) == "<class 'str'>":
      print(
          f"Warning: at line {record['lineno']} in {record['module_name']}, the"
          " 'string addition' is slow.  Use \"\".join(str1, str2)"
      )
  return record_list.append(record)


def process_termination():
  df = pd.DataFrame(record_list)
  # df = df.explode('result_and_args')
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
