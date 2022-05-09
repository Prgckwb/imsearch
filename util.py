import glob
from dataclasses import dataclass


@dataclass
class Image:
    path: str
    index: int
    similarity: float = 0

    def __lt__(self, other):
        return self.index < other.index


IMAGE_DIR = "static/images/ramen"


def init_images():
    imgs_list = []
    path_list = sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))
    for i in range(len(path_list)):
        image = Image(path_list[i], i)
        imgs_list.append(image)
    return imgs_list


def sort_list(sim, target_list):
    zip_list = zip(sim, target_list)
    zip_sort = sorted(zip_list, reverse=True)
    sim, target_list = zip(*zip_sort)

    for i in range(len(target_list)):
        target_list[i].similarity = sim[i]

    return target_list
