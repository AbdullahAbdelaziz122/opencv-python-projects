import os
import cv2 as cv
import numpy as np
def record_video(filename="output.avi", duration=5):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    cap = cv.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot access webcam")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = 20
    out = cv.VideoWriter(filename, cv.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    frame_count = 0
    max_frames = duration * fps

    while frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv.imshow("Recording...", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        frame_count += 1

    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__=='__main__':
    record_video()