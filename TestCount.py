import unittest

from Count import Ten

class TestCount(unittest.TestCase):
  def setUp(self):
    self.res = Ten()

  def test_positive(self):
    self.assertEqual(12, self.res.summ(6, 6))

  def test_1(self):
    self.assertEqual(20, self.res.summ(10, 10))

  def test_2(self):
    self.assertEqual(0, self.res.summ(0, 0))

  def test_3(self):
    self.assertEqual(10, self.res.summ(0, 10))

  def test_4(self):
    self.assertEqual(10, self.res.summ(10, 0))

  def test_5(self):
    self.assertEqual(-1, self.res.summ(-1, 11))

  def test_6(self):
    self.assertEqual(-1, self.res.summ(11, -1))

if __name__ == "__main__":
  unittest.main()
