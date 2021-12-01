import cv2
import numpy as np
import pyautogui

class CommonMethods():

    def CropImage(image, x, y, w, h):
        img = image[y:y + h, x:x + w]
        return img

    def CropImageFromContour(image, contour):
        x, y, w, h = cv2.boundingRect(contour)
        img = image[y:y + h, x:x + w]
        return img

    def CropImageByPoints(image, point1, point2):
        x = point1[0]
        y = point1[1]
        w = point2[0] - point1[0]
        h = point2[1] - point1[1]
        img = image[y:y + h, x:x + w]
        return img

    def MaskForRoi(img, x, y, w, h):
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[y:y + h, x:x + w] = 255
        masked_img = cv2.bitwise_and(img, img, mask=mask)
        return masked_img

    def MaskForRoiFromContour(img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[y:y + h, x:x + w] = 255
        masked_img = cv2.bitwise_and(img, img, mask=mask)
        return masked_img

    def ExtendedMaskForRoiFromContour(img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        x = x - 5
        y = y - 5
        w = w + 10
        h = h + 10
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[y:y + h, x:x + w] = 255
        masked_img = cv2.bitwise_and(img, img, mask=mask)
        return masked_img

    def MaskForRoiFromPoints(img, point1, point2):
        x = point1[0]
        y = point1[1]
        w = point2[0] - point1[0]
        h = point2[1] - point1[1]
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[y:y + h, x:x + w] = 255
        masked_img = cv2.bitwise_and(img, img, mask=mask)
        return masked_img

    def ShowImage(image):
        image = cv2.resize(image, (1200, 800))
        cv2.imshow("", image)
        cv2.waitKey(0)

    def ShowImageWithOriginalSize(image):
        image = cv2.resize(image, (image.shape[:2][1], image.shape[:2][0]))
        cv2.imshow("", image)
        cv2.waitKey(0)

    def ShowTwoImages(image1, image2):
        cv2.imshow("1", image1)
        cv2.imshow("2", image2)
        cv2.waitKey(0)

    def GetMedian(image):
        #медиана - половина массива меньше этого значения, а половина больше
        median_intensity = np.median(image)
        return median_intensity

    def Resize(image, w, h):
        resized_image = cv2.resize(image, (w, h))
        return resized_image

    def GetPercent(number, percent):
        return round((number / 100) * percent)

    def GetImageWidthAndHeigth(image):
        w = image.shape[:2][1]
        h = image.shape[:2][0]
        return w, h

    def GetScreenshot():
        screenshot = pyautogui.screenshot()
        open_cv_image = np.array(screenshot)
        return open_cv_image

    def DoesGrayscaleRegionHaveAColor(image, color):
        w = image.shape[:2][1]
        h = image.shape[:2][0]

        for y in range(h):
            for x in range(w):
                if image[x, y] == color:
                    return True

        return False