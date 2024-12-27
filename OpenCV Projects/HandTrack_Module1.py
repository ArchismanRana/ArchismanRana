import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, maxhands=2, detectioncon=0.5, trackcon=0.5):
        self.mode = mode
        self.maxHands = maxhands
        self.detectionCon = int(detectioncon * 100)
        self.trackCon = int(trackcon * 100)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon / 100,
                                        min_tracking_confidence=self.trackCon / 100)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks) detects hand on cam

        if self.results.multi_hand_landmarks:
            for i in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, i, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, handNo=0, draw=True): # Method for one particular method
        lmList = []  #List of Landmark positions

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(my_hand.landmark):  #id is the no. belongs to the point on hand
                #Each id has x,y,z landmark
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, "cx:", cx, "cy:", cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (60, 0, 150), cv2.FILLED)
        return lmList

def main():
    pTime = 0
    cTime = 0

    detector = HandDetector() # Call the class

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set Width
    cap.set(4, 480)  # Set Height
    cap.set(10, 50)  # Set Brightness

    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = detector.find_position(img) # id, cx, cy
        if len(lmList) != 0:
            print(lmList[8])

        cTime = time.time()  # current time
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (260, 0, 25), 2)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Gives a delay and breaks loop if q is pressed
            break


if __name__ == "__main__":
    main()