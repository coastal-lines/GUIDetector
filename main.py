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


# работать нужно не с кропнутым изображением, а с регионом!

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


def CalculateRectangle(x, y, width, heigth):
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

    return x, y, width, heigth


def Filter():
    x = 70
    y = 245
    width = 257
    heigth = 580

    x, y, width, heigth = CalculateRectangle(x, y, width, heigth)

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
    return x, y, width, heigth


def DetectCells(img, x, y, width, heigth):
    cells = []

    img_table = CommonMethods.MaskForRoi(img, x, y, width, heigth)
    #img_table = cv2.imread(r"C:\Temp2\Flash\MyLabeling\ORB\FullTests2table.png")
    img_bw = ImageConverters.ConvertToBW(img_table)
    th = Threshold.AdaptiveThreshold(img_bw, 255, 11, 8)
    erosion = MorphologicalOperations.Erosion(th)
    CommonMethods.ShowImage(erosion)
    cntsH = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # seaching cells
    for i in range(len(cntsH[0])):
        position = len(cntsH[0]) - (i + 1)  # нужен реверс т.к. отсчет идет с правой стороны
        x, y, w, h = cv2.boundingRect(cntsH[0][position])
        if (w > h and w > 10 and h > 10 and h < 40):  # нужно доработать алгоритм исключения выбросов
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cells.append(Cell(x, y, w, h))

    return img, cells


def ConvertCellsToTable(cells):
    # calculate columns
    columns = 0
    for c in cells:
        if (c.y == 0):
            columns = columns + 1

    # calculate rows
    rows = 0
    for c in cells:
        if (c.x == 0):
            rows = rows + 1

    array = np.array(cells)
    table = array.reshape(rows, columns)

    return table


def SelectCell(img, table, column, row):
    column = column - 1
    row = row - 1
    cv2.rectangle(img, (table[column, row].x, table[column, row].y),
                  (table[column, row].x + table[column, row].w, table[column, row].y + table[column, row].h),
                  (0, 0, 0), 2)
    CommonMethods.ShowImage(img)


Filter()
TestN()
TestS()
ApplyB()
x, y, width, heigth = Table()
img, cells = DetectCells(img, x, y, width, heigth)
#table = ConvertCellsToTable(cells)
#SelectCell(img, table, 2, 2)
CommonMethods.ShowImage(img)
