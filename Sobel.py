#http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

import cv2
import numpy as np
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods

element = ImageLoaders.LoadImage(r'C:\Temp\!my\TestsTab\Tests.bmp')
element_bw = ImageConverters.ConvertToBW(element)

# Create a custom kernel

sobel_x = np.array([[ -1, 0, 1],
                   [ -2, 0, 2],
                   [ -1, 0, 1]])

sobel_y = np.array([[ -1, -2, -1],
                   [ 0, 0, 0],
                   [ 1, 2, 1]])

#ddepth	desired depth of the destination image, see combinations
#when ddepth=-1, the output image will have the same depth as the source
filtered_image_x = cv2.filter2D(element_bw, -1, sobel_x)
filtered_image_y = cv2.filter2D(element_bw, -1, sobel_y)

#0.0 is gamma
#gamma - scalar added to each sum
#0.5 - 	weight of the array elements
result = cv2.addWeighted(filtered_image_x, 0.5, filtered_image_y, 0.5, 0.0)
CommonMethods.ShowImage(result)



