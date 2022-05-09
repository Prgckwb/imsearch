#! /usr/local/anaconda3/bin/python3


import cgi
import glob

from template.main_page import get_page


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


# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')
print(get_page(query_index, feature, images_list))
