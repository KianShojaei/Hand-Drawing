"""Webcam-based hand drawing with OpenCV and MediaPipe."""

import cv2
import mediapipe as mp
import numpy as np

from drawing_logic import get_drawing_segments


COLOR_KEYS = {
    ord("r"): ((0, 0, 255), "Red"),
    ord("g"): ((0, 255, 0), "Green"),
    ord("b"): ((255, 0, 0), "Blue"),
    ord("y"): ((0, 255, 255), "Yellow"),
    ord("c"): ((255, 255, 0), "Cyan"),
    ord("m"): ((255, 0, 255), "Magenta"),
    ord("w"): ((255, 255, 255), "White"),
    ord("o"): ((0, 165, 255), "Orange"),
    ord("p"): ((203, 192, 255), "Pink"),
    ord("u"): ((128, 0, 128), "Purple"),
    ord("n"): ((42, 42, 165), "Brown"),
    ord("k"): ((0, 0, 0), "Eraser"),
}

GUIDE_LINES = [
    'd: start drawing',
    's: stop drawing',
    'r/g/b: red / green / blue',
    'y/c/m: yellow / cyan / magenta',
    'w/o/p: white / orange / pink',
    'u/n: purple / brown',
    'k: eraser',
    'Esc: quit',
]


def main():
    """Run the hand-drawing application."""
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: could not open the webcam.")
        cap.release()
        return

    drawing = False
    previous_point = None
    canvas = None
    drawing_color = (0, 255, 0)

    try:
        with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as hands:
            cv2.namedWindow("Hand Drawing", cv2.WINDOW_NORMAL)

            while True:
                success, frame = cap.read()
                if not success:
                    print("Warning: could not read a frame from the webcam.")
                    break

                frame = cv2.flip(frame, 1)
                if canvas is None:
                    canvas = np.zeros_like(frame)

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb_frame)
                fingertips = []

                if results.multi_hand_landmarks:
                    height, width = rgb_frame.shape[:2]
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            rgb_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                        )
                        tip = hand_landmarks.landmark[8]
                        fingertips.append(
                            (int(tip.x * width), int(tip.y * height))
                        )

                segments, previous_point = get_drawing_segments(
                    fingertips, previous_point, drawing
                )
                for start, end in segments:
                    cv2.line(canvas, start, end, drawing_color, 5)

                display_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
                combined = cv2.addWeighted(display_frame, 0.5, canvas, 0.5, 0)

                for index, line in enumerate(GUIDE_LINES):
                    cv2.putText(
                        combined,
                        line,
                        (10, 25 + index * 22),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.48,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA,
                    )

                mode = "DRAWING" if drawing else "PAUSED"
                cv2.putText(
                    combined,
                    f"Mode: {mode}",
                    (10, combined.shape[0] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (0, 255, 0) if drawing else (0, 165, 255),
                    2,
                    cv2.LINE_AA,
                )
                cv2.imshow("Hand Drawing", combined)

                key = cv2.waitKey(5) & 0xFF
                if key == 27:
                    break
                if key == ord("d"):
                    drawing = True
                    previous_point = None
                elif key == ord("s"):
                    drawing = False
                    previous_point = None
                elif key in COLOR_KEYS:
                    drawing_color = COLOR_KEYS[key][0]

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
