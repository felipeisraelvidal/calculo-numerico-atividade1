import unittest
from bissec import bissec
import math

class TestBissec(unittest.TestCase):

    def test_a(self):
        def f(x):
            return math.cos(x)

        val = bissec(f, 0, 2)
        
        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 1.57080)

    def test_b(self):
        def f(x):
            return x
        
        val = bissec(f, -1, 1)

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 0)

    def test_c(self):
        def f(x):
            return x**2

        # val = bissec(f, -1, 2)

        # rounded_val = float('%.5g' % val[0])

        self.assertTrue(False)

    def test_d(self):
        def f(x):
            return x**3 - (2.5 * x**2) - (2.5 * x) - 3.5

        val = bissec(f, -5.5, 10.5)

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 3.5)

    def test_e(self):
        def f(x):
            return x**2 + (x * math.cos(2 * x)) - 3

        val = bissec(f, -1.5, -1)

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, -1.3410)

    def test_f(self):
        def f(x):
            return (2 * x) + math.cos(2 * x) - ((2 * x) * math.sin(2 * x))

        # val = bissec(f, 1.5, 2.5)

        # rounded_val = float('%.5g' % val[0])

        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
