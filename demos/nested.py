a = 1


def f():
  b = 3

  def g():
    c = 2
    nonlocal b
    global a
    print(b)
    b = 4
    print(b)
    print(a)
    print(c)

  print(b)
  return g


f()()
