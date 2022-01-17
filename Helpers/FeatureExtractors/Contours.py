import cv2
from decimal import Decimal
from Helpers.ImageLoaders import ImageLoaders
import numpy as np

class Contours():

    def GetContours(image_bw):
        contours, hierarchy = cv2.findContours(image_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        return contours, hierarchy

    def GetContoursByCanny(image_bw, lower_threshold, upper_threshold):
        detected_edges = cv2.Canny(image_bw, lower_threshold, upper_threshold)
        #CV_RETR_LIST - режим группировки - без группировки контуров
        #CV_CHAIN_APPROX_SIMPLE — склеивает все горизонтальные, вертикальные и диагональные контуры
        contours, hierarchy = cv2.findContours(detected_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours, hierarchy

    def GetContourLength(contour):
        return cv2.arcLength(contour, True)

    def GetMatchShapes(contour1, contour2):
        value = cv2.matchShapes(contour1, contour2, 1, 0.0)
        return Decimal(value)

    def FindCustomContour(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if (w > 209 and h > 550) and (w < 270 and h < 590):
                point1 = (x, y)
                point2 = (x + w, y + h)
                cv2.rectangle(image, point1, point2, (0, 255, 0), 2)
                ImageLoaders.Serialize(cnt)
                #print(w)
                return cnt

    def GetBoxFromContour(contour):
        rect = cv2.minAreaRect(contour) # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        return box