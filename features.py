import glob

import cv2
import numpy as np

IMAGE_DIR = "static/images/ramen"
images_list = [img for img in sorted(glob.glob(f"{IMAGE_DIR}/*.jpg"))]


def rgb_hist(img_path):
    # img = cv2.imread("./static/images/ramen/2192.jpg")
    img = cv2.imread(img_path)
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    img_shape = img.shape[0] * img.shape[1]

    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256]) / img_shape
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256]) / img_shape
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256]) / img_shape

    hist = [hist_r, hist_g, hist_b]
    return hist


def write_feature_data(data, file_name, data_dir="static/data"):
    np.save(f"{data_dir}/{file_name}", data)


if __name__ == '__main__':
    h = rgb_hist(images_list[0])
    print(h)
    # write_feature_data(h, "sample")
