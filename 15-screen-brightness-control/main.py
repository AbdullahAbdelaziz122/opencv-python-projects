import cv2
import screen_brightness_control as sbc
import mediapipe as mp
from math import hypot
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8,
    max_num_hands=2
)

cap = cv2.VideoCapture(1)

try:
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame from camera.")
            break

        frame = cv2.flip(frame, 1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frameRGB)

        landmark_list = []
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                for _id, landmarks in enumerate(hand_landmark.landmark):
                    height, width, _ = frame.shape
                    x, y = int(landmarks.x * width), int(landmarks.y * height)
                    landmark_list.append((_id, x, y))
                draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

        # Check if landmarks 4 (thumb tip) and 8 (index tip) exist
        if len(landmark_list) >= 9:
            x_1, y_1 = landmark_list[4][1], landmark_list[4][2]
            x_2, y_2 = landmark_list[8][1], landmark_list[8][2]

            cv2.circle(frame, (x_1, y_1), 7, (255, 255, 255), cv2.FILLED)
            cv2.circle(frame, (x_2, y_2), 7, (255, 255, 255), cv2.FILLED)
            cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)

            L = hypot(x_2 - x_1, y_2 - y_1)

            b_level = np.interp(L, [15, 220], [0, 100])
            try:
                sbc.set_brightness(int(b_level))
                # print(f"Brightness set to {int(b_level)}")
            except Exception as e:
                print(f"Could not set brightness: {e}")

        cv2.imshow("Brightness Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
