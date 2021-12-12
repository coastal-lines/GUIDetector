from typing import List

class TestData:
    p1: tuple
    p2: tuple

    def __init__(self, p1: tuple, p2: tuple):
        self.p1 = p1
        self.p2 = p2

class Color:
    active: str
    nonactive: str

    def __init__(self, active: str, nonactive: str):
        self.active = active
        self.nonactive = nonactive

class Scroll:
    horizontal: str
    vertical: str

    def __init__(self, horizontal: str, vertical: str):
        self.horizontal = horizontal
        self.vertical = vertical

class Element:
    name: str
    type: str
    width: int
    heigth: int
    parent: str
    color: Color
    text: str
    columns: List[str]
    scroll: Scroll
    ImagePath: str
    ScreenResolution: List[int]
    findBy: str
    TestData: TestData

    def __init__(self, name: str, type: str, width: int, heigth: int, parent: str, color: Color, text: str, columns: List[str], scroll: Scroll, ImagePath: str, ScreenResolution: List[int], findBy: str, TestData: TestData):
        self.name = name
        self.type = type
        self.width = width
        self.heigth = heigth
        self.parent = parent
        self.color = color
        self.text = text
        self.columns = columns
        self.scroll = scroll
        self.ImagePath = ImagePath
        self.ScreenResolution = ScreenResolution
        self.findBy = findBy
        self.TestData = None

class LabeledData:
    elements: List[Element]

    def __init__(self, elements: List[Element]):
        self.elements = elements