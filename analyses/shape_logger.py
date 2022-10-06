import json
import logging

from instrumentation.util import serialize
import config

import pandas as pd

# config.static_program_info contains the static bytecode information
# it maps module_name->method_id->instr_id->Bytecode

from datetime import datetime
curr_dt = datetime.now()

timestamp = int(round(curr_dt.timestamp()))
columns = ['operand', 'operand1', 'operand2', 'result', 'args_list', 'base', 'index']
keys = ['module_name', 'method_id', 'instruction_id']


def process_event(record):
  return record

log_file = f"trace-{timestamp}.csv"

def is_non_None_row(row):
  for col in columns:
    if isinstance(row[col], tuple):
      return True
  if row['args_list'] is not None and isinstance(row['args_list'], list):
    curr_value = row['args_list']
    for arg in curr_value:
      if isinstance(arg, tuple):
        return True
  return False

def abstraction(obj):
  if hasattr(obj, 'shape'):
    return False, obj.shape
  elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
    return False, obj
  return True, None

def aggr(x):
  try:
    x = [tuple(e) if isinstance(e, list) else e for e in x]
    y = set(x)
    # if len(y) == 1:
    #   y = y[0]
  except TypeError as e:
    logging.debug(f"Set failed on {x} with {e}")
    raise e
  return y

def remove_singleton_set(e):
  if isinstance(e, set) and len(e) == 1:
    return next(iter(e))
  else:
    return e


def process_termination(record_list):
  df = pd.DataFrame(record_list)
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)

#  df = pd.read_csv(log_file)
#  df.fillna(0, inplace=True)
  indices = df.apply(is_non_None_row, axis=1)
  df = df[indices]
  df = df.groupby(keys).agg(aggr)
  df = df.applymap(remove_singleton_set)
  pd.DataFrame.to_csv(df, "filtered_" + log_file)
