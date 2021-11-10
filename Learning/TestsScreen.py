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

def GetBwImage(name):
    element = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\{}'.format(name))
    element_bw = ImageConverters.ConvertToBW(element)
    return element_bw

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

def GetBordersForElement(element):
    h, w = element.shape[:2]
    high_w = w + (w * 1.5)
    high_h = h + (h * 1.5)
    low_w = w - (w / 1.5)
    low_h = h - (h / 1.5)
    return high_w, high_h, low_w, low_h

def ComparePixelByPixel(pattern, roi):
    range_value = 512

    pattern_resized = CommonMethods.Resize(pattern, range_value, range_value)
    roi_resized = CommonMethods.Resize(roi, range_value, range_value)

    matches = 0
    for i in range(range_value):
        for j in range(range_value):
            if (pattern_resized[i][j] == roi_resized[i][j]):
                matches += 1

    return matches

def Comparing(contours, element, mainScreen):
    pattern_matches = [{}]
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        point1 = (x, y)
        point2 = (x + w, y + h)
        cv2.rectangle(mainScreen, point1, point2, (25, 0, 255), 1)

        high_w, high_h, low_w, low_h = GetBordersForElement(element)
        if (w > low_w and w < high_w and h > low_h and h < high_h):
            roi = CommonMethods.CropImage(mainScreen, x, y, w, h)
            matches = ComparePixelByPixel(element, roi)
            pattern_matches.append([matches, point1, point2])
            print(matches)
            #print(point1)
            #print(point2)

    return pattern_matches

def GetTheBestContourMatch(pattern_matches):
    tempMatch = []

    for i in range(len(pattern_matches)):
        if i != 0:
            tempMatch.append(pattern_matches[i][0])

    tempMatch.sort(reverse=True)
    maxMatch = tempMatch[0]


    for i in range(len(pattern_matches)):
        if (i != 0) and (pattern_matches[i][0] == maxMatch):
        #if(pattern_matches[i][0] == maxMatch):
            return pattern_matches[i][1], pattern_matches[i][2]

def GetPointsOfTheBestMatch(contours, element, Screen):
    element_matches = Comparing(contours, element, Screen)
    point1, point2 = GetTheBestContourMatch(element_matches)
    return point1, point2

ApplyFilter = GetBwImage('ApplyFilter.bmp')
CreateTest = GetBwImage('CreateTest.bmp')
DeleteTest = GetBwImage('DeleteTest.bmp')
DeliveredOnPaper = GetBwImage('DeliveredOnPaper.bmp')
DeliveredOnScreen = GetBwImage('DeliveredOnScreen.bmp')
Draft = GetBwImage('Draft.bmp')
EditTest = GetBwImage('EditTest.bmp')
FilterTests = GetBwImage('FilterTests.bmp')
Live = GetBwImage('Live.bmp')
Page = GetBwImage('Page.bmp')
ResetFilters = GetBwImage('ResetFilters.bmp')
Retired = GetBwImage('Retired.bmp')
Subject = GetBwImage('Subject.bmp')
Table = GetBwImage('Table.bmp')
TestDateRange = GetBwImage('TestDateRange.bmp')
TestName = GetBwImage('TestName.bmp')
TestReference = GetBwImage('TestReference.bmp')
Screen = GetBwImage('Screen.bmp')

contours = FindContournsByDifferentWays(Screen)
point1, point2 = GetPointsOfTheBestMatch(contours, CreateTest, Screen)

image = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\Screen.bmp')
Countours.DrawRectangleByPoints(point1, point2, image, (255, 60, 255), 4)

CommonMethods.ShowImage(image)