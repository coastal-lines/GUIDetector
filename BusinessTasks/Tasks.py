from Helpers.ImageConverters import ImageConverters
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.Threshold import Threshold
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from Helpers.MorphologicalOperations import MorphologicalOperations
import cv2

class Tasks():

    def FindMainWindow(img):
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.AdaptiveThreshold(blur,255,11,8)
        dilate = MorphologicalOperations.Erosion(th)
        #CommonMethods.ShowImage(dilate)
        contours, hierarchy = Countours.GetContours(th)
        Countours.DrawRectangle(contours, img)
        CommonMethods.ShowImage(img)

    def FindFilterTests(img):
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.InRangeThreshold(blur,245,255)
        contours, hierarchy = Countours.GetContours(th)

        orig_contour = ImageLoaders.Deserialize("filtertests")
        orig_contour_length = Countours.GetContourLength(orig_contour)
        for contour in contours:
            temp_contour_length = Countours.GetContourLength(contour)
            if temp_contour_length > orig_contour_length / 2:
                match = Countours.GetMatchShapes(orig_contour, contour)
                if match < 0.07:
                    Countours.DrawRectangle(contour, img)

        #CommonMethods.ShowImage(img)
        return contour