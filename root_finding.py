import numpy as np

def bisection_method(f, a, b, eps=1e-2):
    fa = f(a)
    fb = f(b)
    if np.sign(fa) == np.sign(fb):
        raise Exception("The scalars a and b do not bound a root")

    m = (a +  b) / 2
    fm = f(m)
    
    if np.abs(fm) < eps:
        return m
    elif np.sign(fa) == np.sign(fm):
        return bisection_method(f, m, b, eps)
    else:
        return bisection_method(f, a, m, eps)