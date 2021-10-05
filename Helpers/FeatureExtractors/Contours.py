import cv2
import math
import numpy as np

class Countours():

    def GetContoursByCanny(image_bw, lower_threshold, upper_threshold):
        detected_edges = cv2.Canny(image_bw, lower_threshold, upper_threshold)
        #CV_RETR_LIST - режим группировки - без группировки контуров
        #CV_CHAIN_APPROX_SIMPLE — склеивает все горизонтальные, вертикальные и диагональные контуры
        contours, hierarchy = cv2.findContours(detected_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return contours, hierarchy

    def DrawContours(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            point1 = (x, y)
            point2 = (x + w, y + h)
            cv2.rectangle(image, point1, point2, (0, 255, 0), 1)