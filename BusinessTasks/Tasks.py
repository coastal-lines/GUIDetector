from Helpers.ImageConverters import ImageConverters
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.Threshold import Threshold
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from Helpers.MorphologicalOperations import MorphologicalOperations
import cv2

class Tasks():

    #если не на полный экран открыто
    def FindMainWindow(img):
        img = img.copy()
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.AdaptiveThreshold(blur,255,11,8)
        dilate = MorphologicalOperations.Erosion(th)
        contours, hierarchy = Countours.GetContours(dilate)
        orig_contour = ImageLoaders.Deserialize("maintests")
        orig_contour_length = Countours.GetContourLength(orig_contour)

        for contour in contours:
            temp_contour_length = Countours.GetContourLength(contour)
            #проверяем что исследуемый контур помещается в нужный диапазон длинн
            if (orig_contour_length > temp_contour_length - CommonMethods.GetPercent(temp_contour_length, 30)
            and orig_contour_length < temp_contour_length + CommonMethods.GetPercent(temp_contour_length, 30)):
                match = Countours.GetMatchShapes(orig_contour, contour)
                if match < 0.07:
                    Countours.DrawRectangle(contour, img)
                    print("main was found")
                    print(match)
                    #return contour
        #CommonMethods.ShowImage(img)

    def FindFilter(img):
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.InRangeThreshold(blur,245,255)
        contours, hierarchy = Countours.GetContours(th)
        orig_contour = ImageLoaders.Deserialize("filtertests")
        orig_contour_length = Countours.GetContourLength(orig_contour)
        for contour in contours:
            temp_contour_length = Countours.GetContourLength(contour)
            if (orig_contour_length > temp_contour_length - CommonMethods.GetPercent(temp_contour_length, 30)
            and orig_contour_length < temp_contour_length + CommonMethods.GetPercent(temp_contour_length, 30)):
                match = Countours.GetMatchShapes(orig_contour, contour)
                if match < 0.7:
                    print("filter was found")
                    Countours.DrawRectangle(contour, img)
                    return contour

    def NameInput(img, contour):
        #ищем внутри определённого контура
        x, y, w, h = cv2.boundingRect(contour)
        roi = CommonMethods.CropImage(img, x, y, w, h)
        CommonMethods.ShowImage(roi)

