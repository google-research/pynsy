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
from pynsy.analyses import util
from pynsy.instrumentation import logging

log = logging.logger(__name__)

record_list = []


def is_blank(val):
  return val != val


def abstraction(obj):
  if isinstance(obj, str):
    return False, "str"
  else:
    return True, None


def process_event(record):
  if record["type"] == "BINARY_ADD":
    if str(record["result_and_args"][0]["abs"]) == "str":
      print(
          f"Warning: at line {record['lineno']} in {record['module_name']}, the"
          " 'string addition' is slow.  Use \"\".join(str1, str2)"
      )
  return record_list.append(record)


def process_termination():
  df = pd.DataFrame(record_list)
  # df = df.explode('result_and_args')
  log_file = util.get_output_path("string_add_analysis", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)
