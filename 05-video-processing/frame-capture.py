import cv2 as cv
import os


def frame_capture(videoPath):
    vidObj = cv.VideoCapture(videoPath)

    count = 0
    success = 1

    while success:
        success, image = vidObj.read()
        cv.imwrite("Frame%d.jpg" % count, image)
        count += 1




if __name__ == '__main__':
    path = os.path.join(os.getcwd, "videos\sample.mov")
    frame_capture(path)