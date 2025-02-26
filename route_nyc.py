from scipy import interpolate
import numpy as np 
from pchip_2d import pchip_2d

N_data_t = 25
data_t = np.linspace(0, 24, N_data_t)
N_data_x = 30
data_x = np.linspace(0, 60, N_data_x)

nyc_velocity = np.array([[63.65,64.41,65.17,65.93,66.69,56.28,44.73,21.62,18.28,14.94,12.96,14.91,16.85,18.80,48.45,28.11,19.11,20.14,21.48,22.83,29.91,50.65,49.52,48.39,47.26],[63.65,64.41,65.17,65.93,66.69,56.28,44.73,21.62,18.28,14.94,12.96,14.91,16.85,18.80,48.45,28.11,19.11,20.14,21.48,22.83,29.91,50.65,49.52,48.39,47.26],[63.65,64.41,65.17,65.93,66.69,56.28,44.73,21.62,18.28,14.94,12.96,14.91,16.85,18.80,48.45,28.11,19.11,20.14,21.48,22.83,29.91,50.65,49.52,48.39,47.26],[56.01,57.61,59.22,60.83,62.44,64.05,65.66,60.06,52.38,44.71,51.62,52.61,53.60,53.00,50.80,48.60,24.11,24.38,27.03,29.69,40.97,45.47,49.98,54.48,58.98],[56.01,57.61,59.22,60.83,62.44,64.05,65.66,60.06,52.38,44.71,51.62,52.61,53.60,53.00,50.80,48.60,24.11,24.38,27.03,29.69,40.97,45.47,49.98,54.48,58.98],[56.01,57.61,59.22,60.83,62.44,64.05,65.66,60.06,52.38,44.71,51.62,52.61,53.60,53.00,50.80,48.60,24.11,24.38,27.03,29.69,40.97,45.47,49.98,54.48,58.98],[93.02,92.03,91.04,90.05,89.06,88.07,87.08,48.23,32.06,42.94,83.27,82.36,81.45,80.54,79.63,78.72,24.84,36.84,40.37,61.51,80.70,82.61,84.51,86.42,88.33],[93.02,92.03,91.04,90.05,89.06,88.07,87.08,48.23,32.06,42.94,83.27,82.36,81.45,80.54,79.63,78.72,24.84,36.84,40.37,61.51,80.70,82.61,84.51,86.42,88.33],[93.02,92.03,91.04,90.05,89.06,88.07,87.08,48.23,32.06,42.94,83.27,82.36,81.45,80.54,79.63,78.72,24.84,36.84,40.37,61.51,80.70,82.61,84.51,86.42,88.33],[93.02,92.03,91.04,90.05,89.06,88.07,87.08,48.23,32.06,42.94,83.27,82.36,81.45,80.54,79.63,78.72,24.84,36.84,40.37,61.51,80.70,82.61,84.51,86.42,88.33],[93.02,92.03,91.04,90.05,89.06,88.07,87.08,48.23,32.06,42.94,83.27,82.36,81.45,80.54,79.63,78.72,24.84,36.84,40.37,61.51,80.70,82.61,84.51,86.42,88.33],[89.19,88.63,88.07,87.51,86.95,86.39,85.82,85.26,72.68,74.12,85.75,85.60,85.45,85.30,85.15,85.01,84.78,86.53,88.28,87.70,88.49,89.28,90.07,90.87,91.66],[89.19,88.63,88.07,87.51,86.95,86.39,85.82,85.26,72.68,74.12,85.75,85.60,85.45,85.30,85.15,85.01,84.78,86.53,88.28,87.70,88.49,89.28,90.07,90.87,91.66],[89.19,88.63,88.07,87.51,86.95,86.39,85.82,85.26,72.68,74.12,85.75,85.60,85.45,85.30,85.15,85.01,84.78,86.53,88.28,87.70,88.49,89.28,90.07,90.87,91.66],[89.19,88.63,88.07,87.51,86.95,86.39,85.82,85.26,72.68,74.12,85.75,85.60,85.45,85.30,85.15,85.01,84.78,86.53,88.28,87.70,88.49,89.28,90.07,90.87,91.66],[89.19,88.63,88.07,87.51,86.95,86.39,85.82,85.26,72.68,74.12,85.75,85.60,85.45,85.30,85.15,85.01,84.78,86.53,88.28,87.70,88.49,89.28,90.07,90.87,91.66],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[107.34,106.20,105.07,103.94,102.81,101.68,100.55,99.41,98.28,97.15,96.02,94.89,93.75,101.52,101.10,100.67,100.25,99.83,99.40,71.85,98.35,99.54,100.73,101.92,103.11],[95.75,96.07,96.39,96.71,97.03,97.35,97.67,90.93,87.00,83.08,79.16,75.24,71.31,85.97,83.07,80.17,70.54,70.78,71.02,55.75,81.84,86.74,89.43,92.13,94.82],[95.75,96.07,96.39,96.71,97.03,97.35,97.67,90.93,87.00,83.08,79.16,75.24,71.31,85.97,83.07,80.17,70.54,70.78,71.02,55.75,81.84,86.74,89.43,92.13,94.82],[95.75,96.07,96.39,96.71,97.03,97.35,97.67,90.93,87.00,83.08,79.16,75.24,71.31,85.97,83.07,80.17,70.54,70.78,71.02,55.75,81.84,86.74,89.43,92.13,94.82],[95.75,96.07,96.39,96.71,97.03,97.35,97.67,90.93,87.00,83.08,79.16,75.24,71.31,85.97,83.07,80.17,70.54,70.78,71.02,55.75,81.84,86.74,89.43,92.13,94.82],[95.75,96.07,96.39,96.71,97.03,97.35,97.67,90.93,87.00,83.08,79.16,75.24,71.31,85.97,83.07,80.17,70.54,70.78,71.02,55.75,81.84,86.74,89.43,92.13,94.82],[92.51,92.75,92.98,93.21,93.45,93.68,93.91,38.26,20.18,30.66,44.79,52.12,59.44,75.90,77.95,79.99,19.20,21.49,17.97,49.28,84.90,86.84,88.79,90.73,92.67],[92.51,92.75,92.98,93.21,93.45,93.68,93.91,38.26,20.18,30.66,44.79,52.12,59.44,75.90,77.95,79.99,19.20,21.49,17.97,49.28,84.90,86.84,88.79,90.73,92.67],[92.51,92.75,92.98,93.21,93.45,93.68,93.91,38.26,20.18,30.66,44.79,52.12,59.44,75.90,77.95,79.99,19.20,21.49,17.97,49.28,84.90,86.84,88.79,90.73,92.67]])

def route_nyc(t,x):
    """
    This function models traffic data along a given route.
    The function returns the expected speed at a given time t 
    and position x along the route. The model is based on 
    historical traffic data on a number of road links provided 
    by NYC OpenData.
    
    Parameters:
      0 <= t <= 24 (hour of day)
      0 <= x <= 60 (km from start of route)
    Returns:
      Speed in km/h    
    """
    return pchip_2d(data_t,data_x,nyc_velocity,t,x)-10

### PART 4A ###
def nyc_route_traveler_euler(t0,h):
    t_i = t0
    x_i = 0
    time_h = [t_i]
    distance_km = [x_i]
    speed_km = [float(route_nyc(t_i, x_i))]
    while x_i < 60:
        t_ip1 = t_i + h
        x_ip1 = x_i + h*float(route_nyc(t_i, x_i))
        if x_ip1 > 60:
            x_ip1 = 60
            h_2 = (60 - x_i)/float(route_nyc(t_i, x_i))
            t_ip1 = t_i + h_2
        x_i = x_ip1
        t_i = t_ip1
        time_h.append(t_i)
        distance_km.append(x_i)
        speed_km.append(float(route_nyc(t_i, x_i)))
    time_h = np.array(time_h)
    distance_km = np.array(distance_km)
    speed_km = np.array(speed_km)
    return time_h, distance_km, speed_km
    
