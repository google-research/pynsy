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

import sys

from absl import app
from absl import flags

from pynsy.instrumentation.module_loader import instrument_imports, import_method_from_module

_CONFIG_FLAG = flags.DEFINE_string(
    'config', None, 'Path to config file', required=True
)
_MODULE_FLAG = flags.DEFINE_string(
    'module', None, 'Module to run', required=True
)


def main(argv):
  config = _CONFIG_FLAG.value
  module = _MODULE_FLAG.value
  # Strip `argv[0]`, which is the program name.
  sys.argv = argv[1:]
  with instrument_imports(config):
    import_method_from_module(module)


if __name__ == '__main__':
  app.run(main)
