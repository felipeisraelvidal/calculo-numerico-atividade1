import unittest
from newton import newton
import math

class TestNewton(unittest.TestCase):

    def test_a(self):
        a = 0
        b = 2
        x0 = 1
        val = newton(
            f=lambda x: math.cos(x),
            g=lambda x: -math.sin(x),
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3a.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 1.57080)

    def test_b(self):
        a = -1
        b = 1
        x0 = 1
        val = newton(
            f=lambda x: x,
            g=lambda x: 1,
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3b.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 0)

    def test_c(self):
        a = -1
        b = 2
        x0 = 0.5
        val = newton(
            f=lambda x: x**2,
            g=lambda x: 2 * x,
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3c.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 0.0019531)

    def test_d(self):
        a = -5.5
        b = 10.5
        x0 = -1
        val = newton(
            f=lambda x: x**3 - (2.5 * x**2) - (2.5 * x) - 3.5,
            g=lambda x: (3 * x**2) - (5 * x) - 2.5,
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3d.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 3.5)

    def test_e(self):
        a = -1.5
        b = -1
        x0 = -1
        val = newton(
            f=lambda x: x**2 + (x * math.cos(2 * x)) - 3,
            g=lambda x: (2 * x) - (2 * x * math.sin(2 * x)) + math.cos(2 * x),
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3e.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, -1.3410)

    def test_f(self):
        a = 1.5
        b = 2.5
        x0 = 2
        val = newton(
            f=lambda x: (2 * x) + math.cos(2 * x) - ((2 * x) * math.sin(2 * x)),
            g=lambda x: 2 - (4 * math.sin(2 * x)) - (4 * x * math.cos(2 * x)),
            x0=x0,
            tol=10e-6,
            N=100,
            filename='3f.png'
        )

        rounded_val = float('%.5g' % val[0])

        self.assertEqual(rounded_val, 1.1848)

if __name__ == '__main__':
    unittest.main()
