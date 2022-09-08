from dis import Bytecode

from bytecode import Instr
import re

from instrumentation.util import is_const_load_function

# smart diffing of in - out bytecodes because we only insert new instructions
# also returns a mapping from original op indices in b1 to op indices in the b2 code object
def diff_bytecodes(b1, b2):
  b1_code = b1.to_code()
  b2_code = b2.to_code()

  b1_str = list(filter(None, Bytecode(b1_code).dis().splitlines()))
  b2_str = list(filter(None, Bytecode(b2_code).dis().splitlines()))

  diff_lines = []

  old_to_new = {}

  cur_orig_index = 0
  b2_lines_index = 0
  for i in range(len(b2)):
    # use referential equality because we pass through existing ops
    if b1[cur_orig_index] is b2[i]:
      if isinstance(b2[i], Instr):
        old_to_new[cur_orig_index] = b2_lines_index
        diff_lines.append(" " + b2_str[b2_lines_index])
        b2_lines_index += 1
      cur_orig_index += 1
    elif is_const_load_function(b1[cur_orig_index]):
      old_to_new[cur_orig_index] = b2_lines_index
      diff_lines.append((" " if b1[cur_orig_index].arg is b2[i].arg else "~") + re.sub(
        "0x[a-zA-Z0-9]+",
        "SOME ADDRESS",
        b2_str[b2_lines_index]
      ))
      b2_lines_index += 1
      cur_orig_index += 1
    else:
      diff_lines.append("+" + re.sub(
        "0x[a-zA-Z0-9]+",
        "SOME ADDRESS",
        b2_str[b2_lines_index]
      ))
      b2_lines_index += 1

  return ("\n".join(diff_lines), old_to_new)
