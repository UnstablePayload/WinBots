from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('teeth.png', region=(950,250,750,950), grayscale=True, confidence=0.5) != None:
        print('I can see it')
        time.sleep(0.5)
    else:
        print('I do not see it')
        time.sleep(0.5)