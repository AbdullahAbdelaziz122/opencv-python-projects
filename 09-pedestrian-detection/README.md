# Pedestrian Detection with OpenCV

This project demonstrates pedestrian detection in video files using OpenCV's HOG (Histogram of Oriented Gradients) descriptor and SVM-based people detector.

## Features

- Detects pedestrians in a video stream.
- Draws bounding boxes around detected pedestrians.
- Resizes frames for efficient processing.
- Press `q` to exit the video window.

## Usage

1. Place your video file as `sample.mp4` in the project directory.
2. Run the script:

    ```bash
    python main.py
    ```

## Requirements

Install dependencies with:

```bash
pip install opencv-python imutils
```

## How It Works

- Loads the video file.
- Initializes HOG descriptor with the default people detector.
- Processes each frame:
  - Resizes frame to a max width of 400 pixels.
  - Detects pedestrians.
  - Draws rectangles around detected regions.
  - Displays the frame.
- Stops when the video ends or you press `q`.

## File Structure

```
09-pedestrian-detection/
├── main.py
├── sample.mp4
└── README.md
```

## References

- [OpenCV HOGDescriptor Documentation](https://docs.opencv.org/)
- [imutils Library](https://github.com/jrosebr1/imutils)
