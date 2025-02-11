import numpy as np
import roadster

distance_km_anna, speed_kmph_anna = roadster.load_route('speed_anna')
distance_km_elsa, speed_kmph_elsa = roadster.load_route('speed_elsa')

n_exakt = 10000000      # antar att detta värde ger det exakt värde

anna_exakt = roadster.total_consumption(distance_km_anna[-1], 'speed_anna', n_exakt)
elsa_exakt = roadster.total_consumption(distance_km_elsa[-1], 'speed_elsa', n_exakt)

def felet(route, tol, n, exakt):  
    distance_km, _ = roadster.load_route(route)
    gissning = roadster.total_consumption(distance_km[-1], route, n)
    fel = np.abs((gissning - exakt)) 
    if np.abs(fel) <= tol:
        print(f'{n} st intervall räkte för att få felet mindre än {tol} minuter')
        return None
    else:
        felet(route, tol, n+1, exakt)


if __name__ == '__main__':
    print(anna_exakt)
    print(elsa_exakt)
    felet('speed_anna', 0.5, 1000, anna_exakt)
    felet('speed_elsa', 0.5, 1000, elsa_exakt)
    print(np.abs(roadster.total_consumption(distance_km_anna[-1], 'speed_anna', 1552) - anna_exakt))
    print(np.abs(roadster.total_consumption(distance_km_elsa[-1], 'speed_elsa', 1062) - elsa_exakt))
    print(np.abs(roadster.total_consumption(distance_km_anna[-1], 'speed_anna', 1553) - anna_exakt))
    print(np.abs(roadster.total_consumption(distance_km_elsa[-1], 'speed_elsa', 1063) - elsa_exakt))

# Alltså krävdes 1553 interval för anna och 1063 intervall för elsa.

