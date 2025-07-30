import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def houghLineTransform():
    root = os.getcwd()
    imgPath = os.path.join(root, "images/flowers.jpg")

    # Load in color and convert to RGB for Matplotlib
    imgColor = cv.imread(imgPath, cv.IMREAD_COLOR)
    img = cv.cvtColor(imgColor, cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(imgColor, cv.COLOR_BGR2GRAY)

    imgBlur = cv.GaussianBlur(imgGray, (21, 21), 3)
    cannyEdge = cv.Canny(imgBlur, 50, 180)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 4, 2)
    plt.imshow(imgBlur, cmap='gray')
    plt.title("Blurred")
    plt.axis("off")

    plt.subplot(1, 4, 3)
    plt.imshow(cannyEdge, cmap='gray')
    plt.title("Canny Edges")
    plt.axis("off")

    distResol = 1
    angleResol = np.pi / 180
    threshold = 50
    lines = cv.HoughLines(cannyEdge, distResol, angleResol, threshold)

    # Draw lines on the original color image
    imgLines = img.copy()
    k = 3000
    if lines is not None:
        for curLine in lines:
            rho, theta = curLine[0]
            dhat = np.array([[np.cos(theta)], [np.sin(theta)]])
            dk = rho * dhat
            lhat = np.array([[-np.sin(theta)], [np.cos(theta)]])
            p1 = dk + k * lhat
            p2 = dk - k * lhat
            p1 = p1.astype(int)
            p2 = p2.astype(int)
            cv.line(imgLines, (p1[0][0], p1[1][0]), (p2[0][0], p2[1][0]), (255, 0, 0), 2)

    plt.subplot(1, 4, 4)
    plt.imshow(imgLines)
    plt.title("Hough Lines")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    houghLineTransform()
