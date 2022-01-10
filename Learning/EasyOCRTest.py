import easyocr
from Helpers.ImageLoaders import ImageLoaders
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.CommonMethods import CommonMethods
import cv2

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

img = ImageLoaders.LoadBWImage(r"C:\Temp\Photos\data\c5.bmp")
blur = ImageFilters.Blur(img)

result = reader.readtext(blur)
print(result)