import cv2

class CommonMethods():

    def CropImage(image, x, y, w, h):
        img = image[y:y + h, x:x + w]
        return img

    def ShowImage(image):
        cv2.imshow("", image)
        cv2.waitKey(0)