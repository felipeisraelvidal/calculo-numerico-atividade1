import sys
import math

def mycos(x, iterations = 10):
    """
    cos(x)
    """

    print(iterations)

    sum = 1

    k = 1
    while k < iterations:
        term = x**(2 * k) / math.factorial(2 * k)
        signal = math.pow(-1, k)
        sum += signal * term
        
        print(f'Iteration {k}')
        print(sum)

        if sum == math.cos(x):
            break
        
        k += 1

    return sum

if __name__ == '__main__':
    x = int(sys.argv[1])
    iterations = int(sys.argv[2])

    cos = mycos(x, iterations)
    print(f'mycos({x}): ', cos)

    original_cos = math.cos(x)
    print(f'  cos({x}): ', original_cos)

    print(f'difference: ', original_cos - cos)
