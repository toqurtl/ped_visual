from ped.read_file import read_scene
from ped import ped_cfg as cfg
import os

# For strange folder detection
## folder structure
def check_every_csv_exist(folder_path):
    file_list = os.listdir(folder_path)
    label_list = []
    for file_name in file_list:
        if ".csv" in file_name:        
            label = file_name[:-4].split("_")[1]
            label_list.append(label)
    for csv in cfg.item_list():
        if csv not in label_list:
            return False
    return True

def check_time_unit(folder_path):    
    data_map = read_scene.data_map(folder_path)
    ctn = data_map.get("a").count().to_numpy()[0]  
    for key, value in data_map.items():
        valid_ctn = cfg.offspring(key) + ctn
        value_ctn = value.count().to_numpy()[0]
        if value_ctn != valid_ctn:            
            return False         
    return True
            
## csv file