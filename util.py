import glob
from dataclasses import dataclass

import numpy as np

# IMAGE_DIR = "static/images/ramen"
IMAGE_DIR = "static/images"
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


def get_queries(form):
    query_index = 0
    feature = "11"

    if "i" in form:
        query_index = int(form["i"].value)
    if "f" in form:
        feature = form["f"].value

    return query_index, feature


# 2つのヒストグラムの類似度をIntersectionで比較
def compare_hist(data, query_index, images_list):
    similarity = []
    for i in range(len(images_list)):
        sim_r = np.minimum(data[query_index][0][0], data[i][0][0])
        sim_g = np.minimum(data[query_index][0][1], data[i][0][1])
        sim_b = np.minimum(data[query_index][0][2], data[i][0][2])
        sim = (sim_r + sim_g + sim_b) / 3.0
        similarity.append(sim.sum())
    return similarity


def compare_hist2(data, query_index, images_list):
    similarity_all = []
    for i in range(len(images_list)):
        similarity = []
        for j in range(data.shape[1]):
            sim_d1 = np.minimum(data[query_index][j][0], data[i][j][0])
            sim_d2 = np.minimum(data[query_index][j][1], data[i][j][1])
            sim_d3 = np.minimum(data[query_index][j][2], data[i][j][2])
            sim = (sim_d1 + sim_d2 + sim_d3) / 3.0
            similarity.append(sim.sum())
        img_sim = np.array(similarity_all).sum()
        similarity_all.append(img_sim)
        print(img_sim)
    return similarity_all


def sort_list(sim, target_list):
    zip_list = zip(sim, target_list)
    zip_sort = sorted(zip_list, reverse=True)
    sim, target_list = zip(*zip_sort)

    for i in range(len(target_list)):
        target_list[i].similarity = sim[i]

    return target_list


def sortedlist_by_feature(query_index, feature, images_list):
    data = None
    if feature == "10":
        data = np.load("static/data/RGB1.npy")
    elif feature == "11":
        data = np.load("static/data/RGB2.npy")
    elif feature == "12":
        pass
    elif feature == "13":
        data = np.load("static/data/HSV1.npy")
    elif feature == "14":
        pass
    elif feature == "15":
        pass
    elif feature == "16":
        data = np.load("static/data/LUV1.npy")
    elif feature == "17":
        pass
    elif feature == "18":
        pass
    elif feature == "19":
        pass
    else:
        pass

    if feature == "11":
        similarity = compare_hist2(data, query_index, images_list)
    else:
        similarity = compare_hist(data, query_index, images_list)

    sorted_list = sort_list(similarity, images_list)
    return sorted_list


if __name__ == '__main__':
    q = 0
    f = "11"
    i = init_images()
    d = np.load("static/data/RGB2.npy")
    sim = compare_hist2(d, q, init_images())
    print(sim)
