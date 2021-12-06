import cv2
import numpy as np

#Image derivatives
##http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

#One Important Matter!
#In our last example, output datatype is cv.CV_8U or np.uint8. But there is a slight problem with that. Black-to-White transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken as a Negative slope (It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. In simple words, you miss that edge.
#If you want to detect both edges, better option is to keep the output datatype to some higher forms, like cv.CV_16S, cv.CV_64F etc, take its absolute value and then convert back to cv.CV_8U. Below code demonstrates this procedure for a horizontal Sobel filter and difference in results.

def SobelByScratch(img):
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])

    # ddepth	desired depth of the destination image, see combinations
    # when ddepth=-1, the output image will have the same depth as the source
    filtered_image_x = cv2.filter2D(img, -1, sobel_x)
    filtered_image_y = cv2.filter2D(img, -1, sobel_y)

    # 0.0 is gamma
    # gamma - scalar added to each sum
    # 0.5 - 	weight of the array elements
    gradient = cv2.addWeighted(filtered_image_x, 0.5, filtered_image_y, 0.5, 0.0)
    return gradient

def Sobel(img):
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S;

    grad_x = cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(img, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

    #Convert output to a CV_8U image
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    gradient = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return gradient

def Scharr(img):
    img_scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    img_scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    img_scharr_x = cv2.convertScaleAbs(img_scharr_x)
    img_scharr_y = cv2.convertScaleAbs(img_scharr_y)
    gradient = cv2.addWeighted(img_scharr_x, 0.5, img_scharr_y, 0.5, 0)
    return gradient

def Laplasian(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    #Convert output to a CV_8U image
    laplacian8bit = cv2.convertScaleAbs(laplacian)
    return laplacian8bit


