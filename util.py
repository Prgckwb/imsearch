import glob
from dataclasses import dataclass

IMAGE_DIR = "static/images/ramen"
DATA_DIR = "static/data"

FEATURES_NAME_INTERSEC = {
    "0": "RGB Color Histogram 1×1",
    "1": "RGB Color Histogram 2×2",
    "2": "RGB Color Histogram 3×3",
    "3": "HSV Color Histogram 1×1",
    "4": "HSV Color Histogram 2×2",
    "5": "HSV Color Histogram 3×3",
    "6": "LUV Color Histogram 1×1",
    "7": "LUV Color Histogram 2×2",
    "8": "LUV Color Histogram 3×3",
    "9": "DCNN Features",
}

FEATURES_NAME_EUCLID = {}

FEATURES_NAME = {**FEATURES_NAME_INTERSEC, **FEATURES_NAME_EUCLID}

FEATURES_DATA_PATH = {
    "0": f"{DATA_DIR}/RGB1.npy"
}

@dataclass
class Image:
    path: str
    index: int
    similarity: float = 0

    def __lt__(self, other):
        return self.index < other.index




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
