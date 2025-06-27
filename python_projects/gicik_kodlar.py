import pyautogui
import time

def mesaj():
    pyautogui.write("Bugun nasilsin?")
    pyautogui.press("enter")

while True:
    mesaj()