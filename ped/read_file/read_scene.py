import os
import pandas as pd
from ped.read_file import read_csv

# for scene
def data_file_path_map(folder_path: str):
    file_list = os.listdir(folder_path)

    ped_data_path_map = {
        "a":"",
        "va":"",
        "ha":"",
        "s":"",
        "vv":"",
        "hv":"",
        "hp":"",
        "vp":""
    }    
    
    for file_name in file_list:
        if ".csv" in file_name:        
            label = file_name[:-4].split("_")[1]
            ped_data_path_map[label] = os.path.join(folder_path, file_name)

    return ped_data_path_map

def data_map(folder_path: str):
    file_path_map = data_file_path_map(folder_path)    
    new_dict = {}
    for key, file_path in file_path_map.items():
        new_dict[key] = pd.read_csv(file_path) 
    return new_dict

def person_index_list(folder_path: str):
    file_path_map = data_file_path_map(folder_path)
    file_path = file_path_map["a"]
    data = pd.read_csv(file_path)
    return read_csv.person_idx_list(data)

def time_idx(folder_path: str):
    file_path_map = data_file_path_map(folder_path)
    file_path = file_path_map["a"]
    data = pd.read_csv(file_path)
    return data.columns[0]

def max_time_unit(folder_path):
    position_df = data_map(folder_path)["hp"]
    return position_df.to_numpy()[-1][0]

def appear_time_info(folder_path):
    position_df = data_map(folder_path)["hp"]
    position_df[position_df.columns[1]]
    return
