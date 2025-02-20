import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

def f(x):
    return np.sqrt(1 - x**4)

x = np.linspace(0,1,5)
y = f(x)

I = trapezoid(y, x)

print(I)

#Ebba klevås