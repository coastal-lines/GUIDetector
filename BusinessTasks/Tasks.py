from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.ImageConverters import ImageConverters
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.CommonMethods import CommonMethods
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.Threshold import Threshold

class Tasks():

    def FindFilterTests(self):
        #find rectangles
        img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\FullTests.png')
        bw = ImageConverters.ConvertToBW(img)
        #th = ImageFilters.AdaptiveThresholding(bw,255,11,8)
        th = Threshold.BinaryThreshold(bw)
        CommonMethods.ShowImage(th)
        contours, hierarchy = Countours.GetContoursByCanny(th, 0, 255)
        Countours.DrawRectangle(contours, img)
        #CommonMethods.ShowImage(img)

        #check keywords
        #save in memory as object

        #regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(bw)
        #find text in rectangle
        #for box in boundingBoxes:
        #    x, y, w, h = box;
        #    img_temp = CommonMethods.CropImage(bw, x, y, w, h)
        #    text = TesseractOCR.GetTextFromImage(img_temp)
        #    print(text)