import pytesseract
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.CommonMethods import CommonMethods
import cv2
from pytesseract import Output

class TesseractOCR():

    def GetTextFromImage(image):
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        #pytesseract.pytesseract.tesseract_cmd = r'c:\Temp\tesseract\tesseract.exe'
        #pytesseract.pytesseract.tesseract_cmd = r'c:\Temp2\Tesseract-OCR\tesseract.exe'

        #convert to negative
        #image = ImageConverters.ConvertImageToNegative(image)

        resize = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
        sharp = ImageFilters.Sharp(image)
        #blur = ImageFilters.Blur(resize)
        #blur = ImageFilters.Blur(blur)
        #blur = ImageFilters.Blur(blur)
        negative = ImageConverters.ConvertImageToNegative(sharp)
        pytesseract.pytesseract.tesseract_cmd = r'c:\Temp2\Tesseract-OCR\tesseract.exe'
        #text = pytesseract.image_to_string(image, lang='eng', config="--psm 10 --oem 3")
        text = pytesseract.image_to_string(image, lang='eng', config="--psm 3 --oem 3")
        #CommonMethods.ShowImageWithOriginalSize(blur)
        #print(pytesseract.get_languages())
        print(text[0])

        #text = pytesseract.image_to_string(image)
        #print(text)
        #return text
