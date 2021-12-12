import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
from Helpers.FeatureExtractors.Contours import Contours
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.FeatureExtractors import Contours
import pyautogui

#нужно попробовать изменять размер не скриншота, а паттерна
#например, мы знаем, что паттерн был сделан с экрана 1600*1200, а текущий экран 1920*1200
#соответственно, можно с определенной дельтой создать несколько паттернов, которые будут близки к масштабу 1920*1200
#так же можно добавить дополнительную проверку мета данных - текст, цвет и т.п.
#пример ниже меняет размер скриншота, что на практике не особо работает и ресурсозатратно т.к. изображение большое

#Step1 - upload json
json_object = JsonHelper.OpenJsonFile()

pattern = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\Screen.bmp')
pattern_bw = ImageConverters.ConvertToBW(pattern)
subject_pattern = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\FilterTests.bmp')
subject_pattern_bw = ImageConverters.ConvertToBW(subject_pattern)
PatternMatching.FindPatternAndDrawRectange(pattern_bw, subject_pattern_bw)
CommonMethods.ShowImage(pattern_bw)