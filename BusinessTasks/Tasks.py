from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.ImageConverters import ImageConverters
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.CommonMethods import CommonMethods
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.Threshold import Threshold
import cv2
import numpy as np
import math

class Tasks():

    def FindFilterTests(img):
        #find rectangles
        #img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests6.bmp')
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.InRangeThreshold(blur,245,255)#(blur,200,11,8)
        contours, hierarchy = Countours.GetContours(th)
        cnt = Countours.DrawRectangle2(contours, img)
        #CommonMethods.ShowImage(img)
        return cnt

    def FindFilterTests2(img):
        # find rectangles
        # img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests6.bmp')
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.InRangeThreshold(blur, 245, 255)  # (blur,200,11,8)
        contours, hierarchy = Countours.GetContours(th)
        cnt = Countours.DrawRectangle3(contours, img)
        #CommonMethods.ShowImage(img)
        return cnt


        #check keywords
        #save in memory as object

        #regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(bw)
        #find text in rectangle
        #for box in boundingBoxes:
        #    x, y, w, h = box;
        #    img_temp = CommonMethods.CropImage(bw, x, y, w, h)
        #    text = TesseractOCR.GetTextFromImage(img_temp)
        #    print(text)