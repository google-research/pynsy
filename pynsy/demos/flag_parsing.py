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

import json
import sys

from absl import app
from absl import flags

flags.DEFINE_string('string', 'Hello world', 'String flag.')
flags.DEFINE_integer('int', 10, 'Int flag.')


def main(argv):
  print('sys.argv')
  print(sys.argv)
  print()

  print('absl.flags: argv')
  print(argv)
  print()

  print('absl.flags.FLAGS.flag_values_dict()')
  print(json.dumps(flags.FLAGS.flag_values_dict(), indent=2))


app.run(main)
