from Helpers.Json import JsonHelper
import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.FeatureExtractors.Contours import Contours
from Helpers.Json.LabeledData import OriginalElement, LabeledData
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.ActionsForElements import ActionsForElements
import cv2 as cv

#Нужно сложить два изображения, исключая одинаковые области
list_subject = ImageLoaders.LoadBWImage("C:\Temp\Photos\data\list_subjects2.bmp")

# делаем скриншот после каждого скрола
# делим список на строки
# извлекаем текст из строк и копируем в массив
# определяем самую нижнюю строчку
# следим за её перемещением вверх во время скрола
# как только нижняя строчка исчезнула, переместившись наверх, то начинаем алгоритм сначала

from Helpers.Json import JsonHelper
import numpy as np
import pandas as pd
from Helpers.ImageLoaders import ImageLoaders
from Helpers.CommonMethods import CommonMethods
from BusinessTasks.Tasks import Tasks
import cv2
from decimal import Decimal
from Helpers.FeatureExtractors.MSER import MSER
from Helpers.Threshold import Threshold
from Helpers.ImageConverters import ImageConverters
from Helpers.Filters.ImageFilters import ImageFilters
from Helpers.MorphologicalOperations import MorphologicalOperations
from Helpers.OCR.TesseractClass import TesseractOCR
from Helpers.FeatureExtractors.Contours import Contours
from Helpers.Json.LabeledData import OriginalElement, LabeledData
from Helpers.PatternMatching.PatternMatching import PatternMatching
from Helpers.ActionsForElements import ActionsForElements

#separate each text line
list_subject1 = ImageLoaders.LoadBWImage("C:\Temp\!my\TestsTab\Subjects\subj1.bmp")

#делаем трешолд
th, threshed = cv2.threshold(list_subject1, 127, 255, cv2.THRESH_BINARY_INV)
#находим массив точек, которые не равны нулю (т.е. там где есть текст)
non_zero_points = cv2.findNonZero(threshed)

# матрицу изображения превращаем в вектор
# cv2.REDUCE_AVG - the output is the mean vector of all rows/columns of the matrix
# cv2.REDUCE_AVG - выход - это средний вектор всех строк / столбцов матрицы
# параметр "1" - dimension index along which the matrix is reduced. 0 means that the matrix is reduced to a single row. 1 means that the matrix is reduced to a single column
# параметр "1" - индекс размерности, по которому приводится матрица. 0 означает, что матрица сведена к одной строке. 1 означает, что матрица сведена к одному столбцу
hist = cv2.reduce(threshed, 1, cv2.REDUCE_AVG)
# reshape(-1) - The criterion to satisfy for providing the new shape is that 'The new shape should be compatible with the original shape
# т.е. из каких бы массивов не состоял массив, всё это будет извлечено в один вектор
# array = [[1], [2], [2]] -> arrary.shape = (3,1) -> array.reshape(-1) = [1,2,3]
hist_reshaped = hist.reshape(-1)

th = 2
H,W = list_subject1.shape[:2]
# обходим все горизонтальные точки
# решение в одну строчку
#uppers2 = [y for y in range(H-1) if hist_reshaped[y]<=th and hist_reshaped[y+1]>th]

# мы ищем такие вертикальные точки, где начинается рост яркости. От 0 до 255
# складываем их в массив
uppers = []
for i in range(H - 1):
    if(hist_reshaped[i] <= th and hist_reshaped[i + 1] > th):
        uppers.append(i)

# содаём новое изображение
finish_image = cv2.cvtColor(list_subject1, cv2.COLOR_GRAY2BGR)

# отрисовываем линии по полученным точкам максиумов
for y in uppers:
    cv2.line(finish_image, (0, y), (W, y), (255, 0, 0), 1)

# насамомделе ничего рисовать не нужно, нужны координаты полученных прямоугольников
# т.е. 1й прямоугольник это пространство между линией 1 и линией2
# плюс нужно немного сдвигать прямоугольник - текст не совсем ровно в него помещается
rectangles = []
for i in range(len(uppers) - 1):
    x = 0
    y = uppers[i]
    w = W
    h = uppers[i + 1] - uppers[i]
    tuple = (x, y, w , h)
    rectangles.append(tuple)

for r in rectangles:
    x = r[0]
    y = r[1] - 5
    w = r[2]
    h = r[3]
    point1 = (x, y)
    point2 = (x + w, y + h)
    #cv2.rectangle(list_subject1, point1, point2, (0, 0, 0), 1)
    image = CommonMethods.CropImage(list_subject1, x, y, w, h)
    #TesseractOCR.GetTextFromImage(image)

#CommonMethods.ShowImage(finish_image)
#CommonMethods.ShowImage(list_subject1)
