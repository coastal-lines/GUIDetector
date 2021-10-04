import cv2
import numpy as np

class Countours():

    def GetContoursByCanny():
        # open image, conver into RGB, convert into BW
        image_original = cv2.imread(r'C:\Temp2\ForTesseract\labeled\1.png')
        img_bw_rgb = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)

        median_intensity = np.median(img_bw_rgb)
        lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
        upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
        img_canny = cv2.Canny(img_bw_rgb, lower_threshold, upper_threshold)

        # open image in popup
        imgplot = plt.imshow(img_canny[0:100])
        plt.show()