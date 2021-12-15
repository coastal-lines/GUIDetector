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
import cv2 as cv

main_screen = ImageLoaders.LoadImage("C:\Temp\Photos\Tests2.bmp")
main_screen_bw = ImageLoaders.LoadBWImage("C:\Temp\Photos\Tests2.bmp")
list_subject = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects2.bmp")
result = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(main_screen_bw, list_subject)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
x = max_loc[0]
y = max_loc[1]
w, h = CommonMethods.GetImageWidthAndHeigth(list_subject)
point1 = (x, y)
point2 = (x + w, y + h)
Contours.DrawRectangleByPoints(main_screen, point1, point2)
CommonMethods.ShowImage(result)
CommonMethods.ShowImage(main_screen)