import math
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def bissec(f, a, b, tol=10e-6, filename=None):
    if f(a) * f(b) >= 0:
        return None
    
    c = a

    x_arr = []
    y_arr = []

    spaced_num = linspace(a, b, 50)

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

    f_vec = np.vectorize(f)
    
    plt.scatter(x_arr, y_arr)
    plt.plot(spaced_num, f_vec(spaced_num))

    if filename:
        plt.savefig(f'dist/{filename}')
    else:
        plt.show()

    return c

def f(x):
    return x**2 + (x * math.cos(2 * x)) - 3

def main():
    bissec(f, -1.5, 1)

if __name__ == '__main__':
    main()
