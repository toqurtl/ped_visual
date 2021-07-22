from ped.core.person import Person
from ped import ped_cfg as cfg


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
