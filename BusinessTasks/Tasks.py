from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.CommonMethods import CommonMethods
from Helpers.ImageConverters import ImageConverters

class Tasks():

    def FindFilterTests(self):
        #find rectangles
        img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\FullTests.png')
        bw = ImageConverters.ConvertToBW(img)
        regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(bw)
        #find text in rectangle
        for bound in boundingBoxes:


        #check keywords
        #save in memory as object