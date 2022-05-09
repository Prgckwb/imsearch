#! /usr/local/anaconda3/bin/python3


import cgi
import glob

import cv2
import numpy as np

from template.main_page import get_page
import features as f
from dataclasses import dataclass


@dataclass
class Image:
    path: str
    index: str
    similarity: float = 0

    def __lt__(self, other):
        return self.index < other.index


form = cgi.FieldStorage()
IMAGE_DIR = "static/images/ramen"


def init_images():
    imgs_list = []
    path_list = sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))
    for i in range(len(path_list)):
        image = Image(path_list[i], str(i))
        imgs_list.append(image)
    return imgs_list


images_list = init_images()

query_index = "0"
feature = "0"

# クエリ画像と特徴量メソッドの取得・定義
if "i" in form:
    query_index = form["i"].value

if "f" in form:
    feature = form["f"].value

similarity = None

if feature == "0":
    data = np.load("static/data/RGB1.npy")
    similarity = f.compare_hist(data, 0, images_list)


zip_list = zip(similarity, images_list)
zip_sort = sorted(zip_list, reverse=True)
similarity, images_list = zip(*zip_sort)

for i in range(len(images_list)):
    images_list[i].similarity = similarity[i]


# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')
print(get_page(query_index, feature, images_list))
print(similarity)
