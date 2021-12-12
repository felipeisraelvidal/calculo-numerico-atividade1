import unittest
from newton import newton
import math

class TestBissec(unittest.TestCase):

    def test_a(self):
        def f(x):
            return math.cos(x)

        def g(f):
            print('calc d\'')

        val = newton(f, 0, 2)

        self.assertTrue(False)

    def test_b(self):
        def f(x):
            return x
        
        val = newton(f, -1, 1)

        self.assertTrue(False)

    def test_c(self):
        def f(x):
            return x**2

        val = newton(f, -1, 2)

        self.assertTrue(False)

    def test_d(self):
        def f(x):
            return x**3 - (2.5 * x**2) - (2.5 * x) - 3.5

        val = newton(f, -5.5, 10.5)

        self.assertTrue(False)

    def test_e(self):
        def f(x):
            return x**2 + (x * math.cos(2 * x)) - 3

        val = newton(f, -1.5, -1)

        val = newton(f, -1.5, -1)

    def test_f(self):
        def f(x):
            return (2 * x) + math.cos(2 * x) - ((2 * x) * math.sin(2 * x))

        val = newton(f, 1.5, 2.5)

        val = newton(f, -1.5, -1)

if __name__ == '__main__':
    unittest.main()
