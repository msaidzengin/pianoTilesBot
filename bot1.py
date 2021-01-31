import pyautogui
from PIL import ImageGrab

y = 900
while True:
    if ImageGrab.grab().getpixel((555, y))[0] == 1 : pyautogui.click(555, y)
    if ImageGrab.grab().getpixel((620, y))[0] == 1 : pyautogui.click(620, y)
    if ImageGrab.grab().getpixel((690, y))[0] == 1 : pyautogui.click(690, y)
    if ImageGrab.grab().getpixel((750, y))[0] == 1 : pyautogui.click(750, y)
