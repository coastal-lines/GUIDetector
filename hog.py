from pathlib import Path
import numpy as np
from sklearn import svm
from sklearn.utils import Bunch
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from skimage.color import rgb2gray
import cv2 as cv
import pickle
from imutils.object_detection import non_max_suppression

def show(img):
    plt.imshow(img, cmap='gray')
    plt.show()

ppc = 16
container_path = "c:/Work2/Projects/gui/non_strong_examples/"
dimension = (64, 64)

image_dir = Path(container_path)
folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
categories = [fo.name for fo in folders]

descr = "A image classification dataset"
images = []
flat_data = []
target = []
hog_images = []
hog_features = []
for i, direc in enumerate(folders):
    for file in direc.iterdir():
        img = imread(file)
        img_resized = resize(img, dimension, anti_aliasing=True)
        fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
        hog_images.append(hog_image)
        hog_features.append(fd)
        #flat_data.append(img_resized.flatten())
        #images.append(img_resized)
        target.append(i)
#flat_data = np.array(flat_data)
target = np.array(target)
#images = np.array(images)

image_dataset = Bunch(data=hog_features, target=target, target_names=categories, images=hog_images, DESCR=descr)

X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.3, random_state=49)
model = svm.SVC(probability=True)
model.fit(X_train, y_train)

#dbfile = open('hog.model', 'ab')
#pickle.dump(model, dbfile)
#dbfile.close()

#model_file = open('hog.model', 'rb')
#model = pickle.load(model_file)
#model_file.close()

y2 = model.predict(X_test)
print("Accuracy on unknown data is", accuracy_score(y_test, y2))

def single_check():
    gray = imread(r"C:\Work2\Projects\gui\Screenshot_1.bmp", 0)
    img_resized = resize(gray, dimension, anti_aliasing=True)
    fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
    fd = fd.reshape(1, -1)  # re shape the image to make a silouhette of hog
    probability = model.predict_proba(fd)
    print("====")
    print("C:\Work2\Projects\gui\Screenshot_1.bmp")
    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(fd)[0]])# use the SVM model to make a prediction on the HOG features extracted from the window
    print("====")

    gray = imread(r"C:\Work2\Projects\gui\Screenshot_2.bmp", 0)
    img_resized = resize(gray, dimension, anti_aliasing=True)
    fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
    fd = fd.reshape(1, -1)  # re shape the image to make a silouhette of hog
    probability = model.predict_proba(fd)
    print("====")
    print("C:\Work2\Projects\gui\Screenshot_2.bmp")
    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(fd)[0]])# use the SVM model to make a prediction on the HOG features extracted from the window
    print("====")

    gray = imread(r"C:\Work2\Projects\gui\Screenshot_3.bmp", 0)
    img_resized = resize(gray, dimension, anti_aliasing=True)
    fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
    fd = fd.reshape(1, -1)  # re shape the image to make a silouhette of hog
    probability = model.predict_proba(fd)
    print("====")
    print("C:\Work2\Projects\gui\Screenshot_3.bmp")
    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(fd)[0]])# use the SVM model to make a prediction on the HOG features extracted from the window
    print("====")

    gray = imread(r"C:\Work2\Projects\gui\Screenshot_4.bmp", 0)
    img_resized = resize(gray, dimension, anti_aliasing=True)
    fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
    fd = fd.reshape(1, -1)  # re shape the image to make a silouhette of hog
    probability = model.predict_proba(fd)
    print("====")
    print("C:\Work2\Projects\gui\Screenshot_4.bmp")
    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(fd)[0]])# use the SVM model to make a prediction on the HOG features extracted from the window
    print("====")

    gray = imread(r"C:\Work2\Projects\gui\Screenshot_5.bmp", 0)
    img_resized = resize(gray, dimension, anti_aliasing=True)
    fd, hog_image = hog(img_resized, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
    fd = fd.reshape(1, -1)  # re shape the image to make a silouhette of hog
    probability = model.predict_proba(fd)
    print("====")
    print("C:\Work2\Projects\gui\Screenshot_5.bmp")
    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(fd)[0]])# use the SVM model to make a prediction on the HOG features extracted from the window
    print("====")


def multi_check():
    height = dimension[0]
    width = dimension[1]
    screenshot = imread("C:\Work2\Projects\gui\simple_button_screen.bmp")
    screen = resize(screenshot, (screenshot.shape[0], screenshot.shape[0]), anti_aliasing=True, mode='reflect')

    for y in range(0, screen.shape[0] - width, 4):
        for x in range(0, screen.shape[1] - height, 4):
            roi = screen[y:y + width, x:x + height]
            fd, hog_image = hog(roi, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
            fd = fd.reshape(1, -1)
            probability = model.predict_proba(fd)
            button = probability[0][0]
            nonbutton = probability[0][1]

            if (button > nonbutton):
                cv.rectangle(screen, (x, y), (x + dimension[0], y + dimension[0]), (0, 255, 0), 2)

    #(rects, weights) = hog.detectMultiScale(screen, winStride=(4, 4), padding=(8, 8), scale=1.05)

    #for (x, y, w, h) in rects:
    #    cv.rectangle(screen, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    #pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    show(screen)

#single_check()
multi_check()