import glob
from dataclasses import dataclass

IMAGE_DIR = "static/images/ramen"
DATA_DIR = "static/data"

FEATURES_NAME_INTERSEC = {
    "10": "RGB Color Histogram 1×1",
    "11": "RGB Color Histogram 2×2",
    "12": "RGB Color Histogram 3×3",
    "13": "HSV Color Histogram 1×1",
    "14": "HSV Color Histogram 2×2",
    "15": "HSV Color Histogram 3×3",
    "16": "LUV Color Histogram 1×1",
    "17": "LUV Color Histogram 2×2",
    "18": "LUV Color Histogram 3×3",
    "19": "DCNN Features",
}

FEATURES_NAME_EUCLID = {
    "20": "RGB Color Histogram 1×1",
    "21": "RGB Color Histogram 2×2",
    "22": "RGB Color Histogram 3×3",
    "23": "HSV Color Histogram 1×1",
    "24": "HSV Color Histogram 2×2",
    "25": "HSV Color Histogram 3×3",
    "26": "LUV Color Histogram 1×1",
    "27": "LUV Color Histogram 2×2",
    "28": "LUV Color Histogram 3×3",
    "29": "DCNN Features",
}

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
