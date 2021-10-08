import cv2
import numpy as np

class CommonMethods():

    def CropImage(image, x, y, w, h):
        img = image[y:y + h, x:x + w]
        return img

    def ShowImage(image):
        image = cv2.resize(image, (1200, 800))
        cv2.imshow("", image)
        cv2.waitKey(0)

    def GetMedian(image):
        #медиана - половина массива меньше этого значения, а половина больше
        median_intensity = np.median(image)
        return median_intensity

    def Resize(image, w, h):
        resized_image = cv2.resize(image, (w, h))
        return resized_image

    def GetPercent(number, percent):
        return round((number / 100) * percent)
