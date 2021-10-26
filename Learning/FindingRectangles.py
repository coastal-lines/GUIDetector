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
img_bw = ImageConverters.ConvertToBW(img)
sharp = ImageFilters.Sharp(img_bw)
erosion = MorphologicalOperations.Erosion(sharp)
blur = ImageFilters.Blur(erosion)

ddept=cv2.CV_16S
x = cv2.Sobel(blur, ddept, 1,0, ksize=3, scale=10)
y = cv2.Sobel(blur, ddept, 0,1, ksize=3, scale=10)
absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 1)

contours, hierarchy = Countours.GetContoursByCanny(edge,220,255)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    point1 = (x, y)
    point2 = (x + w, y + h)
    if w > 300:
        cv2.rectangle(img, point1, point2, (255, 255, 0), 3)

th = Threshold.AdaptiveThreshold(blur,255,11,8)
image = cv2.resize(th, (1400, 800))
cv2.imshow("", image)
cv2.waitKey(0)