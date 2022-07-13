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

def show(img):
    plt.imshow(img, cmap='gray')
    plt.show()

def check_one(num):
    show(image_dataset.images[num])
    r = model.predict([image_dataset.images[num].flatten()])
    print(model.predict([image_dataset.images[num].flatten()]))
    print(image_dataset.target_names[model.predict([image_dataset.images[num].flatten()])[0]])

def check_real_image():
    # try to find on real image
    test = imread(r"C:\Users\PavelIankin\Desktop\gui\full_screens\tests_main.bmp")
    #test = rgb2gray(test)
    test = resize(test, (1000, 1000), anti_aliasing=True, mode='reflect')

    results = []
    for i in range(929 - 64):
        for j in range(620 - 64):
            roi = test[i:i + 64, j:j + 64]
            result = model.predict([roi.flatten()])
            #results.append(result)
            #print(result)
            if(result == 0):
                start = (i, j)
                rr, cc = rectangle_perimeter(start, extent=(64, 64))
                test[rr, cc, :] = (255, 0, 0)
                print("button")
        print(i)

    show(test)

    print("stop")

def load_image_files(container_path, dimension=(64, 64)):
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

    return Bunch(data=flat_data,
                 target=target,
                 target_names=categories,
                 images=images,
                 DESCR=descr)

image_dataset = load_image_files("C:/Users/PavelIankin/Desktop/gui/examples/")
X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.3,random_state=109)
model = svm.SVC(probability=True)
model.fit(X_train, y_train)


for_test = imread(r"C:\Users\PavelIankin\Desktop\gui\examples\textboxes\Screenshot_53.bmp")
for_test=resize(for_test,(64,64,3))
for_test=[for_test.flatten()]
probability=model.predict_proba(for_test)

for ind,val in enumerate(image_dataset.target_names):
    print(f'{val} = {probability[0][ind]*100}%')

print("The predicted image is : " + image_dataset.target_names[model.predict(for_test)[0]])

#check_one(230)
#check_real_image()

