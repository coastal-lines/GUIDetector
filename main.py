from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\Tests2.bmp')
cnt = Tasks.FindFilterTests(img)

img2 = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\Tests4.bmp')
cnt2 = Tasks.FindFilterTests2(img2)

img3 = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\ORB\Tests4.bmp')
contours = Tasks.FindFilterTests3(img3)

result = []
for c in contours:
    ret = cv2.matchShapes(cnt, c, 1, 0.0)
    d = Decimal(ret)
    if d < 0.07:
        result.append(d)
        x, y, w, h = cv2.boundingRect(c)
        #print(cv2.boundingRect(c))
        point1 = (x, y)
        point2 = (x + w, y + h)
        cv2.rectangle(img3, point1, point2, (0, 255, 0), 3)
        print(cv2.arcLength(c, True))

result.sort()
#print(len(result))
#print(result[0])

ret = cv2.matchShapes(cnt, cnt2, 1, 0.0)
#print("Result: ")
#print(Decimal(ret))

#
#bw = ImageConverters.ConvertToBW(img)
#contours, hierarchy = Countours.GetContoursByCanny(bw, 0, 255)
#Countours.DrawContours(contours, img)
CommonMethods.ShowImage(img3)