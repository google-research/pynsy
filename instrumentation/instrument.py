from types import CodeType, LambdaType

from bytecode import Bytecode, CellVar, FreeVar, Instr, Label, UNSET

from .util import clone_bytecode_empty_body

from typing import Any, Callable, Dict, Optional, Union, cast
from typing_extensions import Literal

# Mappings from op to the size of the stack to report

binary_ops = [
  "BINARY_POWER",
  "BINARY_MULTIPLY",
  "BINARY_MATRIX_MULTIPLY",
  "BINARY_FLOOR_DIVIDE",
  "BINARY_TRUE_DIVIDE",
  "BINARY_MODULO",
  "BINARY_ADD",
  "BINARY_SUBTRACT",
  "BINARY_SUBSCR",
  "BINARY_LSHIFT",
  "BINARY_RSHIFT",
  "BINARY_AND",
  "BINARY_XOR",
  "BINARY_OR",

  "COMPARE_OP",

  "INPLACE_POWER",
  "INPLACE_MULTIPLY",
  "INPLACE_MATRIX_MULTIPLY",
  "INPLACE_FLOOR_DIVIDE",
  "INPLACE_TRUE_DIVIDE",
  "INPLACE_MODULO",
  "INPLACE_ADD",
  "INPLACE_SUBTRACT",
  "INPLACE_LSHIFT",
  "INPLACE_RSHIFT",
  "INPLACE_AND",
  "INPLACE_XOR",
  "INPLACE_OR",

  "MAKE_FUNCTION" # TODO(shadaj): can take more than two args based on flags
]

unary_ops = [
  "UNARY_POSITIVE",
  "UNARY_NEGATIVE",
  "UNARY_NOT",
  "UNARY_INVERT"
]

# Opcodes to instrument before they run
pre_opcode_instrument: Dict[str, Union[int, Callable[[Instr], int]]] = {
  "SETUP_LOOP": 0,
  "STORE_NAME": 1,
  "STORE_FAST": 1,
  "STORE_DEREF": 1,
  "STORE_ATTR": 2,
  "STORE_SUBSCR": 3,
  "LOAD_ATTR": 1,
  "POP_TOP": 1,
  "POP_JUMP_IF_TRUE": 1,
  "POP_JUMP_IF_FALSE": 1,
  "ROT_TWO": 2,
  "CALL_FUNCTION": lambda op: cast(int, op.arg) + 1, # capture all args as well as the function
  "RETURN_VALUE": 1
}

# Opcodes to instrument after they run
post_opcode_instrument = {
  "LOAD_NAME": 1,
  "LOAD_FAST": 1,
  "LOAD_DEREF": 1,
  "LOAD_CLOSURE": 1,
  "LOAD_ATTR": 1,
  "LOAD_CONST": 1,
  "LOAD_GLOBAL": 1,
  "CALL_FUNCTION": 1, # capture the return value
}

for op in binary_ops:
  pre_opcode_instrument[op] = 2
  post_opcode_instrument[op] = 1

def emit_instrument(
  instrumented: Bytecode,
  op: Instr, i: int, stacksize: int,
  label_to_op_index: Dict[Label, int],
  code_id: int, is_post: bool,
  opcode: Optional[Union[int, Literal["JUMP_TARGET"]]] = None,
  arg: Any = None
) -> None:
  def emit_kv(k: str, v: Union[str, int]) -> None:
    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = k,
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = v,
      lineno = op.lineno
    ))

    instrumented.append(Instr(
      name = "BUILD_MAP",
      arg = 1,
      lineno = op.lineno
    ))

  if stacksize > 0:
    instrumented.append(Instr(
      name = "BUILD_LIST",
      arg = stacksize,
      lineno = op.lineno
    ))

    # make a copy to send to the receiver
    instrumented.append(Instr(
      name = "DUP_TOP",
      lineno = op.lineno
    ))

  # load the receiver
  instrumented.append(Instr(
    name = "LOAD_GLOBAL",
    arg = "py_instrument_receiver",
    lineno = op.lineno
  ))

  if stacksize > 0:
    # move the list copy to the end of the stack
    instrumented.append(Instr(
      name = "ROT_TWO",
      lineno = op.lineno
    ))
  else:
    # add an empty list since we have zero stacksize
    instrumented.append(Instr(
      name = "BUILD_LIST",
      arg = 0,
      lineno = op.lineno
    ))

  # add additional parameters specifying the opcode, argument, and original op index
  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = opcode if opcode else op.opcode,
    lineno = op.lineno
  ))

  if not arg:
    arg = op.arg

  if isinstance(arg, Label):
    emit_kv("label", label_to_op_index[arg])
  elif isinstance(arg, CellVar):
    emit_kv("cell", arg.name)
  elif isinstance(arg, FreeVar):
    emit_kv("free", arg.name)
  else:
    instrumented.append(Instr(
      name = "LOAD_CONST",
      arg = None if arg == UNSET else arg,
      lineno = op.lineno
    ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = i,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = code_id,
    lineno = op.lineno
  ))

  instrumented.append(Instr(
    name = "LOAD_CONST",
    arg = is_post,
    lineno = op.lineno
  ))

  # call the receiver
  instrumented.append(Instr(
    name = "CALL_FUNCTION",
    arg = 6, # number of arguments
    lineno = op.lineno
  ))

  # ignore the receiver result
  instrumented.append(Instr(
    name = "POP_TOP",
    lineno = op.lineno
  ))

  if stacksize > 0:
    if stacksize > 1:
      # reverse the stored stack since it is unpacked right-to-left
      instrumented.append(Instr(
        name = "LOAD_GLOBAL",
        arg = "reversed",
        lineno = op.lineno
      ))

      # move the argument after the callable
      instrumented.append(Instr(
        name = "ROT_TWO",
        lineno = op.lineno
      ))

      # call the function so that the only thing left on the stack by us is the reversed list
      instrumented.append(Instr(
        name = "CALL_FUNCTION",
        arg = 1,
        lineno = op.lineno
      ))

    # and unpack the list back onto the stack
    instrumented.append(Instr(
      name = "UNPACK_SEQUENCE",
      arg = stacksize,
      lineno = op.lineno
    ))

def run_or_return_value(maybe_lambda: Union[int, Callable[[Instr], int]], input: Instr) -> int:
  if callable(maybe_lambda):
    return maybe_lambda(input)
  else:
    return maybe_lambda

def instrument_bytecode(code: Bytecode, code_id: int = 0) -> Bytecode:
  instrumented = clone_bytecode_empty_body(code)

  label_to_op_index = {}
  for i in range(len(code)):
    if isinstance(code[i], Label):
      label_to_op_index[code[i]] = i + 1

  for i in range(len(code)):
    op = code[i]

    if isinstance(op, Instr) and op.name in pre_opcode_instrument:
      emit_instrument(
        instrumented, op, i,
        run_or_return_value(pre_opcode_instrument[op.name], op),
        label_to_op_index, code_id, False
      )
    
    if isinstance(op, Instr) and op.name not in pre_opcode_instrument and op.name not in post_opcode_instrument:
      print(f"IGNORING OPERATION {op.name}")

    instrumented.append(op)

    if isinstance(op, Label):
      emit_instrument(
        instrumented, code[i + 1], i, 0, label_to_op_index, code_id, False,
        opcode="JUMP_TARGET", arg=op
      )

    if isinstance(op, Instr) and op.name in post_opcode_instrument:
      emit_instrument(
        instrumented, op, i,
        run_or_return_value(post_opcode_instrument[op.name], op),
        label_to_op_index, code_id, True
      )
  
  return instrumented

def instrument_codeobject(code: CodeType, code_id: int = 0) -> Bytecode:
  return instrument_bytecode(Bytecode.from_code(code), code_id)

def instrument_source(source: str, code_id: int) -> Bytecode:
  return instrument_codeobject(compile(source, "<string>", "exec"), code_id)
