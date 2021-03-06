import cv2
import numpy as np

class ImageFilters():

    def Blur(img):
        img = cv2.GaussianBlur(img, (3, 3), 0)
        return img

    def Sharp(img):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)
        return img

    def Gamma(img):
        gamma = 0.5
        invGamma = 1 / gamma
        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)
        img = cv2.LUT(img, table)
        return img

