import logging
from types import CodeType
from typing import cast

from bytecode import Bytecode
from bytecode import Instr
from bytecode import Label

from .util import clone_bytecode_empty_body

# Mappings from op to the size of the stack to report

binary_ops = {
    "BINARY_POWER": 2,
    "BINARY_MULTIPLY": 2,
    "BINARY_MATRIX_MULTIPLY": 2,
    "BINARY_FLOOR_DIVIDE": 2,
    "BINARY_TRUE_DIVIDE": 2,
    "BINARY_MODULO": 2,
    "BINARY_ADD": 2,
    "BINARY_SUBTRACT": 2,
    "BINARY_SUBSCR": 2,
    "BINARY_LSHIFT": 2,
    "BINARY_RSHIFT": 2,
    "BINARY_AND": 2,
    "BINARY_XOR": 2,
    "BINARY_OR": 2,

    "COMPARE_OP": 2,

    "INPLACE_POWER": 2,
    "INPLACE_MULTIPLY": 2,
    "INPLACE_MATRIX_MULTIPLY": 2,
    "INPLACE_FLOOR_DIVIDE": 2,
    "INPLACE_TRUE_DIVIDE": 2,
    "INPLACE_MODULO": 2,
    "INPLACE_ADD": 2,
    "INPLACE_SUBTRACT": 2,
    "INPLACE_LSHIFT": 2,
    "INPLACE_RSHIFT": 2,
    "INPLACE_AND": 2,
    "INPLACE_XOR": 2,
    "INPLACE_OR": 2,

    "MAKE_FUNCTION": 2,
}

unary_ops = {
    "UNARY_POSITIVE": 1,
    "UNARY_NEGATIVE": 1,
    "UNARY_NOT": 1,
    "UNARY_INVERT": 1,
    "GET_ITER": 1,
    "GET_YIELD_FROM_ITER": 1
}

pre_instrumented_ops = {
    "UNARY_POSITIVE": 1,
    "UNARY_NEGATIVE": 1,
    "UNARY_NOT": 1,
    "UNARY_INVERT": 1,
    "GET_ITER": 1,
    "GET_YIELD_FROM_ITER": 1,

    "BINARY_POWER": 2,
    "BINARY_MULTIPLY": 2,
    "BINARY_MATRIX_MULTIPLY": 2,
    "BINARY_FLOOR_DIVIDE": 2,
    "BINARY_TRUE_DIVIDE": 2,
    "BINARY_MODULO": 2,
    "BINARY_ADD": 2,
    "BINARY_SUBTRACT": 2,
    "BINARY_SUBSCR": 2,
    "BINARY_LSHIFT": 2,
    "BINARY_RSHIFT": 2,
    "BINARY_AND": 2,
    "BINARY_XOR": 2,
    "BINARY_OR": 2,

    "LOAD_ATTR": 1,

    "COMPARE_OP": 2,

    "INPLACE_POWER": 2,
    "INPLACE_MULTIPLY": 2,
    "INPLACE_MATRIX_MULTIPLY": 2,
    "INPLACE_FLOOR_DIVIDE": 2,
    "INPLACE_TRUE_DIVIDE": 2,
    "INPLACE_MODULO": 2,
    "INPLACE_ADD": 2,
    "INPLACE_SUBTRACT": 2,
    "INPLACE_LSHIFT": 2,
    "INPLACE_RSHIFT": 2,
    "INPLACE_AND": 2,
    "INPLACE_XOR": 2,
    "INPLACE_OR": 2,

    "MAKE_FUNCTION": 2,

    "SETUP_LOOP": 0,

    "STORE_NAME": 1,
    "STORE_FAST": 1,
    "STORE_DEREF": 1,
    "STORE_ATTR": 2,
    "STORE_SUBSCR": 3,
    "STORE_GLOBAL": 1,

    "POP_TOP": 1,
    "POP_JUMP_IF_TRUE": 1,
    "POP_JUMP_IF_FALSE": 1,
    "ROT_TWO": 2,

    "CALL_FUNCTION": -1,
    "CALL_METHOD": -1,
    "CALL_FUNCTION_KW": -1,
    "RETURN_VALUE": 1,
}

post_instrumented_ops = {
    "UNARY_POSITIVE": 1,
    "UNARY_NEGATIVE": 1,
    "UNARY_NOT": 1,
    "UNARY_INVERT": 1,
    "GET_ITER": 1,
    "GET_YIELD_FROM_ITER": 1,

    "BINARY_POWER": 1,
    "BINARY_MULTIPLY": 1,
    "BINARY_MATRIX_MULTIPLY": 1,
    "BINARY_FLOOR_DIVIDE": 1,
    "BINARY_TRUE_DIVIDE": 1,
    "BINARY_MODULO": 1,
    "BINARY_ADD": 1,
    "BINARY_SUBTRACT": 1,
    "BINARY_SUBSCR": 1,
    "BINARY_LSHIFT": 1,
    "BINARY_RSHIFT": 1,
    "BINARY_AND": 1,
    "BINARY_XOR": 1,
    "BINARY_OR": 1,

    "COMPARE_OP": 1,

    "INPLACE_POWER": 1,
    "INPLACE_MULTIPLY": 1,
    "INPLACE_MATRIX_MULTIPLY": 1,
    "INPLACE_FLOOR_DIVIDE": 1,
    "INPLACE_TRUE_DIVIDE": 1,
    "INPLACE_MODULO": 1,
    "INPLACE_ADD": 1,
    "INPLACE_SUBTRACT": 1,
    "INPLACE_LSHIFT": 1,
    "INPLACE_RSHIFT": 1,
    "INPLACE_AND": 1,
    "INPLACE_XOR": 1,
    "INPLACE_OR": 1,

    "MAKE_FUNCTION": 1,

    "LOAD_NAME": 1,
    "LOAD_FAST": 1,
    "LOAD_DEREF": 1,
    "LOAD_CLOSURE": 1,
    "LOAD_ATTR": 1,
    "LOAD_CONST": 1,
    "LOAD_GLOBAL": 1,

    "CALL_FUNCTION": 1,
    "CALL_FUNCTION_KW": 1,
    "CALL_METHOD": 1
}


def emit_instrument(
    instrumented: Bytecode,
    instr: Instr, instruction_id: int, stacksize: int,
    method_id: int, is_post: bool
) -> None:

  if stacksize > 0:
    instrumented.append(Instr(
        name="BUILD_LIST",
        arg=stacksize,
        lineno=instr.lineno
    ))

    # make a copy to send to the receiver
    instrumented.append(Instr(
        name="DUP_TOP",
        lineno=instr.lineno
    ))

  # load the receiver
  instrumented.append(Instr(
      name="LOAD_GLOBAL",
      arg="pynsy_receiver",
      lineno=instr.lineno
  ))

  if stacksize > 0:
    instrumented.append(Instr(
        name="ROT_TWO",
        lineno=instr.lineno
    ))
  else:
    instrumented.append(Instr(
        name="BUILD_LIST",
        arg=stacksize,
        lineno=instr.lineno
    ))


  instrumented.append(Instr(
      name="LOAD_CONST",
      arg=instruction_id,
      lineno=instr.lineno
  ))

  instrumented.append(Instr(
      name="LOAD_CONST",
      arg=method_id,
      lineno=instr.lineno
  ))

  instrumented.append(Instr(
      name="LOAD_CONST",
      arg=is_post,
      lineno=instr.lineno
  ))

  # call the receiver
  instrumented.append(Instr(
      name="CALL_FUNCTION",
      arg=4,  # number of arguments # careful.  Change it if you change the arguments being passed above
      lineno=instr.lineno
  ))

  # ignore the receiver result
  instrumented.append(Instr(
      name="POP_TOP",
      lineno=instr.lineno
  ))

  if stacksize > 1:
    # reverse the stored stack since it is unpacked right-to-left
    instrumented.append(Instr(
        name="LOAD_GLOBAL",
        arg="reversed",
        lineno=instr.lineno
    ))

    # move the argument after the callable
    instrumented.append(Instr(
        name="ROT_TWO",
        lineno=instr.lineno
    ))

    # call the function so that the only thing left on the stack by us is the reversed list
    instrumented.append(Instr(
        name="CALL_FUNCTION",
        arg=1,
        lineno=instr.lineno
    ))

  # and unpack the list back onto the stack
  if stacksize > 0:
    instrumented.append(Instr(
        name="UNPACK_SEQUENCE",
        arg=stacksize,
        lineno=instr.lineno
    ))


def get_args_num(n_operands: int, input: Instr) -> int:
  if n_operands < 0:
    return cast(int, input.arg) + 1
  else:
    return n_operands


def instrument_bytecode(byte_code: Bytecode, method_id: int = 0) -> Bytecode:
  instrumented_byte_code = clone_bytecode_empty_body(byte_code)

  label_to_op_index = {}
  for instruction_id in range(len(byte_code)):
    if isinstance(byte_code[instruction_id], Label):
      label_to_op_index[byte_code[instruction_id]] = instruction_id + 1

  for instruction_id in range(len(byte_code)):
    instr = byte_code[instruction_id]

    if isinstance(instr, Instr) and instr.name in pre_instrumented_ops:
      emit_instrument(
          instrumented_byte_code, instr, instruction_id,
          get_args_num(pre_instrumented_ops[instr.name], instr),
          method_id, False
      )

    if isinstance(instr, Instr) and instr.name == "LOAD_CLOSURE":
      print(instr.name)

    if isinstance(instr, Instr) \
        and instr.name not in pre_instrumented_ops \
        and instr.name not in post_instrumented_ops:
      pass
      logging.warning(f"IGNORING OPERATION {instr.name}")

    instrumented_byte_code.append(instr)

    if isinstance(instr, Label):
      emit_instrument(
          instrumented_byte_code, byte_code[instruction_id + 1], instruction_id,
          0, method_id, True
      )

    if isinstance(instr, Instr) and instr.name in post_instrumented_ops:
      emit_instrument(
          instrumented_byte_code, instr, instruction_id,
          get_args_num(post_instrumented_ops[instr.name], instr),
          method_id, True
      )

  return instrumented_byte_code


def instrument_codeobject(code: CodeType, method_id: int = 0) -> Bytecode:
  return instrument_bytecode(Bytecode.from_code(code), method_id)


def instrument_source(source: str, method_id: int) -> Bytecode:
  return instrument_codeobject(compile(source, "<string>", "exec"), method_id)
