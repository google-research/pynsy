import unittest
from pynsy.analyses.type_inference import *

class A:
  pass

class MyTestCase(unittest.TestCase):

  def test_list_empty(self):
    t = abstraction([])
    print(t)
    self.assertEqual(str(t), "(False, list[Any])")

  def test_list_int(self):
    t = abstraction([1, 2, 3])
    print(t)
    self.assertEqual(str(t), "(False, list[int])")

  def test_list_two(self):
    t = abstraction([1, "a", 2, "b"])
    print(t)
    self.assertEqual(str(t), "(False, list[Union[int, str]])")

  def test_list_three(self):
    t = abstraction([1, "a", 2, "b", 3, True])
    print(t)
    self.assertEqual(str(t), "(False, list[Any])")

  def test_tuple_empty(self):
    t = abstraction(())
    print(t)
    self.assertEqual(str(t), "(False, tuple[Any])")

  def test_tuple_int(self):
    t = abstraction((1, 2, 3))
    print(t)
    self.assertEqual(str(t), "(False, tuple[int,...])")

  def test_tuple_two(self):
    t = abstraction((1, "a", 2, "b"))
    print(t)
    self.assertEqual(str(t), "(False, tuple[int, str, int, str])")

  def test_tuple_three(self):
    t = abstraction((1, "a", 2, "b", 3, A()))
    print(t)
    self.assertEqual(str(t), "(False, tuple[int, str, int, str, int, A])")

  def test_set_empty(self):
    t = abstraction(set())
    print(t)
    self.assertEqual(str(t), "(False, set[Any])")

  def test_set_float(self):
    t = abstraction({1.0, 2.0, 3.0})
    print(t)
    self.assertEqual(str(t), "(False, set[float])")

  def test_set_two(self):
    t = abstraction({1, "a", 2, "b"})
    print(t)
    self.assertEqual(str(t), "(False, set[Union[int, str]])")

  def test_set_three(self):
    t = abstraction({1, "a", 2, "b", 3, b"hello"})
    print(t)
    self.assertEqual(str(t), "(False, set[Any])")

  def test_dict_empty(self):
    t = abstraction({})
    print(t)
    self.assertEqual(str(t), "(False, dict[Any, Any])")

  def test_dict_one(self):
    t = abstraction({"head": 5})
    print(t)
    self.assertEqual(str(t), "(False, dict[str, int])")

  def test_dict_two(self):
    t = abstraction({"head": 5, 2: None})
    print(t)
    self.assertEqual(str(t), "(False, dict[Union[int, str], Union[NoneType, int]])")

  def test_dict_three(self):
    t = abstraction({"head": 5, 2: "tail", False: True})
    print(t)
    self.assertEqual(str(t), "(False, dict[Any, Any])")

  def test_dicts(self):
    t = abstraction({"head": 5, "tail": [7, 8, "a", "b"], 1: 8})
    print(t)
    self.assertEqual(str(t), "(False, dict[Union[int, str], Union[int, list[Union[int, str]]]])")



if __name__ == '__main__':
  unittest.main()
