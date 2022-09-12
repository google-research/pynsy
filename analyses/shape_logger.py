import json
from instrumentation.util import serialize

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
  for record in record_list:
    print(json.dumps(record, default=serialize))
