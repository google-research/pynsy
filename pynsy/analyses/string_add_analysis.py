import pandas as pd

log_file = f"trace_compact.csv"

record_list = []


def is_blank(val):
  return val != val


def abstraction(obj):
  if isinstance(obj, str):
    return False, obj
  else:
    return True, None


def process_event(record):
  if record["type"] == "BINARY_ADD":
    if str(record["result_and_args"][0]["type"]) == "<class 'str'>":
      print(
          f"Warning: at line {record['lineno']} in {record['module_name']}, the"
          " 'string addition' is slow.  Use \"\".join(str1, str2)"
      )
  return record_list.append(record)


def process_termination():
  df = pd.DataFrame(record_list)
  # df = df.explode('result_and_args')
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
