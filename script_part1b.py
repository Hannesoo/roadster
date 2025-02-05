import roadster
import matplotlib.pyplot as plt
import numpy as np

data = 'speed_elsa'

distance_km, speed_kmph = roadster.load_route(data)
print(distance_km)

x = np.linspace(0, int(distance_km[-1]), 10000)
v = roadster.velocity(x, data) 


plt.plot(distance_km, speed_kmph, 'm.', label = 'data points')
plt.plot(x,v, 'c', label = 'velocity graph')
plt.ylabel('speed [km/h]')
plt.xlabel('distance [km]')
plt.legend()

plt.show() 