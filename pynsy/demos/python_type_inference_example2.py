def add(op1, op2):
  return op1["head"] + op2[0]


if __name__ == "__main__":
  a = add({"head": 5, 2: None}, [1, "tail"])
  b = add({"head": "a", 2: None}, ["b", None])
