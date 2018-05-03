import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

def fourier (l ,f, n_upper = 100):



    #below are the functions used to solve
    def a0():
        """the a(0) term of a, calculate seperatly because it is a simple computation and
        we can start our n at 1
        
        Returns:
            number -- the integral over the given bounds of f(x)
        """

        return integrate.quad(f, -1 * l, l)[0]
    
    def a(n):
        """the a(n) term of a, calculate using f(x) * cos(pi*n*x / l)
        
        Arguments:
            n {int} -- the nth term
        
        Returns:
            number -- the integral over the given bounds of f(x) * cos(pi*n*x / l)
        """

        return integrate.quad(lambda x : f(x) * np.cos(n * np.pi * x / l), -1 * l, l)[0]
    
    def b(n):
        """the b(n) term of a, calculate using f(x) * sin(pi*n*x / l)
        
        Arguments:
            n {int} -- the nth term
        
        Returns:
            number -- the integral over the given bounds of f(x) * sin(pi*n*x / l)
        """
        return integrate.quad(lambda x : f(x) * np.sin(n * np.pi * x / l), -1 * l, l)[0]

    def _sum_func(func_list, var):
        total = 0
        for f in func_list:
            total += f(var)
        return total
            

    #------------------------------------------------------------------------------------------#
    """
    Returns the fourier function
    
    Returns:
        function -- the fourier function
    """
    list_fourier_sum = [lambda x : a(n) * np.cos(n * np.pi * x / l) + b(n) * 
        np.sin(n * np.pi * x / l) for n in range(1 , n_upper)]

    fourier_func = lambda x: a0() / 2 + _sum_func(list_fourier_sum, x)

    
    return fourier_func


#tests
func = fourier(1, lambda x: (abs(x) + x) / 2)

print(func(-1))
print(func(0))
print(func(.5))
print(func(1))