from Helpers import Gradients
from Helpers.Json import JsonHelper
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
from Helpers.Json.PatternsModel import Element, LabeledData

main = ImageLoaders.LoadImage(r"C:\Temp2\Flash\MyLabeling\Tests.bmp")
main_bw = ImageConverters.ConvertToBW(main)

#sobel = Gradients.Sobel(main_bw)
#scharr = Gradients.Scharr(main_bw)
sharp = ImageFilters.Sharp(main_bw)
laplasian = Gradients.Laplasian(sharp)

dilate = MorphologicalOperations.Dilation(laplasian)
result = cv2.addWeighted(laplasian, 0.9, dilate, 0.1, 0.0)

contours, hierarchy = Contours.GetContours(result)
Contours.DrawRectangle(contours, main)

#scharr = Gradients.Scharr(dilate)
#laplasian = Gradients.Laplasian(dilate)
#CommonMethods.ShowImage(dilate)
#CommonMethods.ShowImage(scharr)
CommonMethods.ShowImage(main)