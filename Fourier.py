import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def fourier (l ,f, n_upper = 100):
    """gets the fourier series of an expression
    
    Arguments:
        l {number} -- length
        f {function} -- specific function we are looking at
    
    Keyword Arguments:
        n_upper {int} -- value of n, a number that will be sumed over from 0 to n_upper
                         should aproach infinity (default: {100})
    """

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

        return integrate.quad(lambda x : f(x) * np.cos((n * np.pi * x) / l), -1.0 * l, l)[0]
    
    def b(n):
        """the b(n) term of a, calculate using f(x) * sin(pi*n*x / l)
        
        Arguments:
            n {int} -- the nth term
        
        Returns:
            number -- the integral over the given bounds of f(x) * sin(pi*n*x / l)
        """
        return integrate.quad(lambda x : f(x) * np.sin((n * np.pi * x) / l), -1.0 * l, l)[0]

    def _sum_func(func_list, var):
        total = 0.0
        for f in func_list:
            total += f(var)
        return total
            

    #------------------------------------------------------------------------------------------#
    """
    Returns the fourier function
    
    Returns:
        function -- the fourier function
    """
    list_fourier_sum = (lambda x : a(n) * np.cos((n * np.pi * x) / l) + b(n) * 
        np.sin((n * np.pi * x) / l) for n in range(1 , n_upper + 1))

    fourier_func = lambda x : a0() / 2.0 + _sum_func(list_fourier_sum, x)
    return fourier_func


def graph(func, l):
    x = np.arange(-1.0 * l, l, 0.01)
    plt.plot(x, func(x))
    plt.show()


def graph_ns(func, l, n_lower, n_high, save=False):
    x = np.arange(-1 * l, l, .01)
    fig, ax = plt.subplots()
    line, = ax.plot(x, fourier (l, func, n_high)(x))
       

    def init():
        line.set_data([],[])
        return line,

    def animate(n):
        fourier_func = fourier(l, func, n + n_lower)
        line.set_data(x,fourier_func(x))
        return line,
    anim = animation.FuncAnimation(fig, animate, init_func=init,  interval=1, frames=n_high - n_lower, blit=True )
    if save:
        # Set up formatting for the movie files
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        anim.save('sim.mp4', writer=writer)
    plt.show()
        

def tests(l, f, n_low=1, n_high=30):
    #tests
    #if you wanna modify the testing, the lambda exquation is what is passed, and the length is the first param
    #the last param is the upper bound of n
    func = fourier(l, f, n_high)
    graph(func,l)

    graph_ns(f, l, n_low, n_high, save=False)

tests(1, lambda x: np.cos(1/x) if x != 0 else 0)
