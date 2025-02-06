import roadster
import matplotlib.pyplot as plt
import numpy as np

data = 'speed_anna'

distance_km, speed_kmph = roadster.load_route(data)
print(distance_km)

x = np.linspace(0, int(distance_km[-1]), 10000)
v = roadster.velocity(x, data) 


plt.plot(distance_km, speed_kmph, 'm.', label = 'hastighetsmätningar')
plt.plot(x,v, 'c', label = 'interpolerad hastighet')
plt.ylabel('[km/h]')
plt.xlabel('[km]')
plt.legend()
plt.savefig('kmph_km_10000_anna.png')
plt.show() 