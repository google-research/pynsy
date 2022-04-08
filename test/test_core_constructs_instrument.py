from instrumentation.instrument_nested import extract_all_codeobjects, instrument_extracted
from .util import diff_bytecodes

from textwrap import dedent

import sys

def source_test(snapshot, source):
  root_codeobject = compile(source, "<string>", "exec")
  id_to_bytecode, code_to_id = extract_all_codeobjects(root_codeobject)
  id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

  diff_string = ""
  for code_id in id_to_bytecode.keys():
    diff_string += "\n"
    diff_string += "Code Object: " + id_to_bytecode[code_id].name + "\n"
    diff_string += diff_bytecodes(id_to_bytecode[code_id], id_to_bytecode_new_codeobjects[code_id])[0]
    diff_string += "\n"

  snapshot.assert_match(diff_string, name=str((snapshot.snapshot_counter, sys.version_info.major, sys.version_info.minor)))
  snapshot.snapshot_counter += 1

def test_load_name(snapshot):
  source_test(snapshot, dedent(
    """
    xx
    """
  ))

def test_store_name(snapshot):
  source_test(snapshot, dedent(
    """
    x = 1
    """
  ))

def test_load_attr(snapshot):
  source_test(snapshot, dedent(
    """
    x.a
    """
  ))

def test_store_attr(snapshot):
  source_test(snapshot, dedent(
    """
    x.a = 1
    """
  ))


def test_list_load(snapshot):
  source_test(snapshot, dedent(
    """
    x[1]
    """
  ))

def test_list_store(snapshot):
  source_test(snapshot, dedent(
    """
    x[1] = 1
    """
  ))

def test_for_loop(snapshot):
  source_test(snapshot, dedent(
    """
    for i in None:
      pass
    """
  ))

def test_while_loop(snapshot):
  source_test(snapshot, dedent(
    """
    while True:
      pass
    """
  ))

def test_function_definition(snapshot):
  source_test(snapshot, dedent(
    """
    def f():
      pass
    f()
    """
  ))

def test_inner_function(snapshot):
  source_test(snapshot, dedent(
    """
    def f():
      def g():
        pass
      g()
    f()
    """
  ))

def test_nonlocal_ref(snapshot):
  source_test(snapshot, dedent(
    """
    def f():
      i = 0
      def g():
        nonlocal i
        return i
      g()
    f()
    """
  ))
