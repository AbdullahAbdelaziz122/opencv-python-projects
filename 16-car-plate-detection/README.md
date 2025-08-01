# Car Plate Detection Projects

This repository contains two OpenCV-based projects focused on car plate processing, specifically designed for Russian car plate numbers using the `haarcascade_russian_plate_number.xml` classifier. These projects leverage Haar Cascade techniques to accurately detect and extract Russian license plates from images and video streams.

## 1. Car Plate Detection

This project demonstrates basic car plate detection using OpenCV. It processes input images to identify and highlight car plates.

## 2. Car Plate Detection, Extraction, and Saving

The second project extends detection by:
- Detecting car plates in images or video frames.
- Extracting the detected plate region with pressing letter `s`.
- Saving the extracted plate image to the `plates` folder for further use.

## Demo Video

A demonstration video is available in the [`assets`](assets/) folder:

![Car Plate Detection](assets/detection.png)
---
![Car Plate Extraction](assets/saving.png)
---
![Car Plate Detection and Extraction Video](assets/car_plate_detection.mp4)

---

Feel free to explore, modify, and use these projects for your computer vision tasks!