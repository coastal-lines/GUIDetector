import cv2 as cv
import numpy as np
from Helpers.CommonMethods import CommonMethods
from Helpers.FeatureExtractors.Contours import Contours

class PatternMatching():

    def DetectByPatternMatching(img_gray, template):
        # - сохраняем ширину и высоту паттерна
        h, w = template.shape

        # - TM_SQDIFF метод квадратов разностей. Идеальное совпадение, если сумма квадратов разностей равна 0
        res = cv.matchTemplate(img_gray, template, cv.TM_SQDIFF)

        # min_val - минимум
        # max_val - максимум
        # min_loc - позиция (x,y) минимума
        # max_loc - позиция (x, y) максимума
        # нам нужен минимум - т.е. берем точку, в которой был найден минимум
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # - получаем координаты и рисуем прямоугольник
        x = min_loc[0]
        y = min_loc[1]
        point1 = (x, y)
        point2 = (x + w, y + h)

        return point1, point2

    def DetectByPatternMatchingTM_CCOEFF_NORMED(img_gray, template):
        # - сохраняем ширину и высоту паттерна
        h, w = template.shape

        # - TM_SQDIFF метод квадратов разностей. Идеальное совпадение, если сумма квадратов разностей равна 0
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

        return res

    def ComparePixelByPixel(pattern, roi):
        range_value = 512

        pattern_resized = CommonMethods.Resize(pattern, range_value, range_value)
        roi_resized = CommonMethods.Resize(roi, range_value, range_value)

        match_count = 0
        for i in range(range_value):
            for j in range(range_value):
                if (pattern_resized[i][j] == roi_resized[i][j]):
                    match_count += 1

        return match_count

    def ComparePixelByPixelWithoutResizing(pattern, roi):
        h,w = roi.shape[:2]
        match_count = 0

        for i in range(h):
            for j in range(w):
                if (pattern[i][j] == roi[i][j]):
                    match_count += 1

        return match_count

    def FindPatternAndDrawRectange(img, pattern):
        p1, p2 = PatternMatching.DetectByPatternMatching(img, pattern)
        Contours.DrawRectangleByPoints(p1, p2, img, [0, 0, 0], 4)
