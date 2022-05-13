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
    "10": f"{DATA_DIR}/RGB1.npy",
    "11": f"{DATA_DIR}/RGB2.npy",
    "12": f"{DATA_DIR}/RGB3.npy",
    "13": f"{DATA_DIR}/HSV1.npy",
    "14": f"{DATA_DIR}/HSV2.npy",
    "15": f"{DATA_DIR}/HSV3.npy",
    "16": f"{DATA_DIR}/LUV1.npy",
    "17": f"{DATA_DIR}/LUV2.npy",
    "18": f"{DATA_DIR}/LUV3.npy",
    "19": f"{DATA_DIR}/DCNN.npy",

    "20": f"{DATA_DIR}/RGB1.npy",
    "21": f"{DATA_DIR}/RGB2.npy",
    "22": f"{DATA_DIR}/RGB3.npy",
    "23": f"{DATA_DIR}/HSV1.npy",
    "24": f"{DATA_DIR}/HSV2.npy",
    "25": f"{DATA_DIR}/HSV3.npy",
    "26": f"{DATA_DIR}/LUV1.npy",
    "27": f"{DATA_DIR}/LUV2.npy",
    "28": f"{DATA_DIR}/LUV3.npy",
    "29": f"{DATA_DIR}/DCNN.npy",
}


# 表示される画像についてデータクラスとして保持
@dataclass
class Image:
    path: str
    index: int
    similarity: float = 0

    def __lt__(self, other):
        return self.index < other.index


# 使用する画像リストを初期化
def init_images():
    imgs_list = []
    path_list = sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))
    for i in range(len(path_list)):
        image = Image(path_list[i], i)
        imgs_list.append(image)
    return imgs_list


# ページからクエリ情報を取得する
def get_queries(form):
    query_index = 0
    feature = "10"

    if "i" in form:
        query_index = int(form["i"].value)
    if "f" in form:
        feature = form["f"].value

    return query_index, feature


# ヒストグラムをfeatureの手法で比較する
def compare_hist(data, query_index, feature, images_list):
    similarity = []

    # 画像を何分割したデータであるか
    n = data.shape[1]

    # EUCLIDで比較する場合
    if feature in FEATURES_NAME_EUCLID:
        if feature != "29":
            # データセットの一枚ごとについて比較
            for i in range(len(images_list)):
                # 画像を分割した領域ごとの類似度
                region_sum = []

                # 分割した領域ごとについて比較
                for j in range(n):
                    d1 = np.sqrt((data[query_index][j][0] - data[i][j][0]) ** 2)
                    d2 = np.sqrt((data[query_index][j][1] - data[i][j][1]) ** 2)
                    d3 = np.sqrt((data[query_index][j][2] - data[i][j][2]) ** 2)
                    dis = (d1 + d2 + d3) / 3.0

                    region_sum.append(dis.sum())

                # 画像1枚についての類似度
                image_sum = np.array(region_sum).sum() / n
                similarity.append(image_sum)
        else:
            # DCNNの時
            for i in range(len(images_list)):
                d = np.sqrt((data[query_index][0] - data[i][0])**2)
                similarity.append(d)

    # INTERSECTIONで比較する場合
    elif feature in FEATURES_NAME_INTERSEC:
        if feature != "19":
            # データセットの一枚ごとについて比較
            for i in range(len(images_list)):
                # 画像を分割した領域ごとの類似度
                region_sum = []

                # 分割した領域ごとについて比較
                for j in range(n):
                    s1 = np.minimum(data[query_index][j][0], data[i][j][0])
                    s2 = np.minimum(data[query_index][j][1], data[i][j][1])
                    s3 = np.minimum(data[query_index][j][2], data[i][j][2])
                    sim = (s1 + s2 + s3) / 3.0

                    region_sum.append(sim.sum())

                # 画像1枚についての類似度
                image_sum = np.array(region_sum).sum() / n
                similarity.append(image_sum)
        else:
            # DCNNの時
            pass
    return similarity


def sort_list(query_index, feature, images_list):
    data = np.load(FEATURES_DATA_PATH[feature])
    similarity = compare_hist(data, query_index, feature, images_list)

    zip_list = zip(similarity, images_list)

    zip_sort = None
    if feature in FEATURES_NAME_EUCLID:
        zip_sort = sorted(zip_list, reverse=False)
    elif feature in FEATURES_NAME_INTERSEC:
        zip_sort = sorted(zip_list, reverse=True)

    similarity, images_list = zip(*zip_sort)

    for i in range(len(images_list)):
        images_list[i].similarity = similarity[i]

    return images_list


if __name__ == '__main__':
    pass
