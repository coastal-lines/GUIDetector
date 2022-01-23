from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en', type='title') # need to run only once to download and load model into memory
img_path = r"C:\Temp\Photos\data\list_subjects3.bmp"
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)