from ped import utils
from pandas import Series

class Person(object):
    def __init__(self, scene, person_idx):
        self.scene = scene        
        self.person_idx = person_idx
        
    @property
    def scene_data_map(self):
        return self.scene.data_map

    @property
    def velocity_data(self):
        return self.scene.velocity_data[self.person_idx]
        
    @property
    def velocity_v_data(self):
        return self.scene.velocity_v_data[self.person_idx]
        
    @property
    def velocity_h_data(self):
        return self.scene.velocity_h_data[self.person_idx]
        
    @property
    def acceleration_data(self):
        return self.scene.acceleration_data[self.person_idx]
        
    @property
    def acceleration_v_data(self):
        return self.scene.acceleration_v_data[self.person_idx]
        
    @property
    def acceleration_h_data(self):
        return self.scene.acceleration_h_data[self.person_idx]
        
    @property
    def position_v_data(self):
        return self.scene.position_v_data[self.person_idx]
        
    @property
    def position_h_data(self):
        return self.scene.position_h_data[self.person_idx]
    
    @property
    def direction_data(self):
        h_data = self.velocity_h_data
        v_data = self.velocity_v_data         
        r_data, di_data = utils.cart2pol_theta(h_data, v_data)        
        return di_data   

    def exist_time_range(self):        
        return utils.detected_time_range(
                data=self.scene_data_map["hp"],
                time_str=self.scene.time_idx,
                column_str=self.person_idx
            )

    def info_accerelation(self):
        return self.acceleration_data.mean(), self.acceleration_data.std()

    def info_velocity(self):
        return self.velocity_data.mean(), self.velocity_data.std()
    
    def info_direction(self):
        return self.direction_data.mean(), self.direction_data.std()

    def describe(self):
        des_dict = {
            "a": self.info_accerelation(),
            "v": self.info_velocity(),
            "d": self.info_direction()
        }
        return des_dict
    