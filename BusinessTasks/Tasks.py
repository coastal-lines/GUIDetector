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

    def FindFilterTests(self):
        #find rectangles
        img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests2.bmp')
        bw = ImageConverters.ConvertToBW(img)

        gamma = 0.5
        invGamma = 1 / gamma
        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)
        bw = cv2.LUT(bw, table)

        #CommonMethods.ShowImage(bw)
        th = Threshold.AdaptiveThreshold(bw,255,11,8)
        contours, hierarchy = Countours.GetContours(th)
        Countours.DrawRectangle(contours, img)
        CommonMethods.ShowImage(img)

        #check keywords
        #save in memory as object

        #regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(bw)
        #find text in rectangle
        #for box in boundingBoxes:
        #    x, y, w, h = box;
        #    img_temp = CommonMethods.CropImage(bw, x, y, w, h)
        #    text = TesseractOCR.GetTextFromImage(img_temp)
        #    print(text)