import roadster
import matplotlib.pyplot as plt
import numpy as np

distance_km_anna, speed_kmph_anna = roadster.load_route('speed_anna')
distance_km_elsa, speed_kmph_elsa = roadster.load_route('speed_elsa')

n_exakt = 10000000      # antar att detta värde ger det exakt värde

anna_exakt_t = roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', n_exakt)
elsa_exakt_t = roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', n_exakt)

anna_exakt_e = roadster.total_consumption(distance_km_anna[-1], 'speed_anna', n_exakt)
elsa_exakt_e = roadster.total_consumption(distance_km_elsa[-1], 'speed_elsa', n_exakt)


n = [2**x for x in range(21)]

times = [roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', x) for x in n]
fel_time = [abs(x - anna_exakt_t) for x in times] 

times_2 = [roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', x) for x in n]
fel_time_2 = [abs(x - elsa_exakt_t) for x in times_2] 

counsumtions = [roadster.total_consumption(distance_km_anna[-1], 'speed_anna', x) for x in n]
fel_e = [abs(x - anna_exakt_e) for x in counsumtions] 

counsumtions_2 = [roadster.total_consumption(distance_km_elsa[-1], 'speed_elsa', x) for x in n]
fel_e_2 = [abs(x - elsa_exakt_e) for x in counsumtions_2] 


c = fel_time[0] - 1
c_t_a = fel_time[-1] * n[-1]**2 
c_e_a = fel_e[-1] * n[-1]**2
# Hjälplinjer för annas tid
x_no_1 = np.array([1, 2**15])
y_no_1 = (1 / np.power(x_no_1, 1))
#
x_no_2_a_t = np.array([1, 2**15])
y_no_2_a_t = c_t_a * (1 / np.power(x_no_2_a_t, 2))
#
x_no_3 = np.array([1, 2**10])
y_no_3 = (1 / np.power(x_no_3, 3))
# ----------------
# Hjälplinjer för annas konsumtion
x_no_2_a_e = np.array([1, 2**15])
y_no_2_a_e = c_e_a * (1 / np.power(x_no_2_a_e, 2))


#plt.loglog(x, fel)
plt.loglog(n, fel_time, label='fel för annas tid')
plt.loglog(n, fel_e, label='fel för annas konsumtion')
plt.loglog(n, fel_time_2, label='fel för elsas tid')
plt.loglog(n, fel_e_2, label='fel för elsas konsumtion')
plt.loglog(x_no_2_a_e, y_no_2_a_e, '--', label='$1/n^2$')
plt.loglog(x_no_1, y_no_1, '--', label='1/n')
plt.loglog(x_no_2_a_t, y_no_2_a_t, '--', label='$1/n^2$')
plt.loglog(x_no_3, y_no_3, '--', label='$1/n^3$')
plt.ylabel('absolut fel')
plt.xlabel('n (antal intervall)')
plt.legend()
#plt.savefig('konvergensstudie.png')
plt.show()   