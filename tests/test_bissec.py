import unittest
from bissec import bissec
import math

class TestBissec(unittest.TestCase):

    def test_a(self):
        val = bissec(lambda x: math.cos(x), 0, 2, filename='2a.png')
        
        rounded_val = float('%.5g' % val)

        self.assertEqual(rounded_val, 1.57080)

    def test_b(self):
        val = bissec(lambda x: x, -1, 1, filename='2b.png')

        rounded_val = float('%.5g' % val)

        self.assertEqual(rounded_val, 0)

    def test_c(self):
        val = bissec(lambda x: x**2, -1, 2, filename='2c.png')

        self.assertIsNone(val)

    def test_d(self):
        val = bissec(lambda x: x**3 - (2.5 * x**2) - (2.5 * x) - 3.5, -5.5, 10.5, filename='2d.png')

        rounded_val = float('%.5g' % val)

        self.assertEqual(rounded_val, 3.5)

    def test_e(self):
        val = bissec(lambda x: x**2 + (x * math.cos(2 * x)) - 3, -1.5, -1, filename='2e.png')

        rounded_val = float('%.5g' % val)

        self.assertEqual(rounded_val, -1.3410)

    def test_f(self):
        val = bissec(lambda x: (2 * x) + math.cos(2 * x) - ((2 * x) * math.sin(2 * x)), 1.5, 2.5, filename='2f.png')

        self.assertIsNone(val)

if __name__ == '__main__':
    unittest.main()
