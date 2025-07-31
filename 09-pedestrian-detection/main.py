import cv2 as cv
import os
import imutils

def detect_pedestrian(path):
    
    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

    cap = cv.VideoCapture(path)


    while True:
        ret, img = cap.read()
        if ret:
            # resize window to be 400 or less
            img = imutils.resize(img, width=min(400, img.shape[1]))
            (regions, _) = hog.detectMultiScale(img, winStride=(3,3), padding=(2,2), scale=1.05)

            # Draw rectangle
            for(x,y,w,h) in regions:
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
            cv.imshow("IMG", img)
            if cv.waitKey(25) & 0XFF == ord('q'):
                break
        
        else: break

    cap.release()
    cv.destroyAllWindows()




if __name__=='__main__':

    root = os.path.dirname(os.path.abspath(__file__))
    vidPath = os.path.join(root, "sample.mp4")
    detect_pedestrian(vidPath)