from Helpers.Json import JsonHelper
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
from Helpers.Json.PatternsModel import Element, LabeledData

#Step1 - upload json
json_object = JsonHelper.OpenJsonFile()

# Step2 - get element by name
def GetElementByName(element_name):
    elements_list = json_object.elements['elements']
    for i in range(len(elements_list)):
        if(elements_list[i]["name"] == element_name):
            return elements_list[i]

# Take screenshot and find contours
def GetContoursFromScreenshot():
    screenshot = CommonMethods.GetScreenshot()
    screenshot_bw = ImageConverters.ConvertToBW(screenshot)
    contours = None

    sharp = ImageFilters.Sharp(screenshot_bw)
    erosion = MorphologicalOperations.Erosion(sharp)
    blur = ImageFilters.Blur(erosion)
    ddept = cv2.CV_16S
    x = cv2.Sobel(erosion, ddept, 1, 0, ksize=3, scale=10)
    y = cv2.Sobel(erosion, ddept, 0, 1, ksize=3, scale=10)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 1)

    contoursCannyEdge, hierarchy  = Countours.GetContoursByCanny(edge, 220, 255)
    print(type(contoursCannyEdge))

    th = Threshold.AdaptiveThreshold(erosion, 255, 11, 8)
    contoursCannyThreshold, hierarchy  = Countours.GetContoursByCanny(th, 220, 255)
    print(type(contoursCannyThreshold))

    blur = ImageFilters.Blur(screenshot_bw)
    th = Threshold.InRangeThreshold(blur, 245, 255)
    contoursTh, hierarchy = Countours.GetContours(th)

    contours = contoursCannyEdge
    contours.extend(contoursCannyThreshold)
    contours.extend(contoursTh)

    #for contour in contours:
    #    x, y, w, h = cv2.boundingRect(contour)
    #    point1 = (x, y)
    #    point2 = (x + w, y + h)
    #    cv2.rectangle(screenshot, point1, point2, (25, 0, 255), 1)

    #CommonMethods.ShowImage(screenshot)
    return contours

def FindElement(element, contours):
    if(element["findBy"] == "contour"):
        best_contours = []

        # create delta for flexible search
        w = int(element["width"])
        h = int(element["heigth"])
        max_w = w + (w * 1.2)
        max_h = h + (h * 1.2)
        min_w = w - (w / 1.2)
        min_h = h - (h / 1.2)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if(w > min_w and w < max_w and h > min_h and h < max_h):
                best_contours.append(contour)

        return best_contours

    if(element["findBy"] == "pattern"):
        pass

filter_test = GetElementByName("filter_tests")
contours = GetContoursFromScreenshot()
c = FindElement(filter_test, contours)

#test
s = CommonMethods.GetScreenshot()
Countours.DrawRectangle(c, s)
CommonMethods.ShowImage(s)