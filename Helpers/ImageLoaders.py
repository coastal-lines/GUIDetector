import pickle
import cv2

class ImageLoaders():
    @staticmethod
    def LoadImage(path):
        image = cv2.imread(path)
        return image

    @staticmethod
    def Serialize(data, name):
        with open(fr'C:\Temp2\Flash\MyLabeling\ORB\contour_{name}.data', 'w+b') as file:
            pickle.dump(data, file)

    @staticmethod
    def Deserialize(name):
        with open(fr'C:\Temp2\Flash\MyLabeling\ORB\contour_{name}.data', 'rb') as file:
            data = pickle.load(file)
            return data