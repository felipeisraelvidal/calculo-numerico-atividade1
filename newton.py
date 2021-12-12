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

def main():
    a = 0
    b = 2
    x0 = 1
    print('x0', x0)
    val = newton(
        f=lambda x: math.cos(x),
        g=lambda x: -math.sin(x),
        x0=x0,
        tol=10e-6,
        N=15
    )

    # a = -1
    # b = 1
    # x0 = a - b
    # val = newton(
    #     f=lambda x: x,
    #     g=lambda x: 1,
    #     x0=x0,
    #     tol=10e-6,
    #     N=100
    # )

    # x0 = 0.5
    # val = newton2(
    #     f=lambda x: x**2,
    #     g=lambda x: 2 * x,
    #     x0=x0,
    #     tol=10e-6,
    #     N=15
    # )
    
    # a = -5.5
    # b = 10.5
    # x0 = a - b
    # val = newton(
    #     f=lambda x: x**3 - (2.5 * x**2) - (2.5 * x) - 3.5,
    #     g=lambda x: (3 * x**2) - (5 * x) - 2.5,
    #     x0=x0,
    #     tol=10e-6,
    #     N=100
    # )

    # a = -1.5
    # b = -1
    # x0 = a - b
    # val = newton(
    #     f=lambda x: x**2 + (x * math.cos(2 * x)) - 3,
    #     g=lambda x: (2 * x) - (2 * x * math.sin(2 * x)) + math.cos(2 * x),
    #     x0=x0,
    #     tol=10e-6,
    #     N=100
    # )
    
    # a = 1.5
    # b = 2.5
    # x0 = a - b
    # val = newton(
    #     f=lambda x: (2 * x) + math.cos(2 * x) - ((2 * x) * math.sin(2 * x)),
    #     g=lambda x: 2 - (4 * math.sin(2 * x)) - (4 * x * math.cos(2 * x)),
    #     x0=x0,
    #     tol=10e-6,
    #     N=100
    # )



    print(val)

if __name__ == '__main__':
    main()
