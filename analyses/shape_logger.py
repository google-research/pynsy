import json
from instrumentation.util import serialize
import config

import pandas as pd

# config.static_program_info contains the static bytecode information
# it maps module_name->method_id->instr_id->Bytecode

log_file = "trace.csv"


def abstraction(obj):
  if hasattr(obj, 'shape'):
    return str(obj.shape)
  elif callable(obj):
    return str(obj.__name__)
  elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
    return str(obj)
  else:
    return 'obj'

def process_event(record):
  return record

def process_termination(record_list):
  df = pd.DataFrame(record_list)
  pd.DataFrame.to_csv(df, log_file)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)
  pd.set_option("max_colwidth", None)
  print(df)
