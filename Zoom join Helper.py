import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser         #To open link in chrome
import pyautogui as pg    #For messagebox

keyboard = Controller()

Class_Start = False

for i in lst:
    while True:
        if not Class_Start:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                Class_Start = True
        else:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                confirm = pg.confirm("Do u want to close zoom meeting?", "confirmation", ["Yes", "No"])
                if confirm == "Yes":
                    keyboard.press('w')
                    keyboard.release('w')
                    time.sleep(1)
                    keyboard.press(Key.enter)
                    Class_Start = False
                    break
                else:
                    time.sleep(60)
                    continue

        time.sleep(2)
