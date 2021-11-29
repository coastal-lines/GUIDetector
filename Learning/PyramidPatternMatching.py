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
from Helpers import ContourHelper
import pyautogui

#нужно попробовать изменять размер не скриншота, а паттерна
#например, мы знаем, что паттерн был сделан с экрана 1600*1200, а текущий экран 1920*1200
#соответственно, можно с определенной дельтой создать несколько паттернов, которые будут близки к масштабу 1920*1200
#так же можно добавить дополнительную проверку мета данных - текст, цвет и т.п.
#пример ниже меняет размер скриншота, что на практике не особо работает и ресурсозатратно т.к. изображение большое

def TryfindPattern1(original_gray_image, pattern_gray_image):
    images = []
    h_original, w_original = original_gray_image.shape

    p = 10 #шаг уменьшения 10%
    for i in range(7): #семь раз уменьшаем изображение
        w_temp = round(w_original - ((w_original / 100) * p))
        h_temp = round(h_original - ((h_original / 100) * p))
        dim = (w_temp, h_temp)
        resized_image = cv2.resize(original_gray_image, dim)
        images.append(resized_image)
        p = p + 10

    for i in range(7): #семь раз увеличиваем изображение
        w_temp = round(w_original + ((w_original / 100) * p))
        h_temp = round(h_original + ((h_original / 100) * p))
        dim = (w_temp, h_temp)
        resized_image = cv2.resize(original_gray_image, dim)
        images.append(resized_image)
        p = p + 10

    listMathches = []
    listResults = []
    for i in range(len(images)):
        #print(images[i].shape)
        img = images[i]
        h_image, w_image = img.shape
        temp_image = images[i]
        h_pattern, w_pattern = pattern_gray_image.shape

        if(h_image > h_pattern and w_image > w_pattern):
            res = cv2.matchTemplate(temp_image, pattern_gray_image, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            listMathches.append(min_val)
            listResults.append(res)

    listMathches.sort()
    print("The minimal result is: " + str(listMathches[0]))
    minResult = None
    result_position = None
    for i in range(len(listResults)):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(listResults[i])
        if(min_val == listMathches[0]):
            minResult = listResults[i]
            result_position = i

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(minResult)
    x = min_loc[0]
    y = min_loc[1]
    p1 = (x, y)
    p2 = (x + w_pattern, y + h_pattern)
    Countours.DrawRectangleByPoints(p1, p2, images[result_position], [0,255,0], 4)
    #CommonMethods.ShowImage(images[result_position])

    h_min, w_min = images[result_position].shape

    x_orig = round(x * (w_original / w_min)) + 5 #из-за окргуления приходиться добавлять
    y_orig = round(y * (h_original / h_min)) + 5

    point1 = (x_orig, y_orig)
    point2 = (x_orig + w_pattern, y_orig + h_pattern)
    Countours.DrawRectangleByPoints(point1, point2, original_gray_image, [0, 0, 0], 3)
    CommonMethods.ShowImage(original_gray_image)

def TryFindPattern2(original_gray_image, pattern_gray_image):
    images = []
    h_pattern, w_pattern = pattern_gray_image.shape

    p = 10 #шаг уменьшения 10%
    for i in range(7): #семь раз уменьшаем изображение
        w_temp = round(w_pattern - ((w_pattern / 100) * p))
        h_temp = round(h_pattern - ((h_pattern / 100) * p))
        dim = (w_temp, h_temp)
        resized_image = cv2.resize(original_gray_image, dim)
        images.append(resized_image)
        p = p + 10

    for i in range(7): #семь раз увеличиваем изображение
        w_temp = round(w_pattern + ((w_pattern / 100) * p))
        h_temp = round(h_pattern + ((h_pattern / 100) * p))
        dim = (w_temp, h_temp)
        resized_image = cv2.resize(original_gray_image, dim)
        images.append(resized_image)
        p = p + 10

screenshot = CommonMethods.GetScreenshot()
screenshot_bw = ImageConverters.ConvertToBW(screenshot)
subject_pattern = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\Subject.bmp')
subject_pattern_bw = ImageConverters.ConvertToBW(subject_pattern)
TryFindPattern2(screenshot_bw, subject_pattern_bw)