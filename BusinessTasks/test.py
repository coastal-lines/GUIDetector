import math
import cv2 as cv
import numpy as np
import pytesseract

class GuiObject():
    def __init__(self, img, x, y, w, h):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class TableObject():
    def __init__(self, img, x, y, w, h, verticalLines, horizontalLines):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.verticalLines = verticalLines
        self.horizontalLines = horizontalLines

class VerticalLines():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class HorizontalLines():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

#img_bgr = cv.imread(r'C:\Temp\!my\AuditTab\Screenshot_1.png')
#img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
#img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)

def SaveFile(img):
    cv.imwrite(r'C:\Temp\!my\Test.png', img)

def CropImage(img, x, y, w, h):
    crop_img = img[y:y+h, x:x+w]
    #print("I'm cropping" + " " + str(x))
    return crop_img

def GetGrayImage(img):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    return img_gray


def GetOriginalCoordinates(obj1, obj2):
    pass

img = cv.imread(r"C:\Temp2\Flash\MyLabeling\Table1.png")
#img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#cv.imwrite(r'C:\Temp\!my\Test.png', img_gray)

def upContast():
    pass
    #hsv = cv.cvtColor(img_rgb, cv.COLOR_BGR2HSV)
    #hsv[:, :, 2] = cv.equalizeHist(hsv[:, :, 2])
    #eq_color_gorilla = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
    #show_pic(img_rgb)
    #show_pic(eq_color_gorilla)

def cropImage(img, x, y, w, h):
    crop_img = img[y:y+h, x:x+w]
    #print("I'm cropping" + " " + str(x))
    return crop_img

def findTableArea(img_gray):
    img_gr = img_gray.copy()
    ret, thresh1 = cv.threshold(img_gr, 230, 255, cv.THRESH_BINARY)
    #th2 = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 4)
    contours, hierarchy = cv.findContours(thresh1, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        point1 = (x, y)
        point2 = (x + w, y + h)
        if (h > 400) and (w < 1900):
            #cv.rectangle(img, point1, point2, (0, 255, 0), 1)
            crop = cropImage(img_gr, x, y, w, h)
            return crop, x, y, w, h

def findRows(img):
    ret, thresh_value = cv.threshold(img, 230, 255, cv.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    dilated_value = cv.dilate(thresh_value, kernel, iterations=1)
    contours, hierarchy = cv.findContours(dilated_value, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    lines = cv.HoughLinesP(contours, 1, math.pi / 2, 2, None, 30, 1);
    cordinates = []
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        cordinates.append((x, y, w, h))
        # bounding the images
        if y < 50:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

def findRow2(tableArea):
    #for cells
    horizontalLinesArray = []
    verticalLinesArray = []

    table = CropImage(img, tableArea.x, tableArea.y - 5, tableArea.w, tableArea.h + 5)
    table = GetGrayImage(table)
    #show_pic(table)
    #table = tableArea.img
    #result = tableArea.img.copy()
    # Detect horizontal lines
    ret, thresh_value = cv.threshold(table, 240, 255, cv.THRESH_BINARY_INV)
    horizontal_kernel = cv.getStructuringElement(cv.MORPH_RECT, (120, 1))
    detect_horizontal = cv.morphologyEx(thresh_value, cv.MORPH_OPEN, horizontal_kernel, iterations=1)
    cntsH = cv.findContours(detect_horizontal, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #show_pic(thresh_value)
    # Detect vertical lines
    ret, thresh_value = cv.threshold(table, 250, 255, cv.THRESH_BINARY_INV)
    vertical_kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 100))
    detect_vertical = cv.morphologyEx(thresh_value, cv.MORPH_OPEN, vertical_kernel, iterations=1)
    cntsV = cv.findContours(detect_vertical, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #horizontal lines
    for i in range(len(cntsH[0])):
        position = len(cntsH[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
        x, y , w, h = cv.boundingRect(cntsH[0][position])
        x = x + tableArea.x
        y = y + tableArea.y
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        horizontalLinesArray.append(HorizontalLines(x, y, w, h))

    cv.imshow("", img)
    cv.waitKey(0)

    #vertical lines
    for i in range(len(cntsV[0])):
        position = len(cntsV[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
        #print(position)
        x, y, w, h = cv.boundingRect(cntsV[0][position])
        x = x + tableArea.x
        y = y + tableArea.y
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        verticalLinesArray.append(VerticalLines(x, y, w, h))

    #show_pic(img)
    return table, horizontalLinesArray, verticalLinesArray

def unterractWithTable(raw_rows, horizontalLinesArray, verticalLinesArray, x_cell, y_cell):
    #calculate coordinates for cells
    #cell[2,4]
    x = verticalLinesArray[x_cell - 1].x
    w = verticalLinesArray[x_cell].x - x
    y = horizontalLinesArray[y_cell - 1].y
    h = horizontalLinesArray[y_cell].y - y
    print(x, w, y, h)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 10)
    return x, y, w, h

def getTextFromImage(cropImg):
    textFromImage = pytesseract.image_to_string(cropImg)
    return textFromImage

def TakeCentrOfElement(x, y, w, h):
    x_centr = (w / 2) + x
    y_centr = (w / 2) + y
    return x_centr, y_centr

#find table
#table area
table_img, x, y, w, h = findTableArea(img_gray)
tableArea = GuiObject(table_img, x, y, w, h)

#area with rows
raw_rows, horizontalLinesArray, verticalLinesArray = findRow2(tableArea)
tableObject = TableObject(raw_rows, tableArea.x, tableArea.y, tableArea.w, tableArea.h, verticalLinesArray, horizontalLinesArray)
#show_pic(raw_rows)
#cell 4x4
x, y, w, h = unterractWithTable(tableObject.img, tableObject.horizontalLines, tableObject.verticalLines, 2, 2)

x, y = TakeCentrOfElement(x, y, w, h)
#moveMouseToCentreOfElementAndClick(x, y)

#cv.imshow('Binary Threshold', thresh1)
#if cv.waitKey(0) & 0xff == 27:
#    cv.destroyAllWindows()

#cv.imshow("", img)
#cv.waitKey(0)