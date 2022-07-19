from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm, metrics, datasets
from sklearn.utils import Bunch
from sklearn.model_selection import GridSearchCV, train_test_split
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.draw import rectangle
from skimage.draw import rectangle_perimeter
import pickle
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import plot_roc_curve
from sklearn.datasets import load_wine
from sklearn.metrics import classification_report, confusion_matrix

def show(img):
    plt.imshow(img, cmap='gray')
    plt.show()

def check_one(num):
    show(image_dataset.images[num])
    r = model.predict([image_dataset.images[num].flatten()])
    print(model.predict([image_dataset.images[num].flatten()]))
    print(image_dataset.target_names[model.predict([image_dataset.images[num].flatten()])[0]])

def check_real_image(path, dimension):

    print("start")

    height = dimension[0]
    width = dimension[1]

    # try to find on real image
    screenshot = imread(path)
    screenshot_copy = resize(screenshot, (screenshot.shape[1], screenshot.shape[1]), anti_aliasing=True, mode='reflect')
    results = []
    for i in range(14, 4, -2):
        screen = resize(screenshot_copy, (screenshot_copy.shape[0] / i, screenshot_copy.shape[0] / i), anti_aliasing=True, mode='reflect')
        if(screen.shape[0] < dimension[0]):
            continue

        for y in range(0, screen.shape[0] - dimension[0], 10):
            for x in range(0, screen.shape[1] - dimension[0], 10):
                roi = screen[y:y + dimension[0], x:x + dimension[0]]
                #show(roi)
                #result = model.predict([roi.flatten()])[0]
                roi_flatten = [roi.flatten()]
                probability = model.predict_proba(roi_flatten)
                non_table_scores = probability[0][0]
                table_scores = probability[0][1]

                if(table_scores > non_table_scores):
                    #cv.rectangle(screenshot_copy, (x * i, y * i), ((x*i) + dimension[0], (y*i) + dimension[0]), (0, 255, 0), 2)
                    results.append((table_scores, i, x, y))
                    #print("table was detected")
        print("Screen is: " + str(i))
        #show(screenshot_copy)


    if(len(results) > 0):
        #prepare total table

        results = np.sort(results, axis=0)
        print(results)

        #calculate range for k
        temp_k = 0
        for i in range(len(results)):
            temp_k += results[i][1]
        k = temp_k // len(results)

        #calculate x and y
        temp_x = 0
        temp_y = 0
        for i in range(len(results)):
            temp_x += results[i][2]
            temp_y += results[i][3]

        x = int((temp_x // len(results)) * k)
        y = int((temp_y // len(results)) * k)

        shift = int(dimension[0]*k)
        cv.rectangle(screenshot_copy, (x, y), (x + shift, y + shift), (0, 255, 0), 2)

        show(screenshot_copy)

    print("stop")

def load_image_files(container_path, dimension):
    """
    Load image files with categories as subfolder names
    which performs like scikit-learn sample dataset

    Parameters
    ----------
    container_path : string or unicode
        Path to the main folder holding one subfolder per category
    dimension : tuple
        size to which image are adjusted to

    Returns
    -------
    Bunch
    """
    image_dir = Path(container_path)
    folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
    categories = [fo.name for fo in folders]

    descr = "A image classification dataset"
    images = []
    flat_data = []
    target = []
    for i, direc in enumerate(folders):
        for file in direc.iterdir():
            img = imread(file)
            img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
            flat_data.append(img_resized.flatten())
            images.append(img_resized)
            target.append(i)
    flat_data = np.array(flat_data)
    target = np.array(target)
    images = np.array(images)

    image_dataset =  Bunch(data=flat_data,target=target,target_names=categories,images=images,DESCR=descr)
    return image_dataset

def train_model():
    X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)
    model = svm.SVC(probability=True)
    model.fit(X_train, y_train)

    #dbfile = open('big_table_model.model', 'ab')
    #pickle.dump(model, dbfile)
    #dbfile.close()
    return model

def check(dimension):
    for_test = imread(r"C:\Work2\Projects\gui\examplesForTable\test.bmp")
    for_test = resize(for_test, dimension)
    for_test = [for_test.flatten()]
    probability = model.predict_proba(for_test)

    for ind, val in enumerate(image_dataset.target_names):
        print(f'{val} = {probability[0][ind] * 100}%')
    print("The predicted image is : " + image_dataset.target_names[model.predict(for_test)[0]])

def load_model():
    # for reading also binary mode is important
    model_file = open('big_table_model.model', 'rb')
    model = pickle.load(model_file)
    model_file.close()
    return model

dimension = (256, 256)
image_dataset = load_image_files("C:/Work2/Projects/gui/examplesForTable/", dimension)
model = train_model()
#model = load_model()
#check(dimension)
check_real_image(r"C:\Work2\Projects\gui\full_screens\big_table_test_screens\test1.bmp", dimension)