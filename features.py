import glob

import cv2
import numpy as np
from tqdm import tqdm

IMAGE_DIR = "static/images/ramen"
images_list = [img for img in sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))]


# RGBヒストグラムによる特徴量抽出を行う
def rgb_hist(img_path):
    img = cv2.imread(img_path)
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    img_shape = img.shape[0] * img.shape[1]

    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256]) / img_shape
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256]) / img_shape
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256]) / img_shape

    hist = np.array([hist_r, hist_g, hist_b])
    return hist


# 特徴抽出methodを定義して全画像リストに対して特徴抽出
def write_alldata(images_list, method, filename, data_dir="static/data"):
    all_data = []

    for i, image in enumerate(tqdm(images_list)):
        data = method(image)
        all_data.append(data)

    all_data = np.array(all_data)
    np.save(f"{data_dir}/{filename}", all_data)


if __name__ == '__main__':
    write_alldata(images_list, rgb_hist, "RGB1")
    # d = np.load("static/data/RGB1.npy")
    # print(d.shape)
