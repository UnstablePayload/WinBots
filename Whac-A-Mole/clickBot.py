from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(950,250,750,950))
    width, height = pic.size

    for x in range(0,width,1):
        for y in range(0,height,1):
            r,g,b = pic.getpixel((x,y))

            if r == 70:
                click(x+950,y+250)
                break

                
