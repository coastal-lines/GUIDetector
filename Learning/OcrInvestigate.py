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

img = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\c5.bmp")

def ocr(img, type):
    pytesseract.pytesseract.tesseract_cmd = r'c:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img, lang='eng', config="-c tessedit_char_whitelist=!?#@abc")
    print(type + ": " + text)

def original():
    ocr(img, "original")

def resized():
    resize = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    ocr(resize, "resize")

def negative():
    negative = ImageConverters.ConvertImageToNegative(img)
    ocr(negative, "negative")

def sharp():
    sharp = ImageFilters.Sharp(img)
    ocr(sharp, "sharp")

def negativeAndResize():
    negative = ImageConverters.ConvertImageToNegative(img)
    resize = cv2.resize(negative, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    ocr(resize, "negative resize")

def negativeResizeSharp():
    negative = ImageConverters.ConvertImageToNegative(img)
    resize = cv2.resize(negative, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    sharp = ImageFilters.Sharp(resize)
    ocr(sharp, "negative resize sharp")

def transform():
    transform = cv2.resize(img, None, fx=2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    ocr(transform, "transform")

def treshold():
    tr = Threshold.BinaryThreshold(img, 128, 255)
    negative = ImageConverters.ConvertImageToNegative(tr)
    ocr(negative, "treshold")

def blur():
    #WORK!
    #blur = ImageFilters.Blur(C:\Temp\Photos\data\list_subjects5.bmp)
    #blur = ImageFilters.Blur(blur)
    th = Threshold.AdaptiveThreshold(img, 255, 7, 11)
    blur = ImageFilters.Blur(th)
    ocr(blur, "blur")

#CommonMethods.ShowImageWithOriginalSize(negative)

original()
resized()
negative()
sharp()
negativeAndResize()
negativeResizeSharp()
transform()
treshold()
blur()