from textwrap import dedent
from dis import opname

from instrumentation.stack_tracking_receiver import StackTrackingReceiver
from instrumentation.data_tracing_receiver import DataTracingReceiver
from instrumentation.module_loader import PatchingPathFinder
from instrumentation.exec import exec_instrumented
import json
patcher = PatchingPathFinder()
patcher.install()

from demos.mnist import init_fun
# import random
# arr = [random.randint(0, 10) for i in range(10)]
# orig_arr = list(arr)
#receiver = DataTracingReceiver()
receiver = StackTrackingReceiver()
with receiver:
  #  with receiver:
  init_fun()

for k, v in receiver.trace_logger.items():
  print(k, ": ", v)
#print(json.dumps(receiver.trace_logger,indent=4))

def pretty_symbolic(symbolic):
  if symbolic.is_cow_pointer:
    return pretty_symbolic(symbolic.cow_latest_value)
  elif symbolic.collection_elems:
    return "[" + ", ".join(pretty_symbolic(elem) for elem in symbolic.collection_elems) + "]"
  else:
    return receiver.stringify_maybe_object_id(symbolic.concrete)

def print_deps(symbolic, indent_level=0):
  indent = '  ' * indent_level
  if symbolic.is_cow_pointer:
    print_deps(symbolic.cow_latest_value, indent_level)
  elif symbolic.collection_elems:
    print(f"{indent}collection with elements:")
    for elem in symbolic.collection_elems:
      print_deps(elem, indent_level + 1)
  elif opname[symbolic.opcode] == "BINARY_SUBSCR":
    print(f"{indent}{pretty_symbolic(symbolic)} depends on index {symbolic.deps[1]} of collection {pretty_symbolic(symbolic.deps[0])}")
    print_deps(symbolic.deps[0].collection_elems[symbolic.deps[1]], indent_level + 1)
  else:
    print(f"{indent}{pretty_symbolic(symbolic)} depends via {opname[symbolic.opcode]}")
    for dep in symbolic.deps:
      print_deps(dep, indent_level + 1)

# print("orig: " + str(orig_arr))
# print("out: " + str(arr))

#print_deps(receiver.symbolic_stack.pop())

# import numpy as np
# arr = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# with StackTrackingReceiver():
#   np.linalg.eigvals(arr)

# source = dedent(
# """
# def myFunc():
#   x = -1
#   data = list(range(5))
#   for i in data:
#     if i == 3:
#       break
#     else:
#       while i > 0:
#         x += i
#         i -= 1
# myFunc()
# """
# )

# source = dedent(
# """
# def factorial(i):
#   if i == 0:
#     return 1
#   else:
#     return i * factorial(i - 1)

# factorial(5)
# """
# )

# source = dedent(
# """
# my_arr = [1, 2, 3]
# for i in range(0, 3):
#   my_arr[i] = my_arr[i] + 1
# """
# )

# source = dedent(
#   """
#   x = 1 # global so won't show up in trace because we don't instrument globals yet
#   y = 2
#   z = 3


#   def f1():
#       print(x)
#       w = 4
#       u = 5

#       def f2():
#           print(x)
#           u = 6
#           print(u)
#           print(w)

#           def f3():
#               print(u)
#               print(w)
#               print(x)

#           f3()
#       f2()

#   f1()
#   """
# )

# with StackTrackingReceiver():
#   exec_instrumented(source)
