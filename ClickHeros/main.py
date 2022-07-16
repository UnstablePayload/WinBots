from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading

time.sleep(5)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

# def do_click():
while keyboard.is_pressed('q') == False:
    click()


# threads = []

# for i in range(50):   
#     t = threading.Thread(target=do_click)
#     t.daemon = True
#     threads.append(t)

# for i in range(50):
#     threads[i].start()

# for i in range(50):
#     threads[i].join()

    
