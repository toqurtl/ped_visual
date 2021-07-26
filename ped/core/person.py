from ped import utils
from ped import ped_cfg as cfg
import numpy as np
from pandas import Series

class Person(object):
    def __init__(self, scene, person_idx):
        self.scene = scene        
        self.person_idx = person_idx
        self._create_pos_info()
        self._create_exist_range()        
        
    def _create_pos_info(self):
        np_h, np_v = self.position_h_data.to_numpy(), self.position_v_data.to_numpy()
        np_h = np.expand_dims(np_h, axis=1)
        np_v = np.expand_dims(np_v, axis=1)
        self.pos = np.append(np_h, np_v, axis=1)
        self.start_pos = np.array([utils.not_nan_data(np_h)[0], utils.not_nan_data(np_v)[0]])
        self.finish_pos = np.array([utils.not_nan_data(np_h)[-1], utils.not_nan_data(np_v)[-1]])
    
    def _create_exist_range(self):
        time_range = utils.detected_time_range(
                data=self.scene_data_map["hp"],
                time_str=self.scene.time_idx,
                column_str=self.person_idx
            )
        self.exist_time_range = time_range["time"]
        self.exist_idx_range = time_range["idx"]
        
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

    @property
    def exist_time_interval(self):
        return (self.exist_time_range[-1] - self.exist_time_range[0]) / cfg.time_unit_for_sec()

    @property
    def velocity_avg(self):        
        return np.linalg.norm(self.finish_pos - self.start_pos, ord=2) / self.exist_time_interval   
    
    @property
    def direction_avg(self):   
        diff = self.finish_pos - self.start_pos
        _, theta = utils.cart2pol_theta(diff[0], diff[1])
        return theta

    @property
    def direction(self):
        return self.direction_avg > 0

    # time
    def time(self, idx):
        return self.scene.time(idx)

    def time_interval(self, start_idx, finish_idx):
        return self.scene.time_interval(start_idx, finish_idx)

    # interval(if interval=1 -> same as property)
    def velocity_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.velocity_data, interval)
        else:
            return utils.to_interval(self.velocity_data, interval)[idx]
        
    def velocity_v_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.velocity_v_data, interval)
        else:
            return utils.to_interval(self.velocity_v_data, interval)[idx]
        
    def velocity_h_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.velocity_h_data, interval)
        else:
            return utils.to_interval(self.velocity_h_data, interval)[idx]
        
    def acceleration_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.acceleration_data, interval)
        else:
            return utils.to_interval(self.acceleration_data, interval)[idx]
        
    def acceleration_v_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.acceleration_v_data, interval)
        else:
            return utils.to_interval(self.acceleration_v_data, interval)[idx]
        
    def acceleration_h_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.acceleration_h_data, interval)
        else:
            return utils.to_interval(self.acceleration_h_data, interval)[idx]
        
    def position_v_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.position_v_data, interval)
        else:
            return utils.to_interval(self.position_v_data, interval)[idx]
        
    def position_h_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.position_h_data, interval)
        else:
            return utils.to_interval(self.position_h_data, interval)[idx]

    def direction_data_interval(self, interval, idx=-1):
        if idx==-1:
            return utils.to_interval(self.direction_data, interval)
        else:
            return utils.to_interval(self.direction_data, interval)[idx]

    # statistics
    def info_at_idx(self, idx, interval=1):
        return {            
            'person_id': self.scene.scene_id+"_"+self.person_idx,
            'scene_id': self.scene.scene_id,
            'group': self.scene.group_name,
            'num_person': self.scene.num_person,
            'a': self.acceleration_data_interval(interval=interval, idx=idx),            
            'v': self.velocity_data_interval(interval=interval, idx=idx),
            'hv': self.velocity_h_data_interval(interval=interval, idx=idx),
            'vv': self.velocity_v_data_interval(interval=interval, idx=idx),
            'hp': self.position_h_data_interval(interval=interval, idx=idx),
            'vp': self.position_v_data_interval(interval=interval, idx=idx),            
            'd': self.direction_data_interval(interval=interval, idx=idx),            
        }

    def to_dict(self):
        return {            
            'person_id': self.scene.scene_id+"_"+self.person_idx,
            'scene_id': self.scene.scene_id,
            'group': self.scene.group_name,
            'num_person': self.scene.num_person,
            'a_mean': self.acceleration_data.mean(),
            'a_std':  self.acceleration_data.std(),
            'v_mean': self.velocity_data.mean(),
            'v_std': self.velocity_data.std(),
            'd_mean': self.direction_data.mean(),
            'd_std': self.direction_data.std(),
            'v_mean_avg': self.velocity_avg,
            'd_mean_avg': self.direction_avg,
        }
    
    def to_dict_interval(self, interval):
        return {            
            'person_id': self.scene.scene_id+"_"+self.person_idx,
            'scene_id': self.scene.scene_id,
            'group': self.scene.group_name,
            'num_person': self.scene.num_person,
            'a_mean': self.acceleration_data_interval(interval).mean(),
            'a_std':  self.acceleration_data_interval(interval).std(),
            'v_mean': self.velocity_data_interval(interval).mean(),
            'v_std': self.velocity_data_interval(interval).std(),
            'd_mean': self.direction_data_interval(interval).mean(),
            'd_std': self.direction_data_interval(interval).std(),
            'v_mean_avg': self.velocity_avg,
            'd_mean_avg': self.direction_avg,
        }
        
    # behavior
    # def _create_position(self):
    #     np_h = self.position_h_data.to_numpy()
    #     np_v = self.position_v_data.to_numpy()
    #     np_h = np.expand_dims(np_h, axis=1)
    #     np_v = np.expand_dims(np_v, axis=1)
    #     self.pos = np.append(np_h, np_v, axis=1)
    #     return          

    def position_at_idx(self, idx):
        return self.position()[idx]

    def position(self):
        return self.pos
