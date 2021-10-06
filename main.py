from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.CommonMethods import CommonMethods
from Helpers.ImageConverters import ImageConverters
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests2.bmp')
cnt = Tasks.FindFilterTests(img)

img2 = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\Tests.bmp')
cnt2 = Tasks.FindFilterTests2(img2)

ret = cv2.matchShapes(cnt, cnt2, 1, 0.0)
print(ret)
print(Decimal(ret))

#
#bw = ImageConverters.ConvertToBW(img)
#contours, hierarchy = Countours.GetContoursByCanny(bw, 0, 255)
#Countours.DrawContours(contours, img)
#CommonMethods.ShowImage(img)