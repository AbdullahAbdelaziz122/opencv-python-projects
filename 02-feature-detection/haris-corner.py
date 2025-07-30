import cv2
import numpy as np

img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris Corner Detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate for marking
dst = cv2.dilate(dst, None)

# Threshold to mark the corners
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('Harris Corners', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
