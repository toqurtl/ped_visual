# folder statistics

from ped.core.scene import Scene
from ped.analysis import person_analysis
from pandas import DataFrame
import numpy as np


def to_pandas(analysis_folder_list, group_name="_"):
    data_dict = {            
            'person_id': [],
            'scene_id': [],
            'group': [],
            'num_person': [],
            'a_mean': [],
            'a_std': [],
            'v_mean': [],
            'v_std': [],
            'd_mean':[],
            'd_std': [],
            'v_mean_avg': [],
            'd_mean_avg': [],            
        }
    
    for s_folder_path in analysis_folder_list:
        s = Scene(s_folder_path, group_name=group_name)
        for person in s.person_dict.values():
            if person_analysis.is_hallway(person):
                for key in data_dict.keys():
                    data_dict[key].append(person.to_dict()[key])
    return DataFrame.from_dict(data_dict)


def to_pandas_interval(analysis_folder_list, interval, group_name="_"):
    data_dict = {            
            'person_id': [],
            'scene_id': [],
            'group': [],
            'num_person': [],
            'a_mean': [],
            'a_std': [],
            'v_mean': [],
            'v_std': [],
            'd_mean':[],
            'd_std': [],
            'v_mean_avg': [],
            'd_mean_avg': [],            
        }
    
    for s_folder_path in analysis_folder_list:
        s = Scene(s_folder_path, group_name=group_name)
        for person in s.person_dict.values():
            if person_analysis.is_hallway(person):
                for key in data_dict.keys():
                    data_dict[key].append(person.to_dict_interval(interval)[key])
    return DataFrame.from_dict(data_dict)
                

def basic_statistics(analysis_folder_list, group_name="_"):    
    velocity_mean = 0
    velocity_deviation = 0
    direction_mean = 0 
    direction_deviaion = 0
    ctn = 0    
    for s_folder_path in analysis_folder_list:
        s = Scene(s_folder_path, group_name=group_name)
        for person in s.person_dict.values():     
            if person_analysis.is_hallway(person):                
                v_mean, v_dev = person.velocity_data.mean(), person.velocity_data.std()
                d_mean, d_dev = person.direction_data.mean(), person.direction_data.std()
                velocity_mean += v_mean
                velocity_deviation += v_dev
                direction_mean += d_mean
                direction_deviaion += d_dev                
                ctn += 1

def direction_avg(analysis_folder_list, group_name="-"):    
    direction_avg_list = []
    for s_folder_path in analysis_folder_list:
        s = Scene(s_folder_path, group_name=group_name)
        for person in s.person_dict.values():
            direction_avg_list.append(person.direction_avg)
    return np.array(direction_avg_list)


            
