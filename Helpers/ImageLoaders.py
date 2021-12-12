import pickle
import cv2

class ImageLoaders():
    @staticmethod
    def LoadImage(path):
        image = cv2.imread(path)
        return image

    def LoadBWImage(path):
        image = cv2.imread(path)
        image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image_bw

    @staticmethod
    def Serialize(data, name):
        with open(fr'C:\Temp2\Flash\MyLabeling\ORB\contour_{name}.data', 'w+b') as file:
            pickle.dump(data, file)

    @staticmethod
    def Deserialize(name):
        with open(fr'C:\Temp2\Flash\MyLabeling\ORB\contour_{name}.data', 'rb') as file:
            data = pickle.load(file)
            return data