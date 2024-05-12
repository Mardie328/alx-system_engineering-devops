import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 1, 1]), 4, "should be 3")


if __name__=="__main__":
    unittest.main()