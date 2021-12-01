from typing import List


class Color:
    active: str
    nonactive: str

    def __init__(self, active: str, nonactive: str) -> None:
        self.active = active
        self.nonactive = nonactive


class Scroll:
    horizontal: str
    vertical: str

    def __init__(self, horizontal: str, vertical: str) -> None:
        self.horizontal = horizontal
        self.vertical = vertical


class ElementElement:
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

    def __init__(self, name: str, type: str, width: int, heigth: int, parent: str, color: Color, text: str, columns: List[str], scroll: Scroll, ImagePath: str, ScreenResolution: List[int], findBy: str) -> None:
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


class Element:
    elements: List[ElementElement]

    def __init__(self, elements: List[ElementElement]):
        self.elements = elements