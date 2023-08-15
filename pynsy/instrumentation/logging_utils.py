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

import io
from typing import Any

from rich.console import Console
from rich.markup import escape
from rich.panel import Panel

CONSOLE = Console()

rprint = CONSOLE.print


def styled(text: str, style: str, *, end: str = "") -> str:
  """Returns text styled via rich."""
  # string_console = Console()
  # with string_console.capture() as capture:
  #   string_console.print(text, style=style, end=end)
  # return capture.get()
  string_console = Console(file=io.StringIO())
  string_console.print(escape(text), style=style, end=end)
  return string_console.file.getvalue()


def print_panel(renderable: Any, title: str = ""):
  CONSOLE.print(Panel(renderable, title=title))


def logger(analysis_name: str):
  """Returns a logger function."""
  def log(message: str):
    rprint(f"[bold][blue]{analysis_name}[/]: {message}")

  return log
