#!　/usr/local/anaconda3/bin/python3


import cgi
import cgitb
import sys

sys.stderr = sys.stdout

from template.main_page import get_page

cgitb.enable(display=0, logdir="./log")

form = cgi.FieldStorage()

IMAGE_DIR = "static/images/ramen"

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
print(get_page(image, feature))
