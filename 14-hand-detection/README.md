# Hand Detection Projects

This repository contains several mini-projects focused on hand detection using Python and [MediaPipe](https://google.github.io/mediapipe/). Each project demonstrates different hand tracking and gesture recognition techniques.

## Projects Overview

- **hand-detection-live-cam.py**
    Detects and tracks hands in real-time using your webcam. Visualizes hand landmarks and connections live.

- **static-images-detection**
    Processes static images to detect hands and annotate landmarks. Useful for analyzing hand positions in photos.

- **finger-count.py**
    Counts the number of fingers shown to the camera in real-time. Displays the count on the video feed.

## Requirements

- Python 3.x
- [MediaPipe](https://pypi.org/project/mediapipe/)
- OpenCV (`opencv-python`)

Install dependencies:
```bash
pip install mediapipe opencv-python
```

## Demo

![Hand detection](images/hand_tracking.gif)
---

![Finger Counts](images/finger_count.png)
