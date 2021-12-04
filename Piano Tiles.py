import pyautogui
import time
import keyboard
import win32api, win32con

One = (642,386)
Two = (725,386)
Three = (805,386)
Four = (889,366)

def click(x,y):

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('r') == False:

    if pyautogui.pixel(642,386)[0] == 0:
        time.sleep(0.025)
        click(642, 386)
    if pyautogui.pixel(725,386)[0] == 0:
        time.sleep(0.025)
        click(725, 386)
    if pyautogui.pixel(805,386)[0] == 0:
        time.sleep(0.025)
        click(805, 386)
    if pyautogui.pixel(889, 386)[0] == 0:
        time.sleep(0.025)
        click(889, 386)