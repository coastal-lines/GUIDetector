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
import pytesseract

list_subject1 = ImageLoaders.LoadBWImage(r"C:\Temp\!my\TestsTab\Subjects\subj2.bmp")

#H, W = list_subject1.shape[:2]
#new_img = np.zeros([H, W * 3], dtype = np.uint8)
#new_img.fill(255)
#new_img[0:H, W:W + W] = list_subject1

resize = cv2.resize(list_subject1, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
sharp = ImageFilters.Sharp(resize)
negative = ImageConverters.ConvertImageToNegative(sharp)
pytesseract.pytesseract.tesseract_cmd = r'c:\Temp\tesseract\tesseract.exe'
text = pytesseract.image_to_string(negative, lang='eng')
print(text)

CommonMethods.ShowImageWithOriginalSize(negative)