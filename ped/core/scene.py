from ped.read_file import read_scene, read_csv
from ped.core.person import Person

class Scene(object):
    def __init__(self, folder_path): 
        self.folder_path = folder_path       
        self.data_path_map = read_scene.data_file_path_map(folder_path)
        self.data_map = read_scene.data_map(folder_path)
        self.person_idx_list = read_scene.person_index_list(folder_path)
        self.time_idx = read_scene.time_idx(folder_path)
        self.person_dict= {}
        self.__create_person()
        

    def __create_person(self):
        for person_idx in self.person_idx_list:
            p = Person(scene=self, person_idx=person_idx)
            self.person_dict[person_idx] = p
        

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
   
    def distance_of(p1: Person, p2: Person, idx):
        pass
