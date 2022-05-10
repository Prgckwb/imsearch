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
    feature = "10"

    if "i" in form:
        query_index = int(form["i"].value)
    if "f" in form:
        feature = form["f"].value

    return query_index, feature


# 2つのヒストグラムの類似度をIntersectionで比較
def compare_hist(data, query_index, images_list):
    similarity = []

    # 画像を何分割したデータであるか
    n = data.shape[1]

    # データセットの一枚ごとについて比較
    for i in range(len(images_list)):
        # 画像を分割した領域ごとの類似度
        region_sum = []

        # 分割した領域ごとについて比較
        for j in range(n):
            sim_d1 = np.minimum(data[query_index][j][0], data[i][j][0])
            sim_d2 = np.minimum(data[query_index][j][1], data[i][j][1])
            sim_d3 = np.minimum(data[query_index][j][2], data[i][j][2])
            sim = (sim_d1 + sim_d2 + sim_d3) / 3.0

            region_sum.append(sim.sum())

        # 画像1枚についての類似度
        image_sum = np.array(region_sum).sum() / n
        similarity.append(image_sum)
    return similarity


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
        data = np.load("static/data/RGB3.npy")
    elif feature == "13":
        data = np.load("static/data/HSV1.npy")
    elif feature == "14":
        data = np.load("static/data/HSV2.npy")
    elif feature == "15":
        data = np.load("static/data/HSV3.npy")
    elif feature == "16":
        data = np.load("static/data/LUV1.npy")
    elif feature == "17":
        data = np.load("static/data/LUV2.npy")
    elif feature == "18":
        data = np.load("static/data/LUV3.npy")
    elif feature == "19":
        pass
    else:
        pass

    similarity = compare_hist(data, query_index, images_list)
    sorted_list = sort_list(similarity, images_list)
    return sorted_list


if __name__ == '__main__':
    pass
