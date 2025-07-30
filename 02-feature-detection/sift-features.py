import cv2 as cv
import matplotlib.pyplot as plt
import numpy
import os


def SIFT(path):
   
    imgGray = cv.imread(path, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    keypoints = sift.detect (imgGray, None)
    imgGray = cv.drawKeypoints(imgGray, keypoints, imgGray, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    plt.figure()
    plt.imshow(imgGray)
    plt.show()

if __name__ == "__main__":
    root =  os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "images", "flowers.jpg")
    SIFT(path)