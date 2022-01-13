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

w,h = CommonMethods.GetImageWidthAndHeigth(img1)
h_test = round(h / 10)
w_test = w

combined_image = None
for y in range(h):
    result = (img1[y:y+h_test, 0:w_test]==img2[y:y+h_test, 0:w_test]).all()
    print(result)

    if(result == True):
        temp = img2[y:h, 0:w_test]
        combined_image = np.concatenate((img1, temp), axis=0)
        break

CommonMethods.ShowImageWithOriginalSize(combined_image)