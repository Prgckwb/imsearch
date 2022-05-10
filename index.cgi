#! /usr/local/anaconda3/bin/python3
import cgi

import numpy as np

from template.main_page import get_page
from util import init_images, sort_list, compare_hist

form = cgi.FieldStorage()

images_list = init_images()
sorted_list = images_list.copy()

query_index = 0
feature = "10"

# クエリ画像と特徴量メソッドの取得・定義
if "i" in form:
    query_index = int(form["i"].value)

if "f" in form:
    feature = form["f"].value

similarity = None

if feature == "10":
    data = np.load("static/data/RGB1.npy")
    similarity = compare_hist(data, query_index, images_list)
    sorted_list = sort_list(similarity, sorted_list)
elif feature == "13":
    data = np.load("static/data/HSV1.npy")
    similarity = compare_hist(data, query_index, images_list)
    sorted_list = sort_list(similarity, sorted_list)
elif feature == "16":
    data = np.load("static/data/LUV1.npy")
    similarity = compare_hist(data, query_index, images_list)
    sorted_list = sort_list(similarity, sorted_list)

# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')
print(get_page(query_index, feature, images_list, sorted_list))
