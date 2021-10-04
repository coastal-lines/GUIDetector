import cv2
import numpy as np

class Countours():

    def GetContoursByCanny(image_bw):
        median_intensity = np.median(image_bw)
        lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
        upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
        img_canny = cv2.Canny(image_bw, lower_threshold, upper_threshold)