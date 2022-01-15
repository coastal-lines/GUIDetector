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

img1 = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\Subjects\1.bmp")
img2 = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\Subjects\2.bmp")

#просто соединить два массива
vis = np.concatenate((img1, img2), axis=0)
#CommonMethods.ShowImageWithOriginalSize(vis)

#алгоритм
#накладываем одно изображение на другое, сравниваем верхние 10% изображения, если наложилость - складываем в одно большое
#нужно иметь в виду скролбары - из-за них может быть несовпадение, особенно если работаем с текстом

w,h = CommonMethods.GetImageWidthAndHeigth(img1)
w_scrollbar = 18
h_test = round(h / 10)
w_test = w - w_scrollbar

combined_image = None
result = None
for img1_y in range(h - h_test):
    for img2_y in range(h - h_test):
        roi1 = img1[img1_y:img1_y+h_test, 0:w_test]
        roi2 = img2[img2_y:img2_y+h_test, 0:w_test]
        result = (roi1==roi2).all()
        #if(img1_y > 115 and img2_y > 40):
        #    CommonMethods.ShowTwoImages(roi1, roi2)
        #print(result)

        if(result == True):
            temp = img1[0:img1_y - h_test, 0:w]
            combined_image = np.concatenate((temp, img2), axis=0)
            CommonMethods.ShowImageWithOriginalSize(combined_image)
            break

    if (result == True):
        break

#CommonMethods.ShowImageWithOriginalSize(combined_image)