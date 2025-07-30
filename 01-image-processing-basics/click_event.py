import cv2 as cv
import os


def click_event(event, x, y, flags, params):

    if event == cv.EVENT_LBUTTONUP:

        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(x)+", "+str(y), (x,y), font, 1, (255,0,0),1,2 )
        cv.imshow("Image",img)

        print(x, ", ", y)

    if event == cv.EVENT_RBUTTONUP:

        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(x)+", "+str(y), (x,y), font, 1, (255,0,0),1,2 )
        cv.imshow("Image",img)
        print(x, ", ", y)
    


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "images", "cat1.png")
    
    
    img = cv.imread(path)
    cv.imshow("Image",img)
    

    cv.setMouseCallback("Image", click_event)

    cv.waitKey(0)