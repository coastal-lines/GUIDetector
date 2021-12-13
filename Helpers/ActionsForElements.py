import pyautogui

class ActionsForElements():

    def GetCentreOfElement(p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        return x, y

    def ClickOnTheCentreOfTheElement(p1, p2):
        x = p2[0] - ((p2[0] - p1[0]) / 2)
        y = p2[1] - ((p2[1] - p1[1]) / 2)
        pyautogui.click(x, y)