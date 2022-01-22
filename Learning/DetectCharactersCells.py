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

#т.е. вся матрица сжимается в вектор по горизонтали (все строки сжимаются в одну). при этом значения суммируются и делятся на число столбцов. т.о. получается среднее значение для столбца
hist_x = cv2.reduce(threshed, 0, cv2.REDUCE_AVG)
hist_x_reshaped = hist_x.reshape(-1)
#здесь наоборот, матрица сжимается по вертикали (все столбцы сжимаются в один) и получается среднее значение для строки
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
for i in range(W - 1):
    if(hist_x_reshaped[i] <= th and hist_x_reshaped[i + 1] > th):
        uppers_x.append(i)

uppers_y = []
for i in range(H - 1):
    if(hist_y_reshaped[i] <= th and hist_y_reshaped[i + 1] > th):
        uppers_y.append(i)

# содаём новое изображение
finish_image = cv2.cvtColor(list_subject1, cv2.COLOR_GRAY2BGR)

# отрисовываем линии по полученным точкам максиумов
for i in uppers_x:
    cv2.line(finish_image, (i, 0), (i, H), (255, 0, 0), 1)

for i in uppers_y:
    cv2.line(finish_image, (0, i), (W, i), (255, 0, 0), 1)

# насамомделе ничего рисовать не нужно, нужны координаты полученных прямоугольников
# т.е. 1й прямоугольник это пространство между линией 1 и линией2
# плюс нужно немного сдвигать прямоугольник - текст не совсем ровно в него помещается
#uppers = np.concatenate((uppers_x, uppers_y), axis=0)

#найти среднее расстояние между буквами
allWidthBetweenLetters = []
for i in range(len(uppers_x) - 1):
    allWidthBetweenLetters.append(round((uppers_x[i + 1] - uppers_x[i])))
averageW = int(np.average(allWidthBetweenLetters))

charactersRegions = []
for i in range(len(uppers_x) - 1):
    p1 = (uppers_x[i], uppers_y[0])
    p2 = (uppers_x[i + 1], uppers_y[1] + 5)
    #cv2.rectangle(list_subject1, p1, p2, (0, 0, 0), 1)
    charactersRegions.append([p1, p2])

    #последняя ячейка выпадает - нужно самостоятельно создавать координаты на основе среднего значения
    if(i == len(uppers_x) - 2):
        p1 = (uppers_x[i + 1], uppers_y[0])
        p2 = (uppers_x[i + 1] + averageW, uppers_y[1]+ 5)
        #cv2.rectangle(list_subject1, p1, p2, (0, 0, 0), 1)
        charactersRegions.append([p1, p2])

    #нужно определять пробелы по среднему значению ширины. т.е. если ширина аномально большая, то скорее всего это пробел
    #а если два и более пробелов?.. TODO
    if(uppers_x[i + 1] - uppers_x[i] > averageW + (averageW / 2)):
        p1 = (uppers_x[i] + averageW, uppers_y[0])
        p2 = (uppers_x[i + 1], uppers_y[1]+ 5)
        #cv2.rectangle(list_subject1, p1, p2, (0, 0, 0), 1)
        charactersRegions.append([p1, p2])

#создаём roi для каждого символа с учётом необходимого пространства (как-то отдельно нужно заранее помечать пробелы)
averageH = uppers_y[1] - uppers_y[0]
roiArray = []
for i in range(len(charactersRegions)):
    p1 = charactersRegions[i][0]
    p2 = charactersRegions[i][1]
    roi = CommonMethods.CropImageByPoints(list_subject1, p1, p2)
    img = np.zeros([roi.shape[0] + 20, roi.shape[1] + 20], dtype=np.uint8)
    img.fill(255)
    img[10:roi.shape[0] + 10, 10:roi.shape[1] + 10] = roi
    roiArray.append(img)
    #CommonMethods.ShowImageWithOriginalSize(img)

#читаем каждый символ тессерактом
for i in range(len(roiArray)):
    #ImageLoaders.SaveBWImage(roiArray[i], "c:/Temp/Photos/data/1/" + str(i) + ".bmp")
    TesseractOCR.GetTextFromImage(roiArray[i])

#CommonMethods.ShowImageWithOriginalSize(finish_image)
#CommonMethods.ShowImageWithOriginalSize(list_subject1)