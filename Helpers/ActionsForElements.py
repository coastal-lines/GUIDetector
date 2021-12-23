import cv2
import pyautogui
from Helpers.CommonMethods import CommonMethods
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.OCR.TesseractClass import TesseractOCR


class ActionsForElements():
    def GetCentreOfElement(p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        return x, y

    def ClickOnTheCentreOfTheElement(self, p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        pyautogui.click(x, y)

    # region for scrolling
    def FindScrollArea(self, roi_bw, up_button, down_button):
        up_button_p1, up_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(roi_bw, up_button)
        down_button_p1, down_button_p2 = PatternMatching.DetectByPatternMatchingTM_CCOEFF_NORMED(roi_bw, down_button)

        # check that buttons are on the same line
        if (up_button_p1[0] >= (down_button_p1[0] - 2) and up_button_p1[0] <= (down_button_p1[0] + 2)):
            w, h = CommonMethods.GetImageWidthAndHeigth(up_button)
            scroll_w = w
            scroll_h = down_button_p2[1] - up_button_p1[1]
            scroll_p1 = (up_button_p1[0], up_button_p1[1])
            scroll_p2 = (down_button_p2[0], down_button_p2[1])

            return scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2

    def ScrollDown(self, roi_bw, up_button, down_button):
        scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2 = self.FindScrollArea(self, roi_bw, up_button, down_button)
        if(scroll_p1 != None and scroll_p2 != None):
            self.ClickOnTheCentreOfTheElement(self, down_button_p1, down_button_p2)

    def ScrollUp(self, roi_bw, up_button, down_button):
        scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2 = self.FindScrollArea(self, roi_bw, up_button, down_button)
        if(scroll_p1 != None and scroll_p2 != None):
            self.ClickOnTheCentreOfTheElement(self, up_button_p1, up_button_p2)

    def ScrollDownWhilePossibleAndReadText(self, main_screen_bw, p1, p2, up_button, down_button):
        roi_bw = CommonMethods.MaskForRoiFromPoints(main_screen_bw, p1, p2)
        scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2 = self.FindScrollArea(self, roi_bw, up_button, down_button)

        # click down until it is possible
        condition = False
        warning_count = 0
        while(condition == False):
            # save start view of element
            roi_before_click = CommonMethods.MaskForRoiFromPoints(CommonMethods.GetScreenshotBW(), p1, p2)

            # click down
            self.ClickOnTheCentreOfTheElement(self, down_button_p1, down_button_p2)

            # make new roi
            temp_roi_bw = CommonMethods.MaskForRoiFromPoints(CommonMethods.GetScreenshotBW(), p1, p2)

            # check bottom condition
            score_before = PatternMatching.ComparePixelByPixel(roi_before_click, roi_before_click)
            score_after = PatternMatching.ComparePixelByPixel(roi_before_click, temp_roi_bw)

            # read text
            TesseractOCR.GetTextFromImage()

            if(score_before == score_after):
                condition = True

            warning_count += 1
            if(warning_count > 100):
                condition = True


