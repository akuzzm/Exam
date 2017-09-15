import unittest

from Count import Ten

class TestCount(unittest.TestCase):
  def setUp(self):
    self.res = Ten()
    
  def test_positive(self):
    self.assertEqual(12, self.res.summ(6, 6))
    
  def test_negative(self):
    self.assertNotEqual(-1, self.res.summ(12, 15))
    
if__name__ == "__main__":
  unittest.main()
