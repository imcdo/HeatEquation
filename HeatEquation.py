import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import fractions

def _multi_sum(iter_func, *var):
    total = 0
    for func in iter_func:
        total += func(*var)
    return total

def heat_equation(alpha_sqrd, l, f, n_upper=100):
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
        return (2/l) * integrate.quad(lambda x : f(x) * np.sin(n * np.pi * x / l) ,0, l)[0]

    base_func = lambda x, t, n : b(n) * np.sin(n * np.pi * x / l) * np.e ** (-1 * alpha_sqrd * (np.pi ** 2) * (n ** 2)  * t / (l ** 2))
    return lambda x, t : _multi_sum((lambda x, t :base_func(x, t, n) for n in range(1, n_upper, 2)), x, t)

def graph_heat_equation_t(alpha_sqrd, l, f, t=0):
    x = np.arange(0, l, .01)
    y = heat_equation(alpha_sqrd, l, f)(x, t)
    plt.plot(x, y)

def animate_heat_equation(heat_eq):
    raise NotImplementedError
    

def tests():
    l = 2
    alpha_sqrd = 2
    
    f = lambda x : x ** 2
    #graph the original func
    domain = np.arange(0, l, .01)
    plt.plot(domain, f(domain), color="red")

    graph_heat_equation_t(alpha_sqrd, l, f)

    graph_heat_equation_t(alpha_sqrd, l, f, t=.001)
    graph_heat_equation_t(alpha_sqrd, l, f, t=.01)
    plt.show()
tests()