import cv2
import os

def car_detect(cascade_path, video_path):
    car_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, image = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('cars', image)

        if cv2.waitKey(33) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    cascade_path = os.path.join(root, "./car.xml")
    video_path = os.path.join(root, "./cars.mp4")

    car_detect(cascade_path, video_path)
