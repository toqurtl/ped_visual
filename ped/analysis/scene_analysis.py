# for scene
from ped.core.scene import Scene


def num_person_range(scene: Scene, min, max):
    return min <= scene.num_person <= max

