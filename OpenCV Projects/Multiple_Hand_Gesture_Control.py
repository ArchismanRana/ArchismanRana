import time
from math import hypot
import cv2
import HandTrack_Module2 as HTM


def start_webcam_measurement():
    pTime = 0
    cTime = 0

    detector = HTM.HandDetector(detectioncon=0.5, maxhands=2)  # so that it does not flicker too much

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set Width
    cap.set(4, 480)  # Set Height
    cap.set(10, 40)  # Set Brightness

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)  # With drawing

        all_hands = detector.find_position(img)  # Get landmarks for all detected hands

        if len(hands) == 2:
            hand1, hand2 = hands[0], hands[1]
            # Index tip of both hands
            index_tip1 = hand1[8]
            index_tip2 = hand2[8]

            x1, y1 = index_tip1[1], index_tip1[2]
            x2, y2 = index_tip2[1], index_tip2[2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 10, (20, 0, 25), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (20, 0, 25), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (20, 0, 25), 3)
            cv2.circle(img, (cx, cy), 10, (260, 0, 25), cv2.FILLED)

            length = hypot(x2 - x1, y2 - y1)  # Distance b/w the two fingers
            print(length)
            cv2.putText(img, str(f"length: {length: .2f}"), (10, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (260, 0, 25), 2)

        cTime = time.time()  # current time
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (260, 0, 25), 2)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Gives a delay and breaks loop if q is pressed
            break

if __name__ == "__main__":
    start_webcam_measurement()
