import cv2 as cv
import os


def video_reverse(videoPath):
    cap = cv.VideoCapture(videoPath)

    count = 0
    success = 1
    frame_list = []

    while success:
        success, frame = cap.read()
        frame_list.append(frame)
        count += 1

    frame_list.pop()
    frame_list.reverse()

    for frame in frame_list:
        cv.imshow("Reverse", frame)
        if cv.waitKey(25) and 0xff == ord("q"):
            break
    
    cap.release()
    cv.destroyAllWindows()



if __name__ == '__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "videos", "sample.mp4")
    video_reverse(path)