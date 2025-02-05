import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

g = 9.81
c = 12
t = 10

def v(t, g, m, c):
    return g*m/c*(1-np.exp(-c*t/m))

def s(t, g, m, c):
    s_val, err = quad(v, 0, t, args=(g,m,c))
    return s_val

m_array = np.linspace(40, 100, 201)
s_array = np.zeros(m_array.size)

for i, m in enumerate(m_array):
    s_array[i] = s(t, g, m, c)

plt.plot(m_array, s_array)
plt.xlabel('m (kg)')
plt.ylabel('s (m)')
plt.show()