import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
from Helpers.FeatureExtractors.Contours import Countours
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations

#работать нужно не с кропнутым изображением, а с регионом!

class GuiObject():
    def __init__(self, img, x, y, w, h):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class VerticalLines():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Cell():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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

def Table():
    x = 330
    y = 223
    width = 1583
    heigth = 785

    x, y, width, heigth = CalculateRectangle(x, y, width, heigth)

    point1 = (x, y)
    point2 = (x + width, y + heigth)
    Countours.DrawRectangleByPoints(point1, point2, img)

def DetectCells():
    #for cells
    horizontalLinesArray = []
    verticalLinesArray = []

    table = cv2.imread(r"C:\Temp2\Flash\MyLabeling\ORB\FullTests2table.png", 0)
    img = table
    #tableArea = GuiObject(table, 330, 223, 1583, 785)

    #show_pic(table)
    #table = tableArea.img
    #result = tableArea.img.copy()
    # Detect horizontal lines
    ret, thresh_value = cv2.threshold(table, 235, 250, cv2.THRESH_BINARY_INV)

    #CommonMethods.ShowImage(thresh_value)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (120, 1))
    detect_horizontal = cv2.morphologyEx(thresh_value, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
    cntsH = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #show_pic(thresh_value)
    # Detect vertical lines
    ret, thresh_value = cv2.threshold(table, 245, 250, cv2.THRESH_BINARY_INV)
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 100))
    detect_vertical = cv2.morphologyEx(thresh_value, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
    cntsV = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #horizontal lines
    for i in range(len(cntsH[0])):
        position = len(cntsH[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
        x, y , w, h = cv2.boundingRect(cntsH[0][position])
        #x = x + tableArea.x
        #y = y + tableArea.y
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        horizontalLinesArray.append(Cell(x, y, w, h))

    #vertical lines
    for i in range(len(cntsV[0])):
        position = len(cntsV[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
        #print(position)
        x, y, w, h = cv2.boundingRect(cntsV[0][position])
        #x = x + tableArea.x
        #y = y + tableArea.y
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        verticalLinesArray.append(VerticalLines(x, y, w, h))

    #CommonMethods.ShowImage(table)

def DetectCells2():
    cells = []

    im = cv2.imread(r"C:\Temp2\Flash\MyLabeling\ORB\FullTests2table.png")
    table = cv2.imread(r"C:\Temp2\Flash\MyLabeling\ORB\FullTests2table.png", 0)
    img = table

    blur = ImageFilters.Blur(img)
    th = Threshold.AdaptiveThreshold(img, 255, 11, 8)
    erosion = MorphologicalOperations.Erosion(th)

    cntsH = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #horizontal lines
    for i in range(len(cntsH[0])):
        position = len(cntsH[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
        x, y, w, h = cv2.boundingRect(cntsH[0][position])
        if(w > h and w > 10 and h > 10 and h<40):
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)
                cells.append(Cell(x, y, w, h))
                #cv2.putText(im, str(i), (x+5, y+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 12), 2)
    #CommonMethods.ShowImage(im)

    #cntsV = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #vertical lines
    #for i in range(len(cntsV[0])):
    #    position = len(cntsV[0]) - (i + 1) #нужен реверс т.к. отсчет идет с правой стороны
    #    x, y, w, h = cv2.boundingRect(cntsV[0][position])
    #    if (w > h and w > 10 and h > 10):
    #        #cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)
    #        verticalLinesArray.append(VerticalLines(x, y, w, h))
    #        cv2.putText(im, str(i), (x+20, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 120), 2)

    x_cell = 1 + 1
    y_cell = 1 + 1
    #x = verticalLinesArray[x_cell - 1].x
    #w = verticalLinesArray[x_cell].x - x
    y = cells[y_cell - 1].y
    h = cells[y_cell].y - y

    #print(x, w, y, h)

    #print(str(verticalLinesArray[1].x) + " " + str(verticalLinesArray[1].y) + " " + str(verticalLinesArray[1].w) + " " + str(verticalLinesArray[1].h))
    print(str(cells[1].x) + " " + str(cells[1].y) + " " + str(cells[1].w) + " " + str(cells[1].h))

    #cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #CommonMethods.ShowImage(im)
    return im,cells

def ConvertCellsToTable(img, cells):
    #calculate columns
    columns = 0
    for c in cells:
        if(c.y == 0):
            columns = columns + 1

    #calculate rows
    rows = 0
    for c in cells:
        if(c.x == 0):
            rows = rows + 1

    array = np.array(cells)
    table = array.reshape(rows, columns)

    return img, table

def SelectCell(img, table, column, row):
    column = column - 1
    row = row - 1
    cv2.rectangle(img, (table[column, row].x, table[column, row].y), (table[column, row].x + table[column, row].w, table[column, row].y + table[column, row].h),
                  (0, 0, 0), 2)
    CommonMethods.ShowImage(img)

#Filter()
#TestN()
#TestS()
#ApplyB()
#Table()
img,cells = DetectCells2()
img, table = ConvertCellsToTable(img,cells)
SelectCell(img, table, 2, 2)
#CommonMethods.ShowImage(img)