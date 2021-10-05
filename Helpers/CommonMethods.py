import cv2
import numpy as np

class CommonMethods():

    def CropImage(image, x, y, w, h):
        img = image[y:y + h, x:x + w]
        return img

    def ShowImage(image):
        cv2.imshow("", image)
        cv2.waitKey(0)

    def GeyMedian(image):
        #медиана - половина массива меньше этого значения, а половина больше
        median_intensity = np.median(image)
        return median_intensity
