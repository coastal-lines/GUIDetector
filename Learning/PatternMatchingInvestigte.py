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

main_screen = ImageLoaders.LoadImage("C:\Temp\Photos\Tests2.bmp")
main_screen_bw = ImageLoaders.LoadBWImage("C:\Temp\Photos\Tests2.bmp")
list_subject = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects2.bmp")
p7, p8 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(main_screen_bw, list_subject)
Contours.DrawRectangleByPointsAndPrintText(main_screen, p7, p8, "list")
CommonMethods.ShowImage(main_screen)