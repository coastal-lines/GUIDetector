import cv2

class ImageFilters():

    def Blur(img):
        img = cv2.GaussianBlur(img, (3, 3), 0)
        return img

    def AdaptiveThresholding(img, max_value, block_size, constant):
        th = cv2.adaptiveThreshold(img,max_value,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,block_size,constant)
        return th