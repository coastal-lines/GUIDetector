from Helpers.ImageConverters import ImageConverters
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.Threshold import Threshold
import cv2

class Tasks():

    def FindFilterTests(img):
        bw = ImageConverters.ConvertToBW(img)
        blur = ImageFilters.Blur(bw)
        th = Threshold.InRangeThreshold(blur,245,255)
        contours, hierarchy = Countours.GetContours(th)

        cnt = Countours.DrawRectangle2(contours, img)
        #CommonMethods.ShowImage(img)
        return cnt


        #check keywords
        #save in memory as object

        #regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(bw)
        #find text in rectangle
        #for box in boundingBoxes:
        #    x, y, w, h = box;
        #    img_temp = CommonMethods.CropImage(bw, x, y, w, h)
        #    text = TesseractOCR.GetTextFromImage(img_temp)
        #    print(text)