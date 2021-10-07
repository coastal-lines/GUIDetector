from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests2.bmp')
#cnt = Tasks.FindFilterTests(img)

#bw = ImageConverters.ConvertToBW(img)
#contours, hierarchy = Countours.GetContoursByCanny(bw, 0, 255)
#Countours.DrawContours(contours, img)