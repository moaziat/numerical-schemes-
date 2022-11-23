import numpy as np



#finite difference scheme

def diffx_nd(f, x, y, ds): 
    return (f(x + ds/2, y) - f(x - ds/2, y))/ds
def diffy_nd(f, x, y, ds): 
    return (f(x , y) + ds/2 - f(x,  y- ds/2,))/ds

"""
Poisson brackets of two fields f and g, in preference 
the two fields be two non-linear functions 
{f, g} = df_x * dg_y - df_y * dg_x 
The two fields are functions of two variables 

"""
def poisson_brackets(f, g, x, y):
     return (diffx_nd(f, x, y, ds) * diffy_nd(g, x, y, ds)) - (diffx_nd(g, x, y, ds) * diffy_nd(f, x, y, ds))
