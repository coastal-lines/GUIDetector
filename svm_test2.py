import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from skimage.io import imread

def show(img):
    plt.imshow(img, cmap='gray')
    plt.show()

my6 = imread("6m.bmp", 0)
my6_flat = my6.flatten()

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)

f = digits.images[5].flatten()
print("Prediction: ", clf.predict([f]))
print("Prediction: ", clf.predict([my6_flat]))