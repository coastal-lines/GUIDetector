from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\Tests2.bmp')
Tasks.FindMainWindow(img)