from ped.read_file import read_scene
from ped.core.person import Person
import numpy as np

class Scene(object):
    def __init__(self, folder_path, group_name="_"):        
        self.folder_path = folder_path
        self.group_name = group_name   
        self.scene_id = group_name + "_scene_" + folder_path.split("\\")[-1]        
        self.person_dict= {}
        self._set_data()
        self._create_person()
        
    def _set_data(self):
        self.data_path_map = read_scene.data_file_path_map(self.folder_path)
        self.data_map = read_scene.data_map(self.folder_path)
        self.person_idx_list = read_scene.person_index_list(self.folder_path)
        self.time_idx = read_scene.time_idx(self.folder_path)

    def _create_person(self):
        for person_idx in self.person_idx_list:
            p = Person(scene=self, person_idx=person_idx)
            self.person_dict[person_idx] = p

    @property
    def num_person(self):
        return len(self.person_dict)
        
    @property
    def velocity_data(self):
        return self.data_map["s"]

    @property
    def velocity_v_data(self):
        return self.data_map["vv"]

    @property
    def velocity_h_data(self):
        return self.data_map["hv"]

    @property
    def acceleration_data(self):
        return self.data_map["a"]

    @property
    def acceleration_v_data(self):
        return self.data_map["va"]

    @property
    def acceleration_h_data(self):
        return self.data_map["ha"]

    @property
    def position_v_data(self):
        return self.data_map["vp"]    

    @property
    def position_h_data(self):
        return self.data_map["hp"]

    def common_idx_list(self, p1: Person, p2: Person):        
        p1_range, p2_range = p1.exist_idx_range, p2.exist_idx_range
        return list(set(p1_range) & set(p2_range))

    def distance_of(self, p1: Person, p2: Person, idx: int):
        p1_pos = p1.position_at_idx(idx)
        p2_pos = p2.position_at_idx(idx)
        return np.linalg.norm(p1_pos-p2_pos, ord=2)

    def distance_list_of(self, p1: Person, p2: Person):
        distance_list = []
        for idx in self.common_idx_list(p1, p2):
            distance_list.append([idx, self.distance_of(p1, p2, idx)])
        return distance_list

