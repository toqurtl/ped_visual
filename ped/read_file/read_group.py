import os
from ped.read_file import read_scene
from ped.read_file import check_folder

def available_scene_list(group_folder_path):
    folder_list = os.listdir(group_folder_path)
    available_list = []
    for folder_name in folder_list:
        folder_path = os.path.join(group_folder_path, folder_name)        
        check_1 = check_folder.check_every_csv_exist(folder_path)
        if check_1:
            check_2 = check_folder.check_time_unit(folder_path)
            if check_2:
                available_list.append(folder_path)                
    return available_list

def scene_list_with_num_person(group_folder_path):
    pass

def opossite_scene_list_opposite(group_folder_path):
    pass