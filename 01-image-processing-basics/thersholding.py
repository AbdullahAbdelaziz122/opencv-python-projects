import cv2

img = cv2.imread('sample.jpg', 0)  # Grayscale

# Simple Binary Thresholding
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

cv2.imshow('Binary Threshold', binary)
cv2.imshow('Adaptive Threshold', adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
