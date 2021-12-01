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

class Element():
    def __init__(self, img_bw, point1, point2):
        self.img_bw = img_bw
        self.point1 = point1
        self.point2 = point2



def GetBwImage(name):
    element = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\{}'.format(name))
    element_bw = ImageConverters.ConvertToBW(element)
    return element_bw

def GetScreenshot():
    screenshot = pyautogui.screenshot()
    open_cv_image = np.array(screenshot)
    return open_cv_image

def FindContournsByDifferentWays(img_bw):
    contours = None

    sharp = ImageFilters.Sharp(img_bw)
    erosion = MorphologicalOperations.Erosion(sharp)
    blur = ImageFilters.Blur(erosion)
    ddept = cv2.CV_16S
    x = cv2.Sobel(erosion, ddept, 1, 0, ksize=3, scale=10)
    y = cv2.Sobel(erosion, ddept, 0, 1, ksize=3, scale=10)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 1)

    contoursCannyEdge, hierarchy  = Countours.GetContoursByCanny(edge, 220, 255)

    th = Threshold.AdaptiveThreshold(erosion, 255, 11, 8)
    contoursCannyThreshold, hierarchy  = Countours.GetContoursByCanny(th, 220, 255)

    blur = ImageFilters.Blur(img_bw)
    th = Threshold.InRangeThreshold(blur, 245, 255)
    contoursTh, hierarchy = Countours.GetContours(th)

    contours = contoursCannyEdge
    contours.extend(contoursCannyThreshold)
    contours.extend(contoursTh)

    return contours

def ComparePixelByPixel(pattern, roi):
    range_value = 128

    pattern_resized = CommonMethods.Resize(pattern, range_value, range_value)
    roi_resized = CommonMethods.Resize(roi, range_value, range_value)

    matches = 0
    for i in range(range_value):
        for j in range(range_value):
            if (pattern_resized[i][j] == roi_resized[i][j]):
                matches += 1

    return matches

def GetBordersForElement(element):
    h, w = element.shape[:2]
    high_w = w + (w * 1.5)
    high_h = h + (h * 1.5)
    low_w = w - (w / 1.5)
    low_h = h - (h / 1.5)
    return high_w, high_h, low_w, low_h

def Comparing(contours, element, mainScreen):
    pattern_matches = [{}]
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        #cv2.rectangle(mainScreen, point1, point2, (25, 0, 255), 1)

        high_w, high_h, low_w, low_h = GetBordersForElement(element)
        if (w > low_w and w < high_w and h > low_h and h < high_h):
            roi = CommonMethods.CropImage(mainScreen, x, y, w, h)
            matches = ComparePixelByPixel(element, roi)
            point1 = (x, y)
            point2 = (x + w, y + h)
            pattern_matches.append([matches, point1, point2])
            #print(matches)
            #print(point1)
            #print(point2)

    return pattern_matches

def GetTheBestContourMatch(pattern_matches, bestPosition):
    tempMatch = []

    for i in range(len(pattern_matches)):
        if i != 0:
            tempMatch.append(pattern_matches[i][0])

    tempMatch.sort(reverse=True)
    maxMatch = tempMatch[bestPosition]
    #print("maxMatch:")
    #print(maxMatch)

    for i in range(len(pattern_matches)):
        if (i != 0) and (pattern_matches[i][0] == maxMatch):
        #if(pattern_matches[i][0] == maxMatch):
            return pattern_matches[i][1], pattern_matches[i][2]

def GetPointsOfTheBestMatch(contours, element, Screen, bestPosition):
    element_matches = Comparing(contours, element, Screen)
    point1, point2 = GetTheBestContourMatch(element_matches, bestPosition)
    return point1, point2

def SearchElement(contours, element, screenshot, bestPosition):
    point1, point2 = GetPointsOfTheBestMatch(contours, element, screenshot, bestPosition)
    el = Element(element, point1, point2)
    return el

def GetCropComparison(el, pattern):
    pattern_w = pattern.shape[:2][1]
    pattern_h = pattern.shape[:2][0]
    roi_w = pattern.shape[:2][1]
    roi_h = pattern.shape[:2][0]
    X1 = el.point2[:2][0] - pattern_w
    Y1 = el.point2[:2][1] - pattern_h

    if(X1 > 0 and Y1 > 0):
        roi = CommonMethods.CropImage(screenshot_bw, X1, Y1, roi_w, roi_h)
        roi_resized = CommonMethods.Resize(roi, pattern_w, pattern_h)

        matches = 0
        for i in range(pattern_h):
            for j in range(pattern_w):
                if (pattern[i][j] == roi_resized[i][j]):
                    matches += 1
        print(matches)

def SearchBest10Mathces(contours, element, screenshot, customRange):
    element_matches = Comparing(contours, element, screenshot)

    position = 0
    for m in range(len(element_matches[:customRange])):
            if(position == 0):
                point1, point2 = GetTheBestContourMatch(element_matches, position)
                el = Element(element, point1, point2)
                Countours.DrawRectangleByPoints(el.point1, el.point2, screen, (0, 60, 255), 4)
                GetCropComparison(el, Subject)
                position += 1
                continue

            point1, point2 = GetTheBestContourMatch(element_matches, position)
            el = Element(element, point1, point2)
            GetCropComparison(el, Subject)

            #Countours.DrawRectangleByPoints(el.point1, el.point2, screen, (255, 60, 255), 4)
            if(position == 11):
                GetCropComparison(el, Subject)
                cv2.putText(screen, str(position), (el.point1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 5, 25), 2, cv2.LINE_AA)

            position += 1


#find subject list
screen = GetScreenshot()
screenshot_bw = ImageConverters.ConvertToBW(screen)
sharp = ImageFilters.Sharp(screenshot_bw)
erosion = MorphologicalOperations.Erosion(sharp)

contours = FindContournsByDifferentWays(erosion)
Subject = GetBwImage('Subject.bmp')
#Subject_element = SearchElement(contours, Subject, erosion, 0)
#Countours.DrawRectangleByPoints(Subject_element.point1, Subject_element.point2, screen, (255, 60, 255), 4)
SearchBest10Mathces(contours, Subject, erosion, 17)
CommonMethods.ShowImage(screen)
