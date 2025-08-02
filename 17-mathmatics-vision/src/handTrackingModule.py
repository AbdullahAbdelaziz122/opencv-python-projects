import cv2
import mediapipe as mp

class handDetector:
    def __init__(self,
               static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.static_image_mode,
            max_num_hands=self.max_num_hands,
            model_complexity=self.model_complexity,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.tipsIds = [4, 8, 12, 16, 20]

    def find_hands(self, img, draw=True):
        # img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_postion(self, img, draw=True):
        myHand = {}
        lmList = []
        allHands = []

        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):

                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z *w)
                    lmList.append([id, cx, cy, cz])
                    myHand['lmList'] = lmList
                    myHand['type'] = "Right" if handType.classification[0].label == "Left" else "Left"
                    allHands.append(myHand)
                
                
                if draw:
                    cv2.circle(img, (lmList[8][1], lmList[8][2]), 5, (255, 0, 0), cv2.FILLED)
        
            
        return allHands, img
    
    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        fingers = []
        myHandType = myHand["type"]
        lm_list = myHand["lmList"]
        # Removing the first element from each sublist
        myLmList = [sublist[1:] for sublist in lm_list]

        # Printing the updated list
        #print(myLmList)
        if self.results.multi_hand_landmarks:

            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipsIds[0]][0] > myLmList[self.tipsIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipsIds[0]][0] < myLmList[self.tipsIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipsIds[id]][1] < myLmList[self.tipsIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers



def main():
    cap = cv2.VideoCapture(1)
    detector = handDetector()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = detector.find_hands(frame)
        allhands, frame = detector.find_postion(frame)

        if allhands:
            print(allhands)
            hand1 = allhands[0]
            lmList = hand1['lmList']
            type = hand1['type']

            cv2.circle(frame, (lmList[4][1], lmList[4][2]), 5, (0, 255, 0), cv2.FILLED)
            fingers = detector.fingersUp(hand1)
            print(fingers)
            print(f"H1 = {fingers.count(1)}", end = "")
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()