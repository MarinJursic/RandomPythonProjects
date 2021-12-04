from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

started = False

last = []

radius = 25

time.sleep(2)

def click(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

color = (255, 219, 195)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(660,350,600,400))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                if started:
                    if not last[0]-radius <= x+660 <= last[0]+radius and not last[1]-radius <= y+350 <= last[1]+radius:
                        click(x+660,y+350)
                        time.sleep(0.05)
                        last = [x+660,y+350]
                else:
                    click(x + 660, y + 350)
                    time.sleep(0.05)
                    last = [x+660,y+350]
                    started = True

                break