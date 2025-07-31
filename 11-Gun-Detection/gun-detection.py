import cv2
import os
import imutils

def gun_detect(cascadePath):
    gun_cascade = cv2.CascadeClassifier(cascadePath)
    cam = cv2.VideoCapture(1)  # Use 0 for default webcam

    gun_exist = False

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        guns = gun_cascade.detectMultiScale(gray, 1.3, 5, maxSize=(500, 500))

        for (x, y, w, h) in guns:
            gun_exist = True
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Gun Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    if gun_exist:
        print("GUN DETECTED")
    else:
        print("NO GUN DETECTED")

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    cascadePath = os.path.join(root, "./gun_cascad.xml")
    gun_detect(cascadePath)
