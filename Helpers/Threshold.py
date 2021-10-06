import cv2

class Threshold():

    def BinaryThreshold(img):
        ret, th = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        return th

    def AdaptiveThreshold(img, max_value, block_size, constant):
        th = cv2.adaptiveThreshold(img ,max_value ,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY ,block_size ,constant)
        return th

    def BlendedThreshold(img):
        ret, th1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
        blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=0)
        return blended