import cv2
import mediapipe as mp
import numpy as np

# Initialize mediaPipe hands to recognize your hand position
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)
drawing = False
prev_x, prev_y = None, None

# Create a blank image for drawing
canvas = None

# Create a named window and set it to be resizable
cv2.namedWindow('Hand Drawing', cv2.WINDOW_NORMAL)

# Define the default drawing color
drawing_color = (0, 255, 0)  # Green color

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Initialize canvas if not already done
    if canvas is None:
        canvas = np.zeros_like(image)

    # Flip the image horizontally to create a mirror effect
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw hand landmarks and track index fingers of both right and left hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, _ = image.shape
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            if drawing:
                if prev_x is not None and prev_y is not None:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), drawing_color, 5)
                prev_x, prev_y = x, y
            else:
                prev_x, prev_y = None, None

    # Convert the RGB image back to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Combine the original image with the canvas
    combined_image = cv2.addWeighted(image, 0.5, canvas, 0.5, 0)

    # Display the colors guide
    cv2.putText(combined_image, "Guide: ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "d" to start drawing', (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255),
                1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "r"', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "g"', (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "b"', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "y"', (10, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "c"', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "m"', (10, 135), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "w"', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "o"', (10, 165), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 165, 255), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "p"', (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 192, 203), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "u"', (10, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (128, 0, 128), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "n"', (10, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (42, 42, 165), 1, cv2.LINE_AA)
    cv2.putText(combined_image, 'press "k" to erase', (10, 225), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1,
                cv2.LINE_AA)
    cv2.putText(combined_image, 'press "s" to stop drawing', (10, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255),
                1, cv2.LINE_AA)

    # Display the combined image
    cv2.imshow('Hand Drawing', combined_image)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break
    elif key == ord('d'):  # Press 'd' to start drawing
        drawing = True
    elif key == ord('s'):  # Press 's' to stop drawing
        drawing = False
    elif key == ord('r'):  # Press 'r' to change color to red
        drawing_color = (0, 0, 255)
    elif key == ord('g'):  # Press 'g' to change color to green
        drawing_color = (0, 255, 0)
    elif key == ord('b'):  # Press 'b' to change color to blue
        drawing_color = (255, 0, 0)
    elif key == ord('y'):  # Press 'y' to change color to yellow
        drawing_color = (0, 255, 255)
    elif key == ord('c'):  # Press 'c' to change color to cyan
        drawing_color = (255, 255, 0)
    elif key == ord('m'):  # Press 'm' to change color to magenta
        drawing_color = (255, 0, 255)
    elif key == ord('k'):  # Press 'k' to change color to erase
        drawing_color = (0, 0, 0)
    elif key == ord('w'):  # Press 'w' to change color to white
        drawing_color = (255, 255, 255)
    elif key == ord('o'):  # Press 'o' to change color to orange
        drawing_color = (0, 165, 255)
    elif key == ord('p'):  # Press 'p' to change color to pink
        drawing_color = (255, 192, 203)
    elif key == ord('u'):  # Press 'u' to change color to purple
        drawing_color = (128, 0, 128)
    elif key == ord('n'):  # Press 'n' to change color to brown
        drawing_color = (42, 42, 165)

cap.release()
cv2.destroyAllWindows()
