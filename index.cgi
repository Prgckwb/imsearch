#! /usr/local/anaconda3/bin/python3
import cgi

import numpy as np

from template.main_page import get_page
from util import *

form = cgi.FieldStorage()

images_list = init_images()
# sorted_list = images_list.copy()

# query_index = 0
# feature = "10"
#
# # クエリ画像と特徴量メソッドの取得・定義
# if "i" in form:
#     query_index = int(form["i"].value)
#
# if "f" in form:
#     feature = form["f"].value
query_index, feature = get_queries(form)
print(query_index)
print(feature)

sorted_list = sortedlist_by_feature(query_index, feature, images_list)

# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')

html = get_page(query_index, feature, images_list, sorted_list)
print(html)
