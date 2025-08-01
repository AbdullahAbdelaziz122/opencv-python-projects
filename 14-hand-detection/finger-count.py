import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    model_complexity = 0,
    max_num_hands = 1,
    min_detection_confidence = 0.7
)

# camera capture
cap = cv2.VideoCapture(1)

def count_finger(hand_landmarks):
    fingers = []

    landmarks = hand_landmarks.landmark

    # verify if thump tip is x postion is greater than thump joint
    fingers.append(landmarks[4].x < landmarks[3].x)

    # Rest of the hand y postion of tip against joint
    for tip in [8, 12, 16 ,20]:
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y)

    return fingers.count(True)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame =cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_finger(hand_landmarks=hand_landmarks)
            cv2.putText(frame, f"Fingers:{finger_count}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release
cv2.destroyAllWindows()

