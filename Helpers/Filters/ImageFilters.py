import cv2

class ImageFilters():

    def Blur(img):
        img = cv2.GaussianBlur(img, (3, 3), 0)
        return img