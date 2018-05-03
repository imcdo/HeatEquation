import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

def fourier (l ,f):


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

