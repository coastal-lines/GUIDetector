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
width = 257
heigth = 580
x = 70
y = 245
point1 = (x, y)
point2 = (x + width, y + heigth)
Countours.DrawRectangleByPoints(point1, point2, img_resized)
CommonMethods.ShowImage(img_resized)