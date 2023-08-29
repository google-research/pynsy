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
from pynsy.instrumentation import logging_utils

log = logging_utils.logger(__name__)

record_list = []


def abstraction(obj):
  if (
      isinstance(obj, tuple)
      or isinstance(obj, list)
      or str(type(obj)) == "<class 'range'>"
  ):
    return False, len(obj)
  elif (
      isinstance(obj, int)
      or isinstance(obj, float)
      or isinstance(obj, str)
      or isinstance(obj, bool)
  ):
    return True, obj
  else:
    return False, None


def process_event(record):
  if record["type"] == "CONTAINS_OP":
    if record["result_and_args"][3]["abs"] > 100:
      print(
          f"Warning: at line {record['lineno']} in {record['module_name']}, the"
          " 'key in list' is slow for a list of length"
          f" {record['result_and_args'][3]['abs']}."
      )
  record_list.append(record)


def process_termination():
  df = pd.DataFrame(record_list)
  log_file = util.get_output_path("key_in_list_analysis", "trace.csv")
  log(f"Saving raw data to {log_file}.")
  pd.DataFrame.to_csv(df, log_file)
