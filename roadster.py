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
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')


if __name__ == "__main__":
    #print(time_to_destination(70, 'speed_anna', 100))
    #print(time_to_destination(69, 'speed_elsa', 100))
    #print(total_consumption(70, 'speed_anna', 100))
    pass