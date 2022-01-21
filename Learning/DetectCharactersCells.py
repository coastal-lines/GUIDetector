from Helpers.Json import JsonHelper
import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.FeatureExtractors.Contours import Contours
from Helpers.Json.LabeledData import OriginalElement, LabeledData
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.ActionsForElements import ActionsForElements
import pytesseract

list_subject1 = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects8.bmp")
th, threshed = cv2.threshold(list_subject1, 127, 255, cv2.THRESH_BINARY_INV)

#т.е. вся матрица сжимается в вектор по вертикали. при этом значения суммируются и делятся на число столбцов. т.о. получается среднее значение для столбца
hist_x = cv2.reduce(threshed, 0, cv2.REDUCE_AVG)
hist_x_reshaped = hist_x.reshape(-1)
#здесь наоборот, матрица сжимается по горизонтали и получается среднее значение для строки
hist_y = cv2.reduce(threshed, 1, cv2.REDUCE_AVG)
hist_y_reshaped = hist_y.reshape(-1)

#CommonMethods.ShowImage(hist)

th = 2
H,W = list_subject1.shape[:2]
# обходим все горизонтальные точки
# решение в одну строчку
#uppers2 = [y for y in range(H-1) if hist_reshaped[y]<=th and hist_reshaped[y+1]>th]

# мы ищем такие вертикальные точки, где начинается рост яркости. От 0 до 255
# складываем их в массив
uppers_x = []
for i in range(H - 1):
    if(hist_x_reshaped[i] <= th and hist_x_reshaped[i + 1] > th):
        uppers_x.append(i)

uppers_y = []
for i in range(W - 1):
    if(hist_y_reshaped[i] <= th and hist_y_reshaped[i + 1] > th):
        uppers_y.append(i)

# содаём новое изображение
finish_image = cv2.cvtColor(list_subject1, cv2.COLOR_GRAY2BGR)

# отрисовываем линии по полученным точкам максиумов
for i in uppers_x:
    cv2.line(finish_image, (0, i), (W, i), (255, 0, 0), 1)

for i in uppers_y:
    cv2.line(finish_image, (i, 0), (i, H), (255, 0, 0), 1)

# насамомделе ничего рисовать не нужно, нужны координаты полученных прямоугольников
# т.е. 1й прямоугольник это пространство между линией 1 и линией2
# плюс нужно немного сдвигать прямоугольник - текст не совсем ровно в него помещается
uppers = uppers_x.append(uppers_y)
rectangles = []
for i in range(len(uppers) - 1):
    x = 0
    y = uppers[i]
    w = W
    h = uppers[i + 1] - uppers[i]
    tuple = (x, y, w , h)
    rectangles.append(tuple)

for r in rectangles:
    x = r[0]
    y = r[1] - 5
    w = r[2]
    h = r[3]
    point1 = (x, y)
    point2 = (x + w, y + h)
#    cv2.rectangle(list_subject1, point1, point2, (0, 0, 0), 1)
#    image = CommonMethods.CropImage(list_subject1, x, y, w, h)
    #TesseractOCR.GetTextFromImage(image)

CommonMethods.ShowImageWithOriginalSize(finish_image)
#CommonMethods.ShowImageWithOriginalSize(list_subject1)