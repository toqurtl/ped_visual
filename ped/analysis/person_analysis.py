from ped.core.person import Person
from ped import ped_cfg as cfg
import numpy as np


def velocity_in_hallway(person: Person):
    v_mean = person.velocity_data.mean()
    return cfg.v_mean_min() < v_mean < cfg.v_mean_max()

def direction_in_hallway(person: Person):
    d_mean = person.direction_data.mean()
    if d_mean > 0:
        return cfg.d_mean_p_min() < d_mean < cfg.d_mean_p_max()
    else:
        return cfg.d_mean_n_min() < d_mean < cfg.d_mean_n_max()

def is_hallway(person: Person):
    return velocity_in_hallway(person) and direction_in_hallway(person)

def exception_position(person: Person):
    ctn_near_exception = 0
    exception_dict = cfg.exception_dict()
    # TODO : general_exception
    exception_pos = np.array([exception_dict["door"]["h"], exception_dict["door"]["v"]])
    range = exception_dict["door"]["range"]
    check = exception_dict["door"]["num_check"]
    for pos in person.position():
        if np.linalg.norm(exception_pos-pos, ord=2) < range:
            ctn_near_exception += 1
            if ctn_near_exception > check:
                return True

    return False
        
