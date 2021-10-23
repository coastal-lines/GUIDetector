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

#паттерн был сделан с разрешением 1920*1200 монитора и имеет размер 420*200
#текущий экран 1600*1200
#находим все прямоугольники и сжимаем их до соответствующих пропорций т.е. подгоняя под 1920*1200
#далее сравниваем попиксельно паттерн и каждый прямоугольник
#будет множество вариантов ускорения
#поискать как быть в случае частичного совпадения

pattern_screen_w = 1920
pattern_screen_h = 1080
pattern = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\TestSimpleComparing\pattern.png')
current_screen = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\CustomWindow.png')

img_bw = ImageConverters.ConvertToBW(current_screen)
th = Threshold.AdaptiveThreshold(img_bw, 255, 11, 8)
erosion = MorphologicalOperations.Erosion(th)
blur = ImageFilters.Blur(erosion)
contours, hierarchy = Countours.GetContours(blur)
print(len(contours))

matches = [0,9,5,3,4,1]
matches.sort(reverse=True)

def Comparator(pattern, roi):
    match_count = 0
    for i in range(128):
        for j in range(128):
            if(pattern[i][j] == roi[i][j]):
                match_count+=1

    return match_count

matches = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    point1 = (x, y)
    point2 = (x + w, y + h)
    #cv2.rectangle(current_screen, point1, point2, (0, 255, 0), 1)
    roi = CommonMethods.CropImageFromContour(current_screen, contour)
    roi_bw = ImageConverters.ConvertToBW(roi)
    pattern_bw = ImageConverters.ConvertToBW(pattern)
    pattern_resized = CommonMethods.Resize(pattern_bw, 128, 128)
    roi_resized = CommonMethods.Resize(roi_bw, 128, 128)
    match = Comparator(pattern_resized, roi_resized)
    print(match)
    matches.append(match)

matches.sort(reverse=True)
print("max_match: ")
print(matches[0])
print(matches[1])
print(matches[2])

#CommonMethods.ShowImage(pattern_resized)