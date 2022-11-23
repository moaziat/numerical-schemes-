from mypythonlibrary import myfunctions 
import numpy as np 
import matplotlib.pyplot as plt
def f(x, y): 
    return x*y + x**2 
def g(x, y): 
    return np.cos(x + y)
X, Y = np.meshgrid(np.linspace(-10, 10), np.linspace(-10, 10))


if __name__ == "__main__":
   
    ds = 0.01
    P_fg_ =  myfunctions.poisson_brackets(f, g, X, Y)

    plt.pcolor(X, Y, P_fg_)
    plt.show()