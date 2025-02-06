import numpy as np
import roadster

n = 151

distance_km_anna, speed_kmph_anna = roadster.load_route('speed_anna')
distance_km_elsa, speed_kmph_elsa = roadster.load_route('speed_elsa')

anna_h = roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', n)
elsa_h = roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', n)
anna_2h = roadster.time_to_destination(distance_km_anna[-1], 'speed_anna', n//2)
elsa_2h = roadster.time_to_destination(distance_km_elsa[-1], 'speed_elsa', n//2)

# feluppskattning med tredjedelsregeln
fel_anna = (anna_2h - anna_h) / 3
fel_elsa = (elsa_2h - elsa_h) / 3

print(f'Felet för Anna med {n} delintervall är: {fel_anna*60} min')
print(f'Felet för Elsa med {n} delintervall är: {fel_elsa*60} min')


# tar in route och en tolerans i minuter. börjar med n intervall
def feluppskattning(route, tol, n):  
    distance_km, _ = roadster.load_route(route)
    fel_h = roadster.time_to_destination(distance_km[-1], route, n)
    fel_2h = roadster.time_to_destination(distance_km[-1], route, n//2)
    fel = (fel_2h - fel_h) / 3
    if fel*60 <= tol:
        print(f'{n} st intervall räkte för att få felet mindre än {tol} minuter')
        return None
    else:
        feluppskattning(route, tol, n+1)


if __name__ == '__main__':
    feluppskattning('speed_anna', 1, 100)
    feluppskattning('speed_elsa', 1, 100)