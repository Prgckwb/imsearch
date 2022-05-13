# 特徴量抽出用スクリプト
# 事前に使うだけで実際のCGIプログラムには関係しない

import glob

import cv2
import numpy as np
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms
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
        # hist_type: RGBならそれぞれR.G.Bの情報
        d1, d2, d3 = cv2.split(img)  # img[..., 0], img[..., 1], img[..., 2]
        img_shape = img.shape[0] * img.shape[1]

        # 画像サイズに依らないように正規化
        hist_d1 = cv2.calcHist([d3], [0], None, [256], [0, 256]) / img_shape
        hist_d2 = cv2.calcHist([d2], [0], None, [256], [0, 256]) / img_shape
        hist_d3 = cv2.calcHist([d1], [0], None, [256], [0, 256]) / img_shape

        h = np.array([hist_d1, hist_d2, hist_d3])
        hist.append(h)

    return hist


def extract_dcnn_hist(img_path, transform, model):
    img = Image.open(img_path)
    img = transform(img).unsqueeze(0)
    img = img.to('cuda')
    output = model(img)

    return output


def write_dcnn_data( data_dir="static/data"):
    model = models.vgg16(pretrained=True)

    # 最終層を取り除く
    layers = list(model.classifier.children())[:-2]
    model.classifier = nn.Sequential(*layers)

    # 推論モードへ
    model.eval()

    model = model.to('cuda')

    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        )
    ])

    all_data = []
    for i, image in enumerate(tqdm(images_path_list)):
        data = extract_dcnn_hist(image, transform, model)
        data = data.to('cpu').detach().numpy().copy()
        all_data.append(data)

    all_data = np.array(all_data)
    print(all_data.shape)
    np.save(f"{data_dir}/DCNN", all_data)


# 特徴抽出methodを定義して全画像リストに対して特徴抽出
def write_data(data_type, split_n=1, data_dir="static/data"):
    all_data = []

    for i, image in enumerate(tqdm(images_path_list)):
        data = extract_hist(image, data_type, split_n)
        all_data.append(data)

    all_data = np.array(all_data)

    # 出力は(画像数, 3, 256, 1)のサイズ
    np.save(f"{data_dir}/{data_type}{split_n}", all_data)


# 特徴量データの作成
def create_features_data():
    type_list = ["RGB", "HSV", "LUV"]
    for i in range(1, 4):
        for c_type in type_list:
            write_data(c_type, i)


# 画像 img を n 分割した結果をリストで返す
def split_image(img, n):
    h, w = img.shape[:2]

    split_images = []
    cx, cy = 0, 0
    x0, y0 = int(w / n), int(h / n)

    for x in range(n):
        for y in range(n):
            part_image = img[cy:cy + y0, cx:cx + x0, :]
            cy += y0
            split_images.append(part_image)
        cy = 0
        cx += x0

    return split_images


if __name__ == '__main__':
    write_dcnn_data()
