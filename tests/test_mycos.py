import math
import unittest

class TestMycos(unittest.TestCase):
    def test_mycos1(self):
        from mycos import mycos
        from math import cos

        my_cos = mycos(1)
        original_cos = cos(1)
        
        self.assertEqual(my_cos, original_cos)

if __name__ == '__main__':
    unittest.main()
