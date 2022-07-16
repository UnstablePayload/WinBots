from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(.5)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1000, 500) [0] <= 15:      # R1
        click(1000, 500)
    if pyautogui.pixel(1050, 500) [0] <= 15:      # R2
        click(1050, 500)
    if pyautogui.pixel(1150, 500) [0] <= 15:      # R3
        click(1150, 500)
    if pyautogui.pixel(1250, 500) [0] <= 15:      # R4
        click(1250, 500)



