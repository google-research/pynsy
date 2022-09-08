from .test_core_constructs_exec import source_test
from textwrap import dedent

def test_nested_iteration(snapshot):
  source_test(snapshot, dedent(
    """
    def myFunc():
      x = -1
      data = list(range(5))
      for i in data:
        if i == 3:
          break
        else:
          while i > 0:
            x += i
            i -= 1
    myFunc()
    """
  ))

def test_factorial(snapshot):
  source_test(snapshot, dedent(
    """
    def factorial(i):
      if i == 0:
        return 1
      else:
        return i * factorial(i - 1)

    factorial(5)
    """
  ))

def test_list_map(snapshot):
  source_test(snapshot, dedent(
    """
    my_arr = [1, 2, 3]
    for i in range(0, 3):
      my_arr[i] = my_arr[i] + 1
    """
  ))

def test_nonlocal_load(snapshot):
  source_test(snapshot, dedent(
    """
    def f(i):
      def g():
        nonlocal i
        return i
      g()
    f(0)
    f(1)
    """
  ))

def test_scope_forwarding_loads(snapshot):
  source_test(snapshot, dedent(
    """
    x = 1
    y = 2
    z = 3
    def f1():
      test1 = x
      w = 4
      u = 5
      def f2():
        test2 = x
        test3 = w
        u = 6
        def f3():
          test4 = x
          test5 = w
          test6 = u
        f3()
      f2()
    f1()
    """
  ))
