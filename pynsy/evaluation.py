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

from collections.abc import Sequence
import pandas as pd
import subprocess
from timeit import default_timer as timer

import fire
import tqdm

from pynsy.analyses import util


def run_command(args: Sequence[str]) -> int:
  start = timer()
  subprocess.run(args, capture_output=True, check=True)
  end = timer()
  return end - start


class PythonCommand:

  def __init__(self, name: str, raw_command: str):
    self.name = name
    self.raw_command = raw_command
    self.raw_args = raw_command.split(' ')

  def run_python_command(self) -> int:
    args = ['python3', '-m'] + self.raw_args
    return run_command(args)

  def run_pynsy_command(self) -> int:
    module_name, *remaining_args = self.raw_args
    args = [
        'python3',
        '-m',
        'pynsy.main',
        '--config',
        'configs/shape_analysis.toml',
        '--module',
        module_name,
        '--',
    ] + remaining_args
    return run_command(args)


EVAL_COMMANDS = [
    # Haiku examples
    PythonCommand(
        name='haiku/rnn',
        raw_command='pynsy.demos.haiku.examples.rnn.train',
    ),
    PythonCommand(
        name='haiku/impala_rl',
        raw_command='pynsy.demos.haiku.examples.impala.run_catch',
    ),
    PythonCommand(
        name='haiku/transformer',
        raw_command=(
            'pynsy.demos.haiku.examples.transformer.train '
            '--dataset_path=/tmp/shakespeare.txt'
        ),
    ),
    # Flax examples
    PythonCommand(
        name='flax/mnist',
        raw_command=(
            'pynsy.demos.flax.examples.mnist.main --workdir=/tmp/mnist '
            '--config=pynsy/demos/flax/examples/mnist/configs/default.py '
            '--config.num_epochs=1'
        ),
    ),
    # PyTorch examples
    PythonCommand(
        name='pytorch/gcn',
        raw_command=(
            'pynsy.demos.pytorch_examples.gcn.main --dry-run --epochs 1'
        ),
    ),
    PythonCommand(
        name='pytorch/mnist_forward_forward',
        raw_command=(
            'pynsy.demos.pytorch_examples.mnist_forward_forward.main --epochs 1'
        ),
    ),
    PythonCommand(
        name='pytorch/regression',
        raw_command='pynsy.demos.pytorch_examples.regression.main',
    ),
    # NOTE: Commented because prohibitively slow without --num_epochs flag.
    # PythonCommand(
    #     name='pytorch/rl/reinforce',
    #     raw_command=(
    #         'pynsy.demos.pytorch_examples.reinforcement_learning.reinforce'
    #     ),
    # ),
    # PythonCommand(
    #     name='pytorch/rl/actor_critic',
    #     raw_command=(
    #         'pynsy.demos.pytorch_examples.reinforcement_learning.actor_critic'
    #     ),
    # ),
    PythonCommand(
        name='pytorch/siamese_network',
        raw_command=(
            'pynsy.demos.pytorch_examples.siamese_network.main --dry-run '
            '--epochs 1'
        ),
    ),
    PythonCommand(
        name='pytorch/vae',
        raw_command='pynsy.demos.pytorch_examples.vae.main --epochs 1',
    ),
    PythonCommand(
        name='pytorch/vision_transformer',
        raw_command=(
            'pynsy.demos.pytorch_examples.vision_transformer.main --dry-run '
            '--epochs 1'
        ),
    ),
]


def run_evaluation():
  rows = []
  pbar = tqdm.tqdm(EVAL_COMMANDS)
  for command in pbar:
    pbar.set_description(f'Evaluating {command.name} baseline')
    try:
      baseline_time = command.run_python_command()
    except:
      baseline_time = 'Error'

    pbar.set_description(f'Evaluating {command.name} with Pynsy')
    try:
      pynsy_time = command.run_pynsy_command()
    except:
      pynsy_time = 'Error'

    row = dict(
        name=command.name,
        baseline_time=baseline_time,
        pynsy_time=pynsy_time,
    )
    print(row)
    rows.append(row)
  df = pd.DataFrame.from_records(rows)
  df = df.sort_values(by=['name'])
  print(df)
  df.to_csv(util.OUTPUT_ROOT_DIR / 'evaluation_performance.csv')
  df.to_latex(
      util.OUTPUT_ROOT_DIR / 'evaluation_performance.tex',
      index=False,
      escape=True,
  )


if __name__ == '__main__':
  fire.Fire()
