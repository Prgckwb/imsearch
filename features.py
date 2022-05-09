import cv2


def calc():
    img = cv2.imread("./static/images/ramen/2192.jpg")
    b, g, r = img[..., 0], img[...,1], img[..., 2]
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    print(hist_b)


if __name__ == '__main__':
    calc()