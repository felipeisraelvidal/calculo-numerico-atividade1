import math
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def bissec(f, a, b, tol=10e-6, filename='bissec.png'):
    if f(a) * f(b) >= 0:
        return None
    
    c = a

    x_arr = []
    y_arr = []

    while abs(b - a) >= tol:
        c = (a + b) / 2
        fc = f(c)

        print(c, fc)

        x_arr.append(c)
        y_arr.append(fc)

        if f(c) == 0:
            break
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print(c)

    z = linspace(a, b, 100)
    plt.scatter(x_arr, y_arr)
    f_vec = np.vectorize(f)
    plt.plot(z, f_vec(z), 'r', linestyle='solid')
    # plt.show()
    plt.savefig(f'dist/{filename}')

    return c

def f(x):
    return x**2 + (x * math.cos(2 * x)) - 3

def main():
    bissec(f, -1.5, 1)

if __name__ == '__main__':
    main()
