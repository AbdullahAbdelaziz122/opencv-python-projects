import cv2
import mediapipe as mp
import time

# video capture
cap = cv2.VideoCapture(1)

# MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    model_complexity=0
)

# Draw hands landmark
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert BGR to RGB
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks:
        for handType, handLMS in zip(results.multi_handedness, results.multi_hand_landmarks):
            for id, lm in enumerate(handLMS.landmark):
                h, w, c = frame.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                print(id, cx, cy, cz)
                cv2.circle(frame, (int(cx), int(cy)), 15, (0, 0, 255), cv2.FILLED, 1)

            mpDraw.draw_landmarks(frame, handLMS, mpHands.HAND_CONNECTIONS)
            type = handType.classification[0].label

    # calculate frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    text = "FPS: " + str(int(fps))
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()