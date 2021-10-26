import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
from Helpers.FeatureExtractors.Contours import Countours
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.FeatureExtractors.Contours import Countours

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\CustomWindow.png')

def SharpAndNegative(img):
    img_bw = ImageConverters.ConvertToBW(img)
    negative = cv2.bitwise_not(img_bw)
    contours, hierarchy = Countours.GetContours(negative)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        point1 = (x, y)
        point2 = (x + w, y + h)
        #if(h > 300):
        cv2.rectangle(img, point1, point2, (0, 255, 0), 1)
    print(len(contours))
    return img

img=SharpAndNegative(img)
image = cv2.resize(img, (2400, 800))
cv2.imshow("", image)
cv2.waitKey(0)