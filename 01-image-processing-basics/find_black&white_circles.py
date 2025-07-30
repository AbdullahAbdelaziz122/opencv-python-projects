import cv2 as cv
import os

def find_circles(path, isWhite = 0):
    
    grayscaleImg = cv.imread(path, 0)

    # Get Threshold
    if isWhite:
        _,threshold = cv.threshold(grayscaleImg, 100, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    else:
        _,threshold = cv.threshold(grayscaleImg, 100, 255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)

    # Find contours
    contours, _ = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    
    # filter by Area 
    s1, s2 = 3, 20
    cntx = []


    for cnt in contours:
        if s1< cv.contourArea(cnt) < s2:
            cntx.append(cnt)


    print(f"Number of Circles = [{len(cntx)}]")




if __name__ == '__main__':
    root =  os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "images", "white-dot.png")
    find_circles(path, 1)
