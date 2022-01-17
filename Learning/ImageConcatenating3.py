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
from Helpers.DrawMethods import DrawMethods
import pytesseract
import pyautogui

#take screenshot
main = CommonMethods.GetScreenshotBW()
#load pattern
img2 = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\Subjects\5.bmp")
#find pattern in the screen
x, y, w, h = PatternMatching.DetectByPatternMatchingAndReturnCoordinates(main, img2)
#detect scrollbar
roi = CommonMethods.MaskForRoi(main, x, y, w, h)
scroll_up_button = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\up_button.bmp")
scroll_down_button = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\down_button.bmp")
scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2 = ActionsForElements.FindScrollArea(ActionsForElements, roi, scroll_up_button, scroll_down_button)
#prepare roi for scrollable area (exclude scrollbar)
scrollable_area_roi_x1 = x
scrollable_area_roi_y1 = up_button_p1[1]
scrollable_area_roi_x2 = down_button_p1[0]
scrollable_area_roi_y2 = down_button_p2[1]
scrollable_area_roi_p1 = [scrollable_area_roi_x1, scrollable_area_roi_y1]
scrollable_area_roi_p2 = [scrollable_area_roi_x2, scrollable_area_roi_y2]
#DrawMethods.DrawRectangleByPoints(main, scrollable_area_roi_p1, scrollable_area_roi_p2)
#get centre of scrollbar
centre_scrollbar = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\Subjects\6.bmp")
centre_scrollbar_p1, centre_scrollbar_p2 = PatternMatching.DetectByPatternMatching(roi, centre_scrollbar)
#move down 200px
ActionsForElements.ClickOnTheCentreOfTheElement(ActionsForElements, centre_scrollbar_p1, centre_scrollbar_p2)
pyautogui.mouseDown()
pyautogui.moveTo(centre_scrollbar_p1[0], centre_scrollbar_p1[1] + 200, 2)
pyautogui.mouseUp()
#combine the first screenshot and new roi
screenshot2 = CommonMethods.GetScreenshotBW()
screenshot2_roi = screenshot2[y:scrollable_area_roi_y2, x:scrollable_area_roi_x2]
roi_1 = roi[y:scrollable_area_roi_y2, x:scrollable_area_roi_x2]
roi_2 = screenshot2_roi[-200:, 0:]
combined_image = np.concatenate((roi_1, roi_2), axis=0)
CommonMethods.ShowImageWithOriginalSize(combined_image)