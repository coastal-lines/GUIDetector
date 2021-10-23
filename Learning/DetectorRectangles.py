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

#паттерн был сделан с разрешением 1920*1200 монитора и имеет размер 420*200
#текущий экран 1600*1200
#находим все прямоугольники и сжимаем их до соответствующих пропорций т.е. подгоняя под 1920*1200
#далее сравниваем попиксельно паттерн и каждый прямоугольник
#будет множество вариантов ускорения
#поискать как быть в случае частичного совпадения

img_bw = ImageConverters.ConvertToBW(img)
th = Threshold.AdaptiveThreshold(img_bw, 255, 11, 8)
erosion = MorphologicalOperations.Erosion(th)
blur = ImageFilters.Blur(erosion)
contours, hierarchy = Countours.GetContours(blur)
print(len(contours))

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    point1 = (x, y)
    point2 = (x + w, y + h)
    cv2.rectangle(img, point1, point2, (0, 255, 0), 1)

CommonMethods.ShowImage(img)