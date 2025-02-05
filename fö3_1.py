import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

g = 9.81
m = 80
c = 12

def v(t, g, m, c):
    return g*m/c*(1-np.exp(-c*t/m))

def s(t, g, m, c):
    s_val, err = quad(v, 0, t, args=(g,m,c))
    return s_val

t_array = np.linspace(0, 10, 201)
v_array = v(t_array, g, m, c)

plt.plot(t_array, v_array)
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')
plt.show()

s_array = 0*t_array

# compute s for different t
for i in range(len(t_array)):
    s_array[i] = s(t_array[i], g, m, c)

plt.plot(t_array, s_array)
plt.xlabel('t (s)')
plt.ylabel('s (m)')
plt.show()