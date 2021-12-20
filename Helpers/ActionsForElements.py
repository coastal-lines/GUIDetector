import pyautogui
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.FeatureExtractors.Contours import Contours
from Helpers.CommonMethods import CommonMethods

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

    def IsTheBottomOfScroll(self, roi_bw, up_button, down_button):
        scroll_p1, scroll_p2, up_button_p1, up_button_p2, down_button_p1, down_button_p2 = self.FindScrollArea(self, roi_bw, up_button, down_button)

        # save start view of scrollbar
        scroll_before_click = CommonMethods.CropImageByPoints(roi_bw, scroll_p1, scroll_p2)

        # click down
        self.ClickOnTheCentreOfTheElement(self, down_button_p1, down_button_p2)

        # check bottom condition
        scroll_after_click = CommonMethods.CropImageByPoints(roi_bw, scroll_p1, scroll_p2)

        # 
        score = PatternMatching.ComparePixelByPixel(scroll_before_click, scroll_after_click)
        #if(score_after_click != score_before_click):
        #    return True

        #return False


