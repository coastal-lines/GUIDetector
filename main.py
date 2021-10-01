from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.CommonMethods import CommonMethods

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\FullTests.png')
regions, boundingBoxes = MSER.GetRegionsAndBoundingBoxesByMSER(img)
img_for_draw = MSER.DrawRectanglesForMSER(boundingBoxes, img)
CommonMethods.ShowImage(img_for_draw)
