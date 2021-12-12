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
from Helpers.Json.PatternsModel import Element, LabeledData
from Helpers.PatternMatching.PatternMatching import PatternMatching

#Debug
#instead of using the screenshot
main_screen = ImageLoaders.LoadBWImage("C:\Temp\Photos\Tests.bmp")

#Step1 - upload json
json_object = JsonHelper.OpenJsonFile()

# Step2 - get element by name
def GetElementByName(element_name):
    elements_list = json_object.elements['elements']
    for i in range(len(elements_list)):
        if(elements_list[i]["name"] == element_name):
            return elements_list[i]


element_filter_test = GetElementByName("filter_tests")
filter_test_bw = ImageLoaders.LoadBWImage(element_filter_test["ImagePath"])
p1, p2 = PatternMatching.DetectByPatternMatching(main_screen, filter_test_bw)
element_filter_test["TestData"]

#Debug
#test
Contours.DrawRectangleByPointsAndPrintText(main_screen, p1, p2, element_filter_test["name"])
CommonMethods.ShowImage(main_screen)