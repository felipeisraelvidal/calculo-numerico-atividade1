import math
import matplotlib.pyplot as plt

def newton(f, g, x0, tol, N):
    step = 1
    flag = 1
    condition = True
    iters = []
    res = []
    while condition:
        if g(x0) == 0:
            print('Error')
            break

        x1 = x0 - f(x0)/g(x0)
        print(f'Iteration {step}:')
        print(x1, f(x1))

        # Calculate the error
        error = abs(x1 - x0)
        print(f'Error: {error}')

        iters.append(step)
        res.append(error)

        if step > N:
            flag = 0
            break

        x0 = x1
        step += 1

        condition = abs(f(x1)) > tol

    if flag == 1:
        print('------------------')
        print('Found a root:')
        print(x1, f(x1))
        print('------------------')
        
        plt.plot(iters, res)
        plt.xlabel('Iterations')
        plt.ylabel('Error')
        plt.show()

        return (x1, f(x1), step, res)
    else:
        print('Não converge')
