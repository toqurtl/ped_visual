from ped.core.scene import Scene
from ped.core.person import Person

def basic_statistics(group_folder_path):
    velocity_mean = 0
    velocity_deviation = 0
    direction_mean = 0 
    direction_deviaion = 0
    ctn = 0
    for s_folder_path in group_folder_path:
        s = Scene(s_folder_path)
        for person in s.person_dict.values():
            v_mean, v_dev = person.info_velocity()
            d_mean, d_dev = person.info_direction()            
            if 4 < v_mean < 10:            
                velocity_mean += v_mean
                velocity_deviation += v_dev
                direction_mean += d_mean
                direction_deviaion += d_dev
                if d_mean < 0:          
                    print(s_folder_path, d_mean, d_dev)
                ctn += 1