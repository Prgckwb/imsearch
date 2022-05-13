#! /usr/local/anaconda3/bin/python3
import cgi

from template.main_page import get_page
from util import *

# クエリ情報取得
form = cgi.FieldStorage()

print('Content-Type: text/html\n')


# 画像データ・クエリ画像インデックス・特徴量選択の初期化
images_list = init_images()
query_index, feature = get_queries(form)

sorted_list = sort_list(query_index, feature, images_list)

# ページの出力
# ヘッダーには文末に改行が必要

html = get_page(query_index, feature, images_list, sorted_list)
print(html)
