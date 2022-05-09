import cv2


def rgb_hist(img):
    # img = cv2.imread("./static/images/ramen/2192.jpg")
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    print(img.shape)
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    hist = [hist_r, hist_g, hist_b]
    return hist


if __name__ == '__main__':
    # calc()
    pass