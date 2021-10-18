import pytesseract
from Helpers.ImageConverters import ImageConverters
from Helpers.CommonMethods import CommonMethods

class TesseractOCR():

    def GetTextFromImage(image):
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = r'c:\Temp\tesseract\tesseract.exe'

        #convert to negative
        image = ImageConverters.ConvertImageToNegative(image)

        text = pytesseract.image_to_string(image)
        print(text)
        return text