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

class Element:
    def __init__(self, img_bw, point1, point2, element):
        self.roi = img_bw
        self.point1 = point1
        self.point2 = point2
        self.rawElement = element

#Debug
#instead of using the screenshot
main_screen = ImageLoaders.LoadImage("C:\Temp\Photos\Tests2.bmp")
main_screen_bw = ImageLoaders.LoadBWImage("C:\Temp\Photos\Tests2.bmp")

#Step1 - upload json
json_object = JsonHelper.OpenJsonFile()

# Step2 - get element by name
def GetElementByName(element_name):
    elements_list = json_object.elements['elements']
    for i in range(len(elements_list)):
        if(elements_list[i]["name"] == element_name):
            return elements_list[i]

# Step 3 - find some elements by pattern
#find object
filter_test = GetElementByName("filter_tests")
filter_test_bw = ImageLoaders.LoadBWImage(filter_test["ImagePath"])
p1, p2 = PatternMatching.DetectByPatternMatching(main_screen_bw, filter_test_bw)
masked_filter_test_bw = CommonMethods.MaskForRoiFromPoints(main_screen_bw, p1, p2)
element_filter_test = Element(masked_filter_test_bw, p1, p2, filter_test)
Contours.DrawRectangleByPointsAndPrintText(main_screen, p1, p2, filter_test["name"])

#find nested object
draft = GetElementByName("draft")
draft_bw = ImageLoaders.LoadBWImage(draft["ImagePath"])
p3, p4 = PatternMatching.DetectByPatternMatching(element_filter_test.roi, draft_bw)
element_draft = Element(None, p3, p4, draft)
#Contours.DrawRectangleByPointsAndPrintText(main_screen, p3, p4, draft["name"])

# Step 4 - find the dropdown and read all items from this
subject = GetElementByName("subject")
subject_bw = ImageLoaders.LoadBWImage(subject["ImagePath"])
#find dropdown button - TODO
p5, p6 = PatternMatching.DetectByPatternMatching(element_filter_test.roi, subject_bw)
element_subject = Element(None, p5, p6, subject)
#Contours.DrawRectangleByPointsAndPrintText(main_screen, p5, p6, subject["name"])
#ActionsForElements.ClickOnTheCentreOfTheElement(p5, p6)
list_subject = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects2.bmp")
p7, p8 = PatternMatching.DetectByPatternMatching(element_filter_test.roi, list_subject)
Contours.DrawRectangleByPointsAndPrintText(main_screen, p7, p8, "list")


#Debug
#test
CommonMethods.ShowImage(main_screen)