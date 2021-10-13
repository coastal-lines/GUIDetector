import numpy as np

from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
from Helpers.FeatureExtractors.Contours import Countours
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters

#работать нужно не с кропнутым изображением, а с регионом!

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\FullTests2.png')
img_resized = CommonMethods.Resize(img, 1919, 1079)
height, width, channels = img.shape
w_coef = 1919 / width
h_coef = 1079 / height

def CalculateRectangle(x,y,width,heigth):
    if (w_coef > 0):
        x = round(x / w_coef)
        width = round(width / w_coef)
    if (w_coef < 0):
        x = round(x * w_coef)
        width = round(width * w_coef)
    if (h_coef > 0):
        y = round(y / h_coef)
        heigth = round(heigth / h_coef)
    if (h_coef < 0):
        y = round(y * h_coef)
        heigth = round(heigth * h_coef)

    return x,y,width,heigth

def Filter():
    x = 70
    y = 245
    width = 257
    heigth = 580

    x,y,width,heigth = CalculateRectangle(x,y,width,heigth)

    point1 = (x, y)
    point2 = (x + width, y + heigth)
    Countours.DrawRectangleByPoints(point1, point2, img)

def TestN():
    x = 80
    y = 618
    width = 225
    heigth = 44

    x, y, width, heigth = CalculateRectangle(x, y, width, heigth)

    point1 = (x, y)
    point2 = (x + width, y + heigth)
    Countours.DrawRectangleByPoints(point1, point2, img)

def TestS():
    x = 80
    y = 690
    width = 228
    heigth = 29

    x, y, width, heigth = CalculateRectangle(x, y, width, heigth)

    point1 = (x, y)
    point2 = (x + width, y + heigth)
    Countours.DrawRectangleByPoints(point1, point2, img)

def ApplyB():
    x = 80
    y = 740
    width = 230
    heigth = 37

    x, y, width, heigth = CalculateRectangle(x, y, width, heigth)

    point1 = (x, y)
    point2 = (x + width, y + heigth)
    Countours.DrawRectangleByPoints(point1, point2, img)

Filter()
TestN()
TestS()
ApplyB()
CommonMethods.ShowImage(img)