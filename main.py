from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters

#работать нужно не с кропнутым изображением, а с регионом!

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\Tests4.bmp')
#find main
main = Tasks.FindMainWindow(img)
main_img = CommonMethods.CropImageFromContour(img, main)

#find filter
filter = Tasks.FindFilter(main_img)
filter_img = CommonMethods.CropImageFromContour(img, filter)
CommonMethods.ShowImage(filter_img)
#input1 = Tasks.NameInput(img, filter)