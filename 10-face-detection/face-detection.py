# Real-Time Face Detection using your webcam as a primary camera.
import os
import cv2

def face_detect(cascadePath):
    a = cv2.CascadeClassifier(cascadePath)

    cam = cv2.VideoCapture(1)

    while True:
        ret,cam_img = cam.read()
        if ret:
            gray = cv2.cvtColor(cam_img,cv2.COLOR_BGR2GRAY)
            face = a.detectMultiScale(gray,1.3,5)
            
            for (x1,y1,w1,h1) in face:
                cv2.rectangle(cam_img,(x1,y1), (x1+w1,y1+h1),(255,0,0),5)
            cv2.imshow("Face",cam_img)
            if cv2.waitKey(1) & 0xff == ord('a'):
                break
        else: break
    cam.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
        
    root = os.path.dirname(os.path.abspath(__file__))
    vidPath = os.path.join(root, "haarcascade_frontalface_default.xml")
    if not os.path.exists(vidPath):
        raise FileNotFoundError(f"Haar cascade file not found: {vidPath}")
    face_detect(vidPath)
