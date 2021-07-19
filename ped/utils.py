import numpy as np
import math
from pandas import DataFrame, Series

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def cart2pol_theta(x,y):
    rho, phi = cart2pol(x,y)
    return rho, phi / math.pi * 180

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def detected_time_range(data: DataFrame, time_str: str, column_str: str):    
    data = data[[time_str, column_str]]
    nan_idx_list = []
    nan_time_list = []
    for idx, row in data.iterrows():
        if np.isnan(row[column_str]):
            nan_idx_list.append(idx)
            nan_time_list.append(row[time_str])
        
    return nan_time_list, nan_idx_list