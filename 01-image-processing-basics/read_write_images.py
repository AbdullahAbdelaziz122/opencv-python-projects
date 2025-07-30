import cv2

# Read image
img = cv2.imread('sample.jpg')
cv2.imshow('Original Image', img)

# Save image
cv2.imwrite('output_saved.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
