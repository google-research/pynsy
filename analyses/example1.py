import pandas as pd

columns = ['name', 'result_args']
keys = ['module_name', 'method_id', 'instruction_id', 'lineno', 'type']
others = ['indentation', 'execution_index', 'type']

last_oid = -1
log_file = f"trace_compact.csv"


def is_blank(val):
  return val != val

def abstraction(obj):
  if hasattr(obj, 'shape'):
    return False, obj.shape
  elif isinstance(obj, tuple) or isinstance(obj, list):
    return False, len(obj)
  elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
    return False, obj
  else:
    return False, None

def process_event(record):
  return record

def process_termination(record_list):
  df = pd.DataFrame(record_list)
  #df = df.explode('result_and_args')
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
