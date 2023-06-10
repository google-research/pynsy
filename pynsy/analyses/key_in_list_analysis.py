import pandas as pd

log_file = f"trace_compact.csv"


record_list = []


def is_blank(val):
  return val != val


def abstraction(obj):
  if (
      isinstance(obj, tuple)
      or isinstance(obj, list)
      or str(type(obj)) == "<class 'range'>"
  ):
    return False, len(obj)
  elif (
      isinstance(obj, int)
      or isinstance(obj, float)
      or isinstance(obj, str)
      or isinstance(obj, bool)
  ):
    return True, obj
  else:
    return False, None


def process_event(record):
  if record["type"] == "CONTAINS_OP":
    if record["result_and_args"][3]["abs"] > 100:
      print(
          f"Warning: at line {record['lineno']} in {record['module_name']}, the"
          " 'key in list' is slow for a list of length"
          f" {record['result_and_args'][3]['abs']}."
      )
  record_list.append(record)


def process_termination():
  df = pd.DataFrame(record_list)
  print("Saving raw data as a pandas Dataframe in " + log_file)
  pd.DataFrame.to_csv(df, log_file)
