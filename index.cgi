#! /usr/local/anaconda3/bin/python3


import cgi
import glob

from template.main_page import get_page


form = cgi.FieldStorage()

IMAGE_DIR = "static/images/ramen"
images_list = [img for img in glob.glob("static/images/ramen/*.jpg")]

image = ""
feature = "Unko"

# クエリ画像と特徴量メソッドの取得・定義
if "image" in form:
    image = form["image"].value
else:
    image = IMAGE_DIR + "/2192.jpg"
if "feature" in form:
    feature = form["feature"].value
else:
    feature = "RGB Histogram"

# ページの出力
# ヘッダーには文末に改行が必要
print('Content-Type: text/html\n')
print(get_page(image, feature, images_list))
