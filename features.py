import glob

import cv2
import numpy as np
from tqdm import tqdm

from util import IMAGE_DIR

images_path_list = [img for img in sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))]


# RGBヒストグラムによる特徴量抽出を行う
# split_n = 2の場合は画像を2×2に分割
def extract_hist(img_path, hist_type="RGB", split_n=1):
    img = cv2.imread(img_path)

    if hist_type == "RGB":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif hist_type == "HSV":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif hist_type == "LUV":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

    imgs = split_image(img, split_n)
    hist = []

    for img in imgs:
        d1, d2, d3 = img[..., 0], img[..., 1], img[..., 2]
        img_shape = img.shape[0] * img.shape[1]

        hist_d1 = cv2.calcHist([d3], [0], None, [256], [0, 256]) / img_shape
        hist_d2 = cv2.calcHist([d2], [0], None, [256], [0, 256]) / img_shape
        hist_d3 = cv2.calcHist([d1], [0], None, [256], [0, 256]) / img_shape

        h = np.array([hist_d1, hist_d2, hist_d3])
        hist.append(h)

    return hist


# 特徴抽出methodを定義して全画像リストに対して特徴抽出
def write_alldata(filename, data_type, data_dir="static/data"):
    all_data = []

    for i, image in enumerate(tqdm(images_path_list)):
        data = extract_hist(image, data_type)
        all_data.append(data)

    all_data = np.array(all_data)

    # 出力は(画像数, 3, 256, 1)のサイズ
    np.save(f"{data_dir}/{filename}", all_data)


def write_alldata2(filename, data_type, data_dir="static/data"):
    all_data = []

    for i, image in enumerate(tqdm(images_path_list)):
        data = extract_hist(image, data_type, 2)
        all_data.append(data)

    all_data = np.array(all_data)
    print(all_data.shape)

# 特徴量データの作成
def create_features_data():
    write_alldata("RGB1", "RGB")
    write_alldata("HSV1", "HSV")
    write_alldata("LUV1", "LUV")


def split_image(img, n):
    h, w = img.shape[:2]
    x0, y0 = int(w / n), int(h / n)

    images = []
    for x in range(n):
        for y in range(n):
            separate_img = img[x0 * x: x0 * (x + 1), y0 * y: y0 * (y + 1)]
            images.append(separate_img)

    return images


if __name__ == '__main__':
    write_alldata("RGB1", "RGB")
