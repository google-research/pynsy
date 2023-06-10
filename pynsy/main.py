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
