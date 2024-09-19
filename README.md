# 𝐇𝐚𝐧𝐝 𝐃𝐫𝐚𝐰𝐢𝐧𝐠
𝐀 𝐜𝐮𝐭𝐭𝐢𝐧𝐠-𝐞𝐝𝐠𝐞 𝐩𝐫𝐨𝐠𝐫𝐚𝐦 𝐭𝐡𝐚𝐭 𝐭𝐫𝐚𝐜𝐤𝐬 𝐲𝐨𝐮𝐫 𝐡𝐚𝐧𝐝 𝐦𝐨𝐯𝐞𝐦𝐞𝐧𝐭𝐬, 𝐞𝐧𝐚𝐛𝐥𝐢𝐧𝐠 𝐲𝐨𝐮 𝐭𝐨 𝐝𝐫𝐚𝐰 𝐞𝐟𝐟𝐨𝐫𝐭𝐥𝐞𝐬𝐬𝐥𝐲 𝐰𝐢𝐭𝐡 𝐣𝐮𝐬𝐭 𝐲𝐨𝐮𝐫 𝐢𝐧𝐝𝐞𝐱 𝐟𝐢𝐧𝐠𝐞𝐫.






# Hand Drawing Application using OpenCV and MediaPipe


This project is a hand-tracking application that allows users to draw on a screen by moving their index fingers in front of the webcam. It uses OpenCV for capturing video and handling user input, and MediaPipe for hand landmark detection.

## Features
- Real-time hand tracking using MediaPipe.
- Draw with your index finger in front of a webcam.
- Change drawing colors with keyboard shortcuts.
- Erase and stop/start drawing dynamically.
- Draw long lines along the index finger of both hands as you hold them together in front of the camera(useful for quick erasing).

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [How It Works](#how-it-works)
    - Importing Libraries
    - Hand Detection
    - Drawing Mechanism
    - Color Control
4. [License](#license)

---

## Installation

To use this project, you'll need Python 3.x and the following dependencies:

```bash
pip install opencv-python mediapipe numpy
```

Clone the repository:

```bash
git clone https://github.com/KianShojaei/Hand-Drawing.git
cd hand-drawing-app
```

---

## Usage

Run the script to launch the hand drawing application:

```bash
python hand_drawing.py
```

### Controls:

- **Start Drawing**: Press `d` to begin drawing with your index finger.
- **Stop Drawing**: Press `s` to stop drawing.
- **Change Color**:
  - `r` - Red
  - `g` - Green
  - `b` - Blue
  - `y` - Yellow
  - `c` - Cyan
  - `m` - Magenta
  - `w` - White
  - `o` - Orange
  - `p` - Pink
  - `u` - Purple
  - `n` - Brown
  - `k` - Eraser (Black)
- **Exit**: Press `Esc` to close the application.

---

## How It Works

### Importing Libraries

The script uses OpenCV, MediaPipe, and NumPy for video processing, hand detection, and creating the drawing canvas.

```python
import cv2
import mediapipe as mp
import numpy as np
```

### Hand Detection

MediaPipe's `Hands()` solution detects hand landmarks in the webcam feed. The index finger tip is tracked and its position is used to draw on a canvas.

```python
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
```

### Drawing Mechanism

A blank canvas (`numpy` array) is overlaid on the webcam feed. As the index finger moves, a line is drawn between consecutive positions.

```python
if drawing:
    cv2.line(canvas, (prev_x, prev_y), (x, y), drawing_color, 5)
```

The video feed and canvas are merged for display using `cv2.addWeighted`.

```python
combined_image = cv2.addWeighted(image, 0.5, canvas, 0.5, 0)
```

### Color Control

Colors are controlled using keyboard inputs. Pressing keys like `r`, `g`, `b` changes the drawing color to red, green, or blue, while other colors can also be selected as shown below.

```python
elif key == ord('r'):
    drawing_color = (0, 0, 255)  # Red
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Kian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
