import pandas as pd

columns = ['operand', 'operand1', 'operand2', 'args_list', 'base', 'index', 'result', 'var_name', 'attr_name', 'function_name']
keys = ['module_name', 'method_id', 'instruction_id', 'lineno', 'type']
others = ['indentation', 'execution_index', 'type']

last_oid = -1
log_file = f"trace_compact.csv"


def is_blank(val):
  return val != val

def result_and_args(row):
  if row['type'] == 'LOAD_ATTR':
    row['result_and_args'] = [row['result'], row['base'], row['attr_name']]
  elif row['type'] == 'STORE_ATTR':
    row['result_and_args'] = [row['result'], row['base'], row['attr_name'], row['operand']]
  elif row['type'] == 'BINARY_SUBSCR':
    row['result_and_args'] = [row['result'], row['base'], row['index']]
  elif row['type'] == 'STORE_SUBSCR':
    row['result_and_args'] = [row['result'], row['base'], row['index'], row['operand']]
  elif 'operand' in row and not is_blank(row['operand']):
    row['result_and_args'] = [row['result'], row['operand']]
  elif 'operan1d' in row and 'operand2' in row and not is_blank(row['operand1']) or not is_blank(row['operand2']):
    row['result_and_args'] = [row['result'], row['operand1'], row['operand2']]
  elif 'args_list' in row and not is_blank(row['args_list']):
    row['result_and_args'] = [row['result']] + row['args_list']
  else:
    row['result_and_args'] = [row['result']]
  if 'var_name' in row and not is_blank(row['var_name']):
    row['name'] = row['var_name']
  elif 'function_name' in row and not is_blank(row['function_name']):
    row['name'] = str(row['function_name']) + '()'
  elif 'attr_name' in row and not is_blank(row['attr_name']):
    row['name'] = '.' + row['attr_name']
  return row


def abstraction(obj):
  if hasattr(obj, 'shape'):
    return False, obj.shape
  elif isinstance(obj, tuple) or isinstance(obj, list):
    return False, len(obj)
  elif isinstance(obj, int) or  isinstance(obj, float) or isinstance(obj, str):
    return False, obj
  return True, None

def process_event(record):
  return record

def process_termination(record_list):
  df = pd.DataFrame(record_list)
  df = df.apply(result_and_args, axis=1)
  df = df.drop(columns, axis=1, errors='ignore')
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
