# Template Matching is a method for searching and finding the location of a template image in a larger image. 

import cv2
import numpy as np
import os

# path of images
root = os.path.dirname(os.path.abspath(__file__))
imgPath = os.path.join(root, "img.jpg")
templatePath = os.path.join(root, "football.jpg")

img = cv2.imread(imgPath,0)
template = cv2.imread(templatePath,0)


h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        
    bottom_right =(location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
