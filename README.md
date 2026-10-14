# Hand Drawing

A real-time hand-tracking drawing application built with Python, OpenCV, MediaPipe, and NumPy. Use your index finger to draw in the air, or bring both hands into view to draw a line between their index fingertips.

## Features

- Tracks up to two hands using MediaPipe.
- Draws a freehand stroke when one index fingertip is visible.
- Draws a segment between the two index fingertips when both hands are visible.
- Supports multiple drawing colors and an on-canvas eraser.
- Lets you pause and resume drawing without connecting unrelated points.
- Includes a small, dependency-free drawing-logic module with unit tests.

## Requirements

- Python 3
- A working webcam
- The Python packages listed in `requirements.txt`

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/KianShojaei/Hand-Drawing.git
cd Hand-Drawing
```

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application

From the repository root:

```bash
python DrawTable/main.py
```

Allow the application to access your webcam if your operating system asks for permission. Press `Esc` in the application window to exit.

## Controls

| Key | Action |
| --- | --- |
| `d` | Start drawing |
| `s` | Stop drawing |
| `r` | Red |
| `g` | Green |
| `b` | Blue |
| `y` | Yellow |
| `c` | Cyan |
| `m` | Magenta |
| `w` | White |
| `o` | Orange |
| `p` | Pink |
| `u` | Purple |
| `n` | Brown |
| `k` | Eraser |
| `Esc` | Exit |

The selected color remains active until another color key is pressed. The eraser uses the canvas background color, so it removes existing strokes along the eraser path.

## Drawing behavior

- **One hand detected:** move the index fingertip to create a continuous stroke.
- **Two hands detected:** a line is drawn between the two index fingertips on each frame. Moving the hands changes the segment, allowing long lines to be drawn.
- **No hands detected:** the current single-hand stroke anchor is reset to avoid drawing a connecting line when a hand reappears.
- **Drawing paused:** no new strokes are added.

## Tests

The drawing-segment selection logic does not require a webcam or the computer-vision packages. Run its unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

These tests cover single-hand strokes, the two-hand segment, paused drawing, and transitions when hands enter or leave the frame. They do not replace a manual webcam test of the full application.

## Project structure

```text
Hand-Drawing/
├── DrawTable/
│   ├── main.py
│   └── drawing_logic.py
├── tests/
│   └── test_drawing_logic.py
├── requirements.txt
└── README.md
```

## Troubleshooting

- **The webcam does not open:** close other apps that may be using it and check your operating-system camera permissions.
- **The application starts but does not track your hand:** improve lighting, keep your hand in the camera frame, and avoid covering the index fingertip.
- **A dependency fails to install:** check your Python version and consult the installation guidance for OpenCV and MediaPipe.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for the full terms.
