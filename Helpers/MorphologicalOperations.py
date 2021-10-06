import numpy as np
import cv2

class MorphologicalOperations():

    def Dilation(img):
        kernel = np.ones((3, 3), np.uint8)
        img_dilation = cv2.dilate(img, kernel, iterations=1)
        return img_dilation

    def Erosion(img):
        kernel = np.ones((3, 3), np.uint8)
        img_dilation = cv2.erode(img, kernel, iterations=1)
        return img_dilation