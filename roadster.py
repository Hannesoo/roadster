import numpy as np
from scipy import interpolate

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    a1 = 546.8
    a2 = 50.31
    a3 = 0.2584
    a4 = 0.008210
    c = a1*v**(-1) + a2 + a3*v + a4*v**2
    return c


### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    distance_km, speed_kmph = load_route(route)
    b = min(x, distance_km[-1])
    a = distance_km[0]
    h = (b - a) / n
    x_points = np.linspace(distance_km[0], b, n+1)
    fx = 1 / velocity(x_points, route)
    t = h*(np.sum(fx) - (fx[0]+ fx[-1])/2)
    return t

### PART 2B ###
def total_consumption(x, route, n):
    distance_km, speed_kmph = load_route(route)
    b = min(x, distance_km[-1])
    a = distance_km[0]
    h = (b - a) / n
    x_points = np.linspace(distance_km[0], b, n+1)
    fx = consumption(velocity(x_points, route))
    E = h*(np.sum(fx) - (fx[0]+ fx[-1])/2)
    return E

### PART 3A ###

def f(T, s, route):
    return time_to_destination(s, route, 10000000)-T

def f_prim(s, route):
    return 1/velocity(s, route)

def distance(T, route):
    distance_km, speed_kmph = load_route(route)
    s_guess = sum(speed_kmph)/len(speed_kmph) * T #start gissning s = v*t
    s_i = s_guess
    err = 10**(-3)
    while err > 10**(-4):
        s_ip1 = s_i - f(T, s_i, route)/f_prim(s_i, route)
        err = np.abs(s_ip1-s_i)
        s_i = s_ip1
    return s_i

### PART 3B ###
def g(s, C, route):
    return total_consumption(s, route, 10000000) - C

def g_prim(s, route):
    return consumption(velocity(s, route))

def reach(C, route):
    distance_km, speed_kmph = load_route(route)
    medel_v = sum(speed_kmph)/len(speed_kmph)
    s_guess = C / consumption(medel_v)      # startgissning: konsumtion per kilometer dividerat med någon form av medelkonsumption
    s_i = min(s_guess, distance_km[-2]) 
    err = 10**(-3)
    while err > 10**(-4):
        s_ip1 = s_i - g(s_i, C, route)/g_prim(s_i, route)
        s_ip1 = min(s_ip1, distance_km[-1])
        err = np.abs(s_ip1-s_i)
        s_i = s_ip1
    return s_i


if __name__ == "__main__":
    #print(reach(10000, 'speed_elsa'))
    #print(reach(10000, 'speed_anna'))
    distance_anna_05h = distance(0.5, 'speed_anna')
    distance_elsa_05h = distance(0.5, 'speed_elsa')
    reach_anna_10000Wh = reach(10000, 'speed_anna')
    reach_elsa_10000Wh = reach(10000, 'speed_elsa')
    print(f'Anna kommer {distance_anna_05h} km på 30 min.')
    print(f'Elsa kommer {distance_elsa_05h} km på 30 min.')
    print(f'Anna kommer {reach_anna_10000Wh} km med 10000Wh')   
    print(f'Elsa kommer {reach_elsa_10000Wh} km med 10000Wh')    