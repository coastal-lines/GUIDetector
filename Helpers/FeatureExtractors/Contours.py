import cv2
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.CommonMethods import CommonMethods
import random as rng
import numpy as np

class Countours():

    def GetContours(image_bw):
        contours, hierarchy = cv2.findContours(image_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return contours, hierarchy

    def GetContoursByCanny(image_bw, lower_threshold, upper_threshold):
        detected_edges = cv2.Canny(image_bw, lower_threshold, upper_threshold)
        #CV_RETR_LIST - режим группировки - без группировки контуров
        #CV_CHAIN_APPROX_SIMPLE — склеивает все горизонтальные, вертикальные и диагональные контуры
        contours, hierarchy = cv2.findContours(detected_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours, hierarchy

    def DrawRectangle(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            point1 = (x, y)
            point2 = (x + w, y + h)
            cv2.rectangle(image, point1, point2, (0, 255, 0), 1)

    def DrawRectangle2(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if (w > 209 and h > 550) and (w < 270 and h < 590):
                point1 = (x, y)
                point2 = (x + w, y + h)
                cv2.rectangle(image, point1, point2, (0, 255, 0), 1)
                #print(w)
                return cnt

    def DrawRectangle3(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if (w > 209 and h > 550) and (w < 330 and h < 700):
                point1 = (x, y)
                point2 = (x + w, y + h)
                cv2.rectangle(image, point1, point2, (0, 255, 0), 1)
                #print(w)
                return cnt