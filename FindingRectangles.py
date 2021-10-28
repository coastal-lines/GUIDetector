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
from Helpers.PatternMatching.PatternMatching import PatternMatching

#нужно добавлять черные отступы к темплейту, судя по всему
#иначе главные контуры пропускаются

def Preprocessing():
    sharp = ImageFilters.Sharp(img_bw)
    erosion = MorphologicalOperations.Erosion(sharp)
    blur = ImageFilters.Blur(erosion)
    ddept = cv2.CV_16S
    x = cv2.Sobel(erosion, ddept, 1, 0, ksize=3, scale=10)
    y = cv2.Sobel(erosion, ddept, 0, 1, ksize=3, scale=10)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 1)



def findContournsByDifferentWays(img_bw):
    contours = None

    sharp = ImageFilters.Sharp(img_bw)
    erosion = MorphologicalOperations.Erosion(sharp)
    blur = ImageFilters.Blur(erosion)
    ddept = cv2.CV_16S
    x = cv2.Sobel(erosion, ddept, 1, 0, ksize=3, scale=10)
    y = cv2.Sobel(erosion, ddept, 0, 1, ksize=3, scale=10)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 1)

    contoursCannyEdge, hierarchy  = Countours.GetContoursByCanny(edge, 220, 255)
    print(type(contoursCannyEdge))

    th = Threshold.AdaptiveThreshold(erosion, 255, 11, 8)
    contoursCannyThreshold, hierarchy  = Countours.GetContoursByCanny(th, 220, 255)
    print(type(contoursCannyThreshold))

    blur = ImageFilters.Blur(img_bw)
    th = Threshold.InRangeThreshold(blur, 245, 255)
    contoursTh, hierarchy = Countours.GetContours(th)

    contours = contoursCannyEdge
    contours.extend(contoursCannyThreshold)
    contours.extend(contoursTh)

    return contours

#11351 match
#loading files
#pattern = ImageLoaders.LoadImage(r'C:\Temp\!my\TestsTab\TestsMainTab.bmp')
#pattern_bw = ImageConverters.ConvertToBW(pattern)
img = ImageLoaders.LoadImage(r'C:\Temp\!my\TestsTab\TestsLowScreen.bmp')
img_bw = ImageConverters.ConvertToBW(img)
filter = ImageLoaders.LoadImage(r'C:\Temp\!my\TestsTab\Filter.bmp')
filter_bw = ImageConverters.ConvertToBW(filter)

#calculating average
#h,w = pattern_bw.shape[:2]
h,w = filter_bw.shape[:2]
high_w = w + (w * 1.5)
high_h = h + (h * 1.5)
low_w = w - (w / 1.5)
low_h = h - (h / 1.5)

#searching contours
range_value = 128

contours = findContournsByDifferentWays(img_bw)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    point1 = (x, y)
    point2 = (x + w, y + h)
    cv2.rectangle(img, point1, point2, (25, 0, 255), 1)

    if(w > low_w and w < high_w and h > low_h and h < high_h):
        #cv2.rectangle(img, point1, point2, (255, 255, 0), 1)
        roi = CommonMethods.CropImage(img_bw, x, y, w, h)
        p = PatternMatching.ComparePixelByPixel(filter_bw,roi)
        print(p)
        if(p == 199023):
            cv2.rectangle(img, point1, point2, (255, 60, 255), 4)


    #pattern_resized = CommonMethods.Resize(pattern_bw, range_value, range_value)
    #roi_resized = CommonMethods.Resize(roi, range_value, range_value)




image = cv2.resize(img, (1400, 1000))
cv2.imshow("", image)
cv2.waitKey(0)