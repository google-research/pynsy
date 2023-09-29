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

import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()

OUTPUT_ROOT_DIR = ROOT_DIR / "outdir"


def get_output_path(analysis_name: str, filename: str) -> str:
  output_path = OUTPUT_ROOT_DIR / analysis_name / filename
  output_path.parent.mkdir(parents=True, exist_ok=True)
  return output_path
