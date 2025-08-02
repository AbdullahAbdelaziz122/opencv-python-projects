import cv2
import numpy as np
import handTrackingModule as ht
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import time
import streamlit as st

# Setup streamlit
st.set_page_config(page_title="Math Vision with AI", layout="wide")
st.title("Math Vision with AI")

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox("Run", value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Response from AI")
    output_text_area = st.subheader("")


# Initialize camera
def camera(resolution=(640, 400)):
    capture = cv2.VideoCapture(1)
    capture.set(3, resolution[0])
    capture.set(4, resolution[1])
    return capture


cap = camera()
detector = ht.handDetector()

canvas = None
prev_pos = None
response = None

# setup google api key
load_dotenv()
api = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')


# Get hand info
def getHandInfo(img):
    img = detector.find_hands(img)
    hands, img = detector.find_postion(img, draw=True)
    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        handType = hand['type']
        fingers = detector.fingersUp(hand)
        return lmList, handType, fingers
    else:
        return None


# Drawing logic
def draw(frame, handInfo, prev_pos, canvas):
    lmList, handType, fingers = handInfo
    current_pos = None

    # Drawing when only index finger is up
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][1:3]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(map(int, prev_pos)), tuple(map(int, current_pos)), (255, 0, 255), 10)
        prev_pos = current_pos

    # Clear canvas if only thumb is up
    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros_like(frame)
        prev_pos = None

    else:
        prev_pos = None

    return prev_pos, canvas


last_response_time = 0
cooldown = 5  


def sendtoAI(model, canvas, fingers):
    global last_response_time
    if fingers == [0, 1, 1, 1, 1] and time.time() - last_response_time > cooldown:
        try:
            pil_image = Image.fromarray(canvas)
            response = model.generate_content(["Solve this mathematical problem", pil_image])
            last_response_time = time.time()
            return response.text if hasattr(response, "text") else "No response"
        except Exception as e:
            print(f"[ERROR] AI Error: {e}")
            return "AI error"
    else:
        return None


# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    handInfo = getHandInfo(frame)
    if handInfo:
        lmList, handType, fingers = handInfo
        # print(fingers)
        prev_pos, canvas = draw(frame, handInfo, prev_pos, canvas)

        response = sendtoAI(model, canvas, fingers)
        if response:
            print(response)

    # Merge drawing and frame
    merged = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    FRAME_WINDOW.image(merged, channels="BGR")
    if response: output_text_area.text(response)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
