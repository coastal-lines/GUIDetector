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

#load screen
main_screen = ImageLoaders.LoadImage("C:\Temp\Photos\Tests2.bmp")
main_screen_bw = ImageLoaders.LoadBWImage("C:\Temp\Photos\Tests2.bmp")

#find list
list_subject = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects2.bmp")
p1, p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(main_screen_bw, list_subject)
#Contours.DrawRectangleByPoints(main_screen, p1, p2)

#find scroll in roi
list_roi = CommonMethods.MaskForRoiFromPoints(main_screen_bw, p1, p2)
up_button = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\up_button.bmp")
down_button = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\down_button.bmp")
up_button_p1, up_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(main_screen_bw, up_button)
down_button_p1, down_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(main_screen_bw, down_button)
Contours.DrawRectangleByPoints(main_screen, up_button_p1, up_button_p2)
Contours.DrawRectangleByPoints(main_screen, down_button_p1, down_button_p2)

CommonMethods.ShowImage(main_screen)