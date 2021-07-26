# functions compare two person
from ped.core.person import Person
from ped.core.scene import Scene
import numpy as np


def common_idx_list(person_pair):
    p1, p2 = person_pair
    if p1.scene.scene_id != p2.scene.scene_id:
        return
    p1_range, p2_range = p1.exist_idx_range, p2.exist_idx_range
    return list(set(p1_range) & set(p2_range))
    

def distance_of(person_pair, idx):
    p1, p2 = person_pair
    if p1.scene.scene_id != p2.scene.scene_id:
        return
    p1_pos, p2_pos = p1.position_at_idx(idx), p2.position_at_idx(idx)        
    return np.linalg.norm(p1_pos-p2_pos, ord=2)


def is_distance_of(person_pair, idx, dis_min, dis_max):
    return dis_min < distance_of(person_pair, idx) < dis_max


def distance_list_of(scene: Scene, person_pair):
    distance_list = []
    for idx in common_idx_list(scene, person_pair):
        distance_list.append([idx, distance_of(person_pair, idx)])
    return np.array(distance_list)

