import cv2
import time
import numpy as np
import HandTrack_Module1 as HTM1
from math import hypot
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# For controlling audio
# --------------------------------------------------------------------------
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

vol_range = volume.GetVolumeRange()  # (-65.25, 0.0)

min_vol = vol_range[0]
max_vol = vol_range[1]
# --------------------------------------------------------------------------


pTime = 0
cTime = 0

detector = HTM1.HandDetector(detectioncon=0.8)  # so that it does not flicker too much

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set Width
cap.set(4, 480)  # Set Height
cap.set(10, 50)  # Set Brightness

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip only the display to keep natural mirroring
    img = detector.findHands(img)

    # Check if img is None
    if not success or img is None:
        print("Failed to capture image")
        continue

    lmList = detector.find_position(img)  # id, cx, cy
    if len(lmList) >=8:
        print(lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]  # This will give the Cx of 4 and 8th points
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (260, 0, 25), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (260, 0, 25), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (260, 0, 25), 3)
        cv2.circle(img, (cx, cy), 10, (260, 0, 25), cv2.FILLED)

        length = hypot(x2 - x1, y2 - y1)  # Distance b/w the two fingers
        print(length)

        # Hand range: 50 to 300
        # Volume range: -65.25 to 0.0
        # Convert the range
        vol = np.interp(length, [50, 300], [min_vol, max_vol])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 40:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cTime = time.time()  # current time
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 25), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Gives a delay and breaks loop if q is pressed
        break