# ✋ Hand Gesture Brightness Control using OpenCV & MediaPipe

Control your screen brightness in real-time using hand gestures detected by your webcam. The distance between your thumb and index finger is mapped to brightness levels (0–100%).

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** – Webcam access and drawing visuals
- **MediaPipe** – Real-time hand landmark detection
- **NumPy** – Linear interpolation
- **screen-brightness-control** – Monitor brightness control (**Windows only**)

---

## 🎯 Features

- Hand detection via MediaPipe
- Tracks distance between **thumb tip** (landmark 4) and **index tip** (landmark 8)
- Maps distance (15px → 0%, 220px → 100%) to brightness
- Real-time webcam control

---

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/AbdullahAbdelaziz122/hand-brightness-control.git
cd hand-brightness-control
```

### 2. Install Dependencies

```bash
pip install opencv-python mediapipe screen-brightness-control numpy
```

> `screen-brightness-control` works only on **Windows**. For Linux/macOS, use alternatives or comment out the brightness control line.

### 3. Run the Script

```bash
python hand_brightness_control.py
```

---

## ⚙️ Notes

- Adjust brightness sensitivity by changing the interpolation range:

    ```python
    b_level = np.interp(L, [15, 220], [0, 100])
    ```

---

## 📌 Disclaimer

This tool modifies **screen brightness directly**. Use with caution, especially on battery power or if your monitor behaves unexpectedly.

