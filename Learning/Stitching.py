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
import pyautogui

def GetCentreOfElement(p1, p2):
    x = p2[0] - ((p2[0] - p1[0]) / 2)
    y = p2[1] - ((p2[1] - p1[1]) / 2)
    return x, y

screenshot = CommonMethods.GetScreenshot()
screenshot_bw = ImageConverters.ConvertToBW(screenshot)
subject_pattern = ImageLoaders.LoadImage(r"C:\Temp\!my\TestsTab\FullTest\Subject.bmp")
subject_pattern_bw = ImageConverters.ConvertToBW(subject_pattern)
p1, p2 = PatternMatching.DetectByPatternMatching(screenshot_bw, subject_pattern_bw)
x, y = GetCentreOfElement(p1, p2)
pyautogui.click(x, y)
u=0