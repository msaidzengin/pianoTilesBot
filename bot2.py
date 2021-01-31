import pyautogui
from PIL import ImageGrab
import time

# https://www.1001oyun.com/oyun/piano-tiles-2.html

def press(key, second):
    pyautogui.keyDown(key)
    time.sleep(second)
    pyautogui.keyUp(key)

y = 900
while True:
    time.sleep(0.05)
    a = ImageGrab.grab().getpixel((555, y))[0]
    b = ImageGrab.grab().getpixel((620, y))[0]
    c = ImageGrab.grab().getpixel((690, y))[0]
    d = ImageGrab.grab().getpixel((750, y))[0]

    if a == 1 : pyautogui.press('d')
    if b == 1 : pyautogui.press('f')
    if c == 1 : pyautogui.press('j')
    if d == 1 : pyautogui.press('k')

    if a == 0 : press('d', 0.3)
    if b == 0 : press('f', 0.3)
    if c == 0 : press('j', 0.3)
    if d == 0 : press('k', 0.3)
