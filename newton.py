import matplotlib.pyplot as plt

def newton(f, g, x0, tol=10e-6, N=100, filename=None):
    iteration = 1
    found_root = True
    
    condition = True
    
    iters = []
    res = []

    while condition:
        if g(x0) == 0:
            break

        x1 = x0 - f(x0)/g(x0)

        print(f'Iteration {iteration}:')
        print(x1, f(x1))

        # Calculate the error
        error = abs(x1 - x0)
        print(f'Error: {error}')

        iters.append(iteration)
        res.append(error)

        if iteration > N:
            found_root = False
            break

        x0 = x1
        iteration += 1

        condition = abs(f(x1)) > tol

    if found_root == True:
        print('------------------')
        print('Found a root:')
        print(x1, f(x1))
        print('------------------')

        plt.close()
        
        plt.plot(iters, res)
        plt.xlabel('Iterations')
        plt.ylabel('Error')

        if filename:
            plt.savefig(f'dist/{filename}')
        else:
            plt.show()

        return (x1, f(x1), iteration, res)
    else:
        print('Não converge')
