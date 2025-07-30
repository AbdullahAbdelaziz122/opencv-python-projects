import cv2

img = cv2.imread('sample.jpg')

# Average filter
avg = cv2.blur(img, (5, 5))

# Median filter
median = cv2.medianBlur(img, 5)

# Gaussian filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow('Average Blur', avg)
cv2.imshow('Median Blur', median)
cv2.imshow('Gaussian Blur', gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
