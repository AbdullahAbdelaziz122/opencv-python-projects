import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os



def colorHistogram():
    root = os.getcwd()
    #images/flowers.jpg
    imgPath = os.path.join(root, "images/flowers.jpg")
    img = cv.imread(imgPath)
    plt.figure()
    plt.imshow(img)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)

    colors = ['b','g','r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])
        plt.xlabel('pixel int')
        plt.ylabel('% of pixels')

    plt.show()


if __name__ == "__main__":
    colorHistogram()