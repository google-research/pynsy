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

import importlib
import importlib.util
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
  module_name = _MODULE_FLAG.value
  # Rewrite `argv` to be absl-parsed flags.
  this_module_name = sys.argv[0]
  sys.argv = argv
  # Remove parsed flags to avoid flag name conflicts with the
  # module-to-instrument.
  flag_module_dict = flags.FLAGS.flags_by_module_dict()
  fv = flags.FlagValues()
  for flag in flag_module_dict[this_module_name]:
    fv[flag.name] = flag
  flags.FLAGS.remove_flag_values(fv)
  with instrument_imports(config):
    # Execute module with name `__main__` (top-level code environment).
    # This exactly replicates the behavior of directly executing the module.
    spec = importlib.util.find_spec(module_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    module.__name__ = '__main__'
    spec.loader.exec_module(module)


if __name__ == '__main__':
  app.run(main)
