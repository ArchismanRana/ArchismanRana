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
        hands = []  # List to store each detected hand's landmarks
        #print(results.multi_hand_landmarks) detects hand on cam

        if self.results.multi_hand_landmarks:
            for i in self.results.multi_hand_landmarks:
                hand = []
                for id, lm in enumerate(i.landmark):
                    # Convert landmark coordinates to pixel values
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand.append([id, cx, cy])

                # Append the list of landmarks for each hand
                hands.append(hand)

                if draw:
                    self.mpDraw.draw_landmarks(img, i, self.mpHands.HAND_CONNECTIONS)

        return hands, img

    def find_position(self, img, handNo=0, draw=True):
        lmList = []
        bbox = None
        flip_type = "Unknown"
        all_hands = []  # List to store landmark lists for all hands
        if self.results.multi_hand_landmarks:
            for handNo, my_hand in enumerate(self.results.multi_hand_landmarks):
                lmList = []
                x_list, y_list = [], []
                handedness = self.results.multi_handedness[handNo].classification[0].label  # Left or Right
                my_hand = self.results.multi_hand_landmarks[handNo]

                for id, lm in enumerate(my_hand.landmark):  # id is the no. belongs to the point on hand
                    # Each id has x,y,z landmark
                    # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, "cx:", cx, "cy:", cy)
                    lmList.append([id, cx, cy])
                    x_list.append(cx)
                    y_list.append(cy)
                    if draw:
                        cv2.circle(img, (cx, cy), 7, (60, 0, 150), cv2.FILLED)

                # Calculate bounding box coordinates
                if x_list and y_list:
                    x_min, x_max = min(x_list), max(x_list)
                    y_min, y_max = min(y_list), max(y_list)
                    bbox = (x_min, y_min, x_max, y_max)

                # Draw bounding box and label hand type
                if draw and bbox:
                    cv2.rectangle(img, (bbox[0] - 10, bbox[1] - 10), (bbox[2] + 10, bbox[3] + 10), (0, 255, 0), 2)
                    cv2.putText(img, f"{handedness} Hand", (bbox[0] - 10, bbox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                (255, 0, 0), 2)
                all_hands.append(lmList)  # Append landmark list for the current hand to all_hands list
        return all_hands


def main():
    pTime = 0
    cTime = 0

    detector = HandDetector()  # Call the class

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set Width
    cap.set(4, 480)  # Set Height
    cap.set(10, 50)  # Set Brightness

    while True:
        success, img = cap.read()
        img = img.astype('uint8')

        print(type(img))
        if not success or img is None:
            print("Failed to capture image")
            continue

        img = cv2.flip(img, 1)  # Flip only the display to keep natural mirroring
        hands, img = detector.findHands(img)

        all_hands = detector.find_position(img)  # Get landmarks for all detected hands

        # Loop through each hand and print the position of index finger tip
        for hand_landmarks in all_hands:
            if len(hand_landmarks) > 8:  # Ensure there's an index finger landmark
                print("Index finger tip position:", hand_landmarks[8])  # Print landmark of index finger tip

        cTime = time.time()  # current time
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Gives a delay and breaks loop if q is pressed
            break


if __name__ == "__main__":
    main()
