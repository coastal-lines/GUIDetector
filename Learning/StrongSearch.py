from Helpers.FeatureExtractors.ORB import ORB
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

def GetScreenshot():
    screenshot = pyautogui.screenshot()
    open_cv_image = np.array(screenshot)
    return open_cv_image

def GetBwImage(name):
    element = ImageLoaders.LoadImage(r'c:\Temp\!my\TestsTab\FullTest\{}'.format(name))
    return element

screen = GetScreenshot()
screenshot_bw = ImageConverters.ConvertToBW(screen)
Subject = GetBwImage('FilterTests.bmp')
Subject_bw = ImageConverters.ConvertToBW(Subject)

trainKeypointsSubject, trainDescriptorsSubject = ORB.PrepareKeypointsAndDescriptorsByORB(Subject_bw)
queryKeypointsScreen, queryDescriptorsScreen = ORB.PrepareKeypointsAndDescriptorsByORB(screenshot_bw)
matches = ORB.PrepareMatchesByBFMatcher(queryDescriptorsScreen, trainDescriptorsSubject)
ORB.ShowORBMatchesBetweenTwoImages(Subject, trainKeypointsSubject, screen, queryKeypointsScreen, matches)

