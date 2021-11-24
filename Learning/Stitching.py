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
from Helpers import ContourHelper
import pyautogui

def GetCentreOfElement(p1, p2):
    x = p2[0] - ((p2[0] - p1[0]) / 2)
    y = p2[1] - ((p2[1] - p1[1]) / 2)
    return x, y

def OpenSubjects(screenshot_bw):
    subject_pattern = ImageLoaders.LoadImage(r"C:\Temp\!my\TestsTab\FullTest\Subject.bmp")
    subject_pattern_bw = ImageConverters.ConvertToBW(subject_pattern)
    p1, p2 = PatternMatching.DetectByPatternMatching(screenshot_bw, subject_pattern_bw)
    x, y = GetCentreOfElement(p1, p2)
    pyautogui.click(x, y)

def GetRoiFromSubject(screenshot):
    sharp = ImageFilters.Sharp(screenshot)
    er = MorphologicalOperations.Erosion(sharp)
    th = Threshold.BinaryThreshold(er, 150, 255)
    dl = MorphologicalOperations.Dilation(th)
    #CommonMethods.ShowImageWithOriginalSize(dl)

    contours, hierarchy = Countours.GetContoursByCanny(dl, 0, 255)

    my_contour = None
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        #cv2.rectangle(screenshot, (x, y), (x + w, y + h), (255, 50, 0), 4)
        if(w > 30 and h > 30 and w < 300 and h < 200):
            #cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 4)
            my_contour = contour

    #CommonMethods.ShowImageWithOriginalSize(screenshot)
    return my_contour

def GetTextFromRoi(screenshot_bw, my_contour):
    roi = CommonMethods.CropImageFromContour(screenshot_bw, my_contour)
    roi_negative = ImageConverters.ConvertImageToNegative(roi)
    text = TesseractOCR.GetTextFromImage(roi_negative)
    text_array = text.splitlines()
    return text_array

def GetLastWord(text_array):
    text_array_cleaned = []
    for i in range(len(text_array)):
        if text_array[i] != "" and text_array[i] != "\n" and text_array[i] != " ":
            text_array_cleaned.append(text_array[i])

    return text_array_cleaned[-1]

#search scroll inside roi
def GetCenterOfScrolldownButton(my_contour):
    roi = CommonMethods.MaskForRoiFromContour(screenshot_bw, my_contour)
    scrollUpPattern = cv2.imread(r'c:\Temp\!my\AuditTab\buttonUP.png', 0)
    scrollDownPattern = cv2.imread(r'c:\Temp\!my\AuditTab\buttonDOWN.png', 0)
    p1, p2 = PatternMatching.DetectByPatternMatching(screenshot_bw, scrollUpPattern)
    p3, p4 = PatternMatching.DetectByPatternMatching(screenshot_bw, scrollDownPattern)
    Countours.DrawRectangleByPoints(p1, p2, screenshot, [255,0,255], 2)
    Countours.DrawRectangleByPoints(p3, p4, screenshot, [255,0,255], 2)
    return GetCentreOfElement(p3, p4)

def GetfilterRoi(screenshot, screenshot_bw):
    filter_pattern = ImageLoaders.LoadImage(r'C:\Temp\!my\TestsTab\FullTest\FilterTests.bmp')
    filter_pattern_bw = ImageConverters.ConvertToBW(filter_pattern)
    filter_p1, filter_p2 = ContourHelper.SearchObjectByContourAndPixelComparing(screenshot_bw, filter_pattern_bw)
    filter_roi = CommonMethods.MaskForRoiFromPoints(screenshot, filter_p1, filter_p2)
    filter_roi_bw = ImageConverters.ConvertToBW(filter_roi)
    crop = CommonMethods.CropImageByPoints(screenshot_bw, filter_p1, filter_p2 )
    return filter_roi_bw, crop

def ExpandFilter(filter_roi_bw):
    subject_pattern = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\Subject.bmp')
    subject_pattern_bw = ImageConverters.ConvertToBW(subject_pattern)
    subject_p1, subject_p2 = PatternMatching.DetectByPatternMatching(filter_roi_bw, subject_pattern_bw)
    subject_x, subject_y = GetCentreOfElement(subject_p1, subject_p2)
    pyautogui.click(subject_x, subject_y)

def GetsubjectListArea(filter_roi_bw, screenshot):
    my_contour = GetRoiFromSubject(filter_roi_bw, screenshot)
    return my_contour

def LastWord():
    screenshot = CommonMethods.GetScreenshot()
    screenshot_bw = ImageConverters.ConvertToBW(screenshot)
    my_contour = GetRoiFromSubject(screenshot_bw)
    my_contour_roi = CommonMethods.ExtendedMaskForRoiFromContour(screenshot_bw, my_contour)

    screenshot = CommonMethods.GetScreenshot()
    screenshot_bw = ImageConverters.ConvertToBW(screenshot)
    text_array = GetTextFromRoi(screenshot_bw, my_contour)
    last_word = GetLastWord(text_array)
    print(last_word)
    return  my_contour_roi

screenshot = CommonMethods.GetScreenshot()
screenshot_bw = ImageConverters.ConvertToBW(screenshot)
filter_roi_bw, filter_crop = GetfilterRoi(screenshot, screenshot_bw)
ExpandFilter(filter_roi_bw)
my_contour_roi = LastWord()


scrollDownPattern = cv2.imread(r'c:\Temp\!my\AuditTab\buttonDOWN.png', 0)
point1, point2 = PatternMatching.DetectByPatternMatching(my_contour_roi, scrollDownPattern)
s = CommonMethods.GetScreenshot()
Countours.DrawRectangleByPoints(point1, point2, s, [255,0,255], 2)
x, y = GetCentreOfElement(point1, point2)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)
pyautogui.click(x, y)

LastWord()