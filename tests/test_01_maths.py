import unittest
from my_maths import multiplyer, substractor

class TestMaths(unittest.TestCase):
    def test_multiplyer(self):
        total = multiplyer(2, 4)
        self.assertEqual(total, 8)

    def test_subtractor(self):
        total = substractor(10, 6)
        self.assertEqual(total, 4)

    def test_blah(self):
        my_list = [2, 4, 6, 8]
        my_num = multiplyer(2, 3)
        self.assertIn(my_num, my_list)

if __name__ == '__main__':
    unittest.main()
