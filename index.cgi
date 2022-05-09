#! /usr/local/anaconda3/bin/python3


import cgi
import glob

import cv2
import numpy as np

from template.main_page import get_page
import features as f


form = cgi.FieldStorage()

IMAGE_DIR = "static/images/ramen"
images_list = [img for img in sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))]

query_index = "0"
feature = "0"

# クエリ画像と特徴量メソッドの取得・定義
if "i" in form:
    query_index = form["i"].value

if "f" in form:
    feature = form["f"].value

similarity = None
if f == "0":
    similarity = []

    data = np.load("static/data/RGB1.npy")
    for i in range(len(images_list)):
        sim_r = cv2.compareHist(data[query_index][0], data[i][0], cv2.HISTCMP_CORREL)
        sim_g = cv2.compareHist(data[query_index][1], data[i][1], cv2.HISTCMP_CORREL)
        sim_b = cv2.compareHist(data[query_index][2], data[i][2], cv2.HISTCMP_CORREL)
        sim = (sim_r + sim_g + sim_b) / 3.0
        similarity.append(sim)



# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')
print(get_page(query_index, feature, images_list))
print(similarity)
