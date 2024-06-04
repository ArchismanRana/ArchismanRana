import pyautogui as pg

w = pg.confirm("Do u want to close zoom meeting?", "confirmation", ["Yes", "No"])
print(w)

