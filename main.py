from Helpers.ImageLoaders import ImageLoaders
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.FeatureExtractors.Contours import Countours
from Helpers.CommonMethods import CommonMethods
from Helpers.ImageConverters import ImageConverters
from BusinessTasks.Tasks import Tasks

#Tasks.FindFilterTests(Tasks)

img = ImageLoaders.LoadImage(r'C:\Temp2\Flash\MyLabeling\FullTests.png')
bw = ImageConverters.ConvertToBW(img)
contours, hierarchy = Countours.GetContoursByCanny(bw, 0, 255)
Countours.DrawContours(contours, img)
CommonMethods.ShowImage(img)