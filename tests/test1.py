import keyboard
import pyautogui
import time
import pygetwindow as gw
from pygetwindow import Win32Window

time.sleep(1)
print('beggining')
box = (2418,24,78,78)
box2 = (2102,28,71,68)
box3 = (600,1334,236,60)
skip_button_box = (2087,65,40,32)
hsr_window = gw.getActiveWindow()
window_width = hsr_window.width
window_height = hsr_window.height
gw.getWindowsWithTitle('Honkai: Star Rail')[0]
print(hsr_window)
try:
    loc = pyautogui.locateOnScreen(r'C:\Users\Fcowl\PycharmProject\GeneralShit\Genshin\media\skip_button.png',confidence=0.5)
except pyautogui.ImageNotFoundException:
    print('not found')
else:
    pyautogui.moveTo(loc)

    print(loc)

