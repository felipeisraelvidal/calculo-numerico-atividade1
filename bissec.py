import math

def bissec(f, a, b, tol=10e-6):
    """
    f: callback
    a, b: interval
    tol: tolerance
    """

    criteria = abs(b - a) > tol

    fa = f(a)

    x_arr = []
    y_arr = []

    while criteria:
        p = (a + b) / 2
        fp = f(p)

        x_arr.append(p)
        y_arr.append(fp)

        if fp == 0 or abs(fp) < ((b - a) / 2) < tol:
            return (p, x_arr, y_arr)
        
        if (fa * fp) > 0:
            a = p
            fa = fp
        else:
            b = p

    raise ValueError("No root found")

def f(x):
    return x**2

def main():
    val = bissec(f, -1, 2)
    print(val)

if __name__ == '__main__':
    main()
