import cv2
import argparse
import os

ref_point = []
crop = False


def shape_selection(event,x,y,flags,param):

    global ref_point,crop

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x,y)] 

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y))

        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2) 
        cv2.imshow("image", image)


# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help ="Path to image")
# args = vars(ap.parse_args())

# image = cv2.imread(args["image"])

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "images", "cat1.png")
image = cv2.imread(path)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image",shape_selection)


while True:
    cv2.imshow("image",image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()
    elif key == ord("c"):
        break

if len(ref_point) == 2:
    crop_img = clone[ref_point[0][1]:ref_point[1][1],ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("crop_img", crop_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
