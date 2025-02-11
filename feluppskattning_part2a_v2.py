import numpy as np
import roadster

distance_km_anna, speed_kmph_anna = roadster.load_route('speed_anna')
distance_km_elsa, speed_kmph_elsa = roadster.load_route('speed_elsa')

n_exakt = 10000000      # antar att detta värde ger det exakt värde

anna_exakt = roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', n_exakt)
elsa_exakt = roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', n_exakt)

def felet(route, tol, n, exakt):  
    distance_km, _ = roadster.load_route(route)
    gissning = roadster.time_to_destination(distance_km[-1], route, n)
    fel = np.abs((gissning - exakt)) 
    if fel*60 <= tol:
        print(f'{n} st intervall räkte för att få felet mindre än {tol} minuter')
        return None
    else:
        felet(route, tol, n+1, exakt)


if __name__ == '__main__':
    felet('speed_anna', 0.5, 800, anna_exakt)
    felet('speed_elsa', 0.5, 450, elsa_exakt)
    print(np.abs(roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', 828) - anna_exakt)*60)
    print(np.abs(roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', 462) - elsa_exakt)*60)
    print(np.abs(roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', 829) - anna_exakt)*60)
    print(np.abs(roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', 463) - elsa_exakt)*60)

# alltså 829 delintervall för anna och 463 delintervall för elsa

