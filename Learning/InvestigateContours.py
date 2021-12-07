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
from Helpers.FeatureExtractors import Contours
import pyautogui

#load
main = ImageLoaders.LoadImage(r"C:\Temp2\Flash\MyLabeling\Tests.bmp")
main_bw = ImageConverters.ConvertToBW(main)

#filters
sharp = ImageFilters.Sharp(main_bw)
erosion = MorphologicalOperations.Erosion(sharp)

#sobel


#test
CommonMethods.ShowImage(erosion)