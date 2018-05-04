import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import fractions

def heat_equation(alpha_sqrd, l, f):
    """
    returns the function for the heat equation, 
    this function takes in the parms t time and x
    pos
    
    Arguments:
        alpha_sqrd {number} -- the alpha squared
        l {number} -- length of bar
        f {function} -- function f(x)
    """ 

    def b(n):
        """calculates the b(n) for the heat equation
        
        Arguments:
            n {int} -- possition in the n
        """
        return integrate.quad(lambda x : f(x) * np.sin((1 / l) * n * np.pi * x) ,0, l)[0]

    pass


def graph_heat_equation(heat_eq):
    raise NotImplementedError

def animate_heat_equation(heat_eq):
    raise NotImplementedError
    

def tests():
    l = 2
    alpha_sqrd = 2
    f = lambda x : x

    
    raise NotImplementedError

tests()