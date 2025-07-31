# Virtual Color-Based Drawing App 🖌️

This project is a real-time virtual drawing application using OpenCV. It allows users to draw on a canvas by moving a colored object (like a marker cap) in front of the webcam. The drawing color can be selected from a toolbar, and the canvas can be cleared—all controlled using object position and color tracking.

## Features

- 🎨 **Draw using color detection**
- 📷 **Real-time webcam feed**
- 🖍️ **Choose between 4 drawing colors (Blue, Green, Red, Yellow)**
- 🧼 **Clear the canvas with a gesture**
- ⚙️ **Adjust HSV color range interactively via trackbars**

## How It Works

- The application uses HSV color space to detect a colored object (like a blue or green cap).
- Once detected, the position of the object is tracked.
- When the object moves below the toolbar, it draws on a virtual canvas.
- If the object touches the toolbar area:
  - It selects a drawing color.
  - Or clears the canvas (if placed over the "CLEAR" box).

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:
```bash
pip install opencv-python numpy

---

```
## Usage

1. Run the script:

```bash
python your_script_name.py

```

2. A window named **"Color detectors"** will appear with sliders to adjust HSV values.

   * Use these to calibrate the color of the object you want to use for drawing.

3. Point your colored object toward the webcam.

4. Move it into the canvas area to draw.

5. Move it to the top toolbar to:

   * Select drawing colors.
   * Clear the canvas.


## Controls

| Area on Screen            | Action                                   |
| ------------------------- | ---------------------------------------- |
| "CLEAR" Box               | Clears the canvas                        |
| Color Boxes               | Selects drawing color                    |
| Main Area (below toolbar) | Draws on canvas using the detected color |

## Tips

* Use a brightly colored object that is easy to detect with HSV.
* Adjust the HSV sliders in the `"Color detectors"` window to fine-tune detection.


---

Feel free to improve or extend the project by adding:

* Save functionality
* More colors or brush types
* Gesture recognition ```