import pyautogui
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.FeatureExtractors.Contours import Contours
from Helpers.CommonMethods import CommonMethods

class ActionsForElements():
    def GetCentreOfElement(p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        return x, y

    def ClickOnTheCentreOfTheElement(p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        pyautogui.click(x, y)

    def ScrollDownToBottom(roi_bw, up_button, down_button):
        up_button_p1, up_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(roi_bw, up_button)
        down_button_p1, down_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(roi_bw, down_button)

        # check that buttons are on the same line
        if (up_button_p1[0] >= (down_button_p1[0] - 2) and up_button_p1[0] <= (down_button_p1[0] + 2)):
            w, h = CommonMethods.GetImageWidthAndHeigth(up_button)
            scroll_w = w
            scroll_h = down_button_p2[1] - up_button_p1[1]
            scroll_p1 = (up_button_p1[0], up_button_p1[1])
            scroll_p2 = (down_button_p2[0], down_button_p2[1])

            # save start view of scrollbar
            scroll_before_click = CommonMethods.CropImageByPoints(scroll_p1, scroll_p2)

            # click down
            roi_bw.ClickOnTheCentreOfTheElement(down_button_p1, down_button_p2)

            scroll_after_click = 0
            # create roi again and compare with start scrollbar's roi
            while (scroll_after_click != scroll_before_click):
                scroll_before_click = CommonMethods.CropImageByPoints(scroll_p1, scroll_p2)
                roi_bw.ClickOnTheCentreOfTheElement(down_button_p1, down_button_p2)
                scroll_after_click = CommonMethods.CropImageByPoints(scroll_p1, scroll_p2)
                score = PatternMatching.ComparePixelByPixel(scroll_before_click, scroll_after_click)



