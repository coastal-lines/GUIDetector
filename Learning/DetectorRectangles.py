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
#print(len(contours))

range_value = 512
def Comparator(pattern, roi):
    match_count = 0
    for i in range(range_value):
        for j in range(range_value):
            if(pattern[i][j] == roi[i][j]):
                match_count+=1

    return match_count

temp = []
count = 0
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    point1 = (x, y)
    point2 = (x + w, y + h)
    cv2.rectangle(current_screen, point1, point2, (0, 255, 0), 1)
    if(w > 900):
        ##if w > 300 and h > 300:
        rect = cv2.minAreaRect(contour)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат

        # roi = CommonMethods.CropImageFromContour(current_screen, box)
        roi = CommonMethods.CropImage(current_screen, x, y, w, h)
        roi_bw = ImageConverters.ConvertToBW(roi)
        pattern_bw = ImageConverters.ConvertToBW(pattern)
        pattern_resized = CommonMethods.Resize(pattern_bw, range_value, range_value)
        roi_resized = CommonMethods.Resize(roi_bw, range_value, range_value)
        match = Comparator(pattern_resized, roi_resized)
        # temp.append((match, contour))
        temp.append((match, contour))
        print(match)
        # matches.append(match)
        # matches_set.add(contour)
        # count += 1
        # if count > 5:
        #    break



print("========")
sorted_multi_list = sorted(temp, key=lambda x: x[0], reverse=True)
for i in range(len(sorted_multi_list)):
    cv2.drawContours(current_screen, [Countours.GetBoxFromContour(sorted_multi_list[i][1])], 0, (0, 0, 0), 3)

CommonMethods.ShowImage(current_screen)
print(len(temp))