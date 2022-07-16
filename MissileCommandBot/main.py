from pyautogui import *
import pyautogui
import time
import keyboard
from sqlalchemy import null
import win32api, win32con

time.sleep(3)


# def click():
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
#     time.sleep(0.1)


# while keyboard.is_pressed('q') == False:
#     target = pyautogui.locateCenterOnScreen('missile.png', region=(50, 800, 2500, 1300), grayscale=True, confidence=0.7)
#     if target is not None:
#         print('I can see the missiles')
#         pyautogui.moveTo(target[0],target[1]+200)
#         click()
#         # time.sleep(0.01)
#     else:
#         print('Clear Skies')
#         time.sleep(0.5)




def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    #time.sleep(0.1)

while keyboard.is_pressed('q') == False:
    target1 = pyautogui.locateCenterOnScreen('missile.png', region=(50, 400, 2500, 1100), grayscale=True, confidence=0.7)
    target2 = pyautogui.locateCenterOnScreen('missile.png', region=(50, 400, 2500, 1100), grayscale=True, confidence=0.7)
    if target1 and target2 is not None:
        lastPosition1x = []
        lastPosition1y = []
        lastPosition2x = []
        lastPosition2y = []
        lastPosition1x.append(target1[0])
        lastPosition1y.append(target1[1])
        lastPosition2x.append(target2[0])
        lastPosition2y.append(target2[1])
        correctionx = lastPosition2x[0] - lastPosition1x[0]
        correctiony = lastPosition2y[0] - lastPosition1y[0]
        firePositionx = lastPosition2x[0] + correctionx
        firePositiony = 1.25*(lastPosition2y[0] + correctiony)
        print('I can see the missiles')
        if firePositiony <= 10 or firePositiony >= 1200:
            pass
        if firePositionx <= 10 or firePositionx >= 2500:
            pass
        else:
            pyautogui.moveTo(firePositionx,firePositiony)
            click()        
            # time.sleep(0.01)
    else:
        print('Clear Skies')
        time.sleep(0.5)