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

from absl import app
from absl import flags

from pynsy.instrumentation.module_loader import instrument_imports

_CONFIG_FLAG = flags.DEFINE_string(
    'config', 'config.json', 'Path to config file.'
)


def main(argv):
  del argv
  with instrument_imports(_CONFIG_FLAG.value):
    # Import any module within this context to instrument it.
    import pynsy.demos.key_in_list


if __name__ == '__main__':
  app.run(main)
