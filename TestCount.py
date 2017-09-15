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

  def test_7(self):
    self.assertEqual(-1, self.res.summ(0, 11))

  def test_8(self):
    self.assertEqual(-1, self.res.summ(11, 0))

  def test_9(self):
    self.assertEqual(-1, self.res.summ(-1, 10))
    
  def test_10(self):
    self.assertEqual(-1, self.res.summ(10, -1))

  def test_11(self):
    self.assertEqual(-1, self.res.summ(-5, -8))

  def test_12(self):
    self.assertEqual(-1, self.res.summ(20, 100))

  def test_13(self):
    self.assertEqual(-1, self.res.summ(20, -8))

  def test_14(self):
    self.assertEqual(-1, self.res.summ(-5, 100))
    
  def test_15(self):
    self.assertEqual(-1, self.res.summ(-5, 6))
    
  def test_16(self):
    self.assertEqual(-1, self.res.summ(6, -5))
    
  def test_17(self):
    self.assertEqual(-1, self.res.summ(6, 100))
    
  def test_18(self):
    self.assertEqual(-1, self.res.summ(100, 6))

if __name__ == "__main__":
  unittest.main()
