import os
from pathlib import Path
import keyboard
import pygetwindow as gw
import pyautogui
import time

import sys
sys.path.append(r'C:\Users\Fcowl\PycharmProject\GeneralShit')
import functions2 as f2

path = Path(r'C:\Users\Fcowl\PycharmProject\GeneralShit\start_x\media')

def main():
    t1 = time.time()
    os.startfile(r"C:\Users\Fcowl\Desktop\Prism Launcher.lnk")
    counter = 0
    while True:
        try:
            loc = pyautogui.locateOnScreen(str(path/'atm10.png'),confidence=0.8)
            #time.sleep(1)
            pyautogui.click(loc,clicks=2,interval=0.2)
            print('atm10 starting')
            break
        except pyautogui.ImageNotFoundException:
            counter+=1
            print(f'locating atm10 {counter=}')
            time.sleep(0.5)

    counter = 0
    while True:
        try:
            loc = pyautogui.locateOnScreen(str(path/'singleplayer.png'),confidence=0.8)
            pyautogui.click(loc)
            print('singleplayer menu opened starting')
            break
        except pyautogui.ImageNotFoundException:
            counter+=1
            print(f'locating singleplayer {counter=}')
            time.sleep(2)

    m_window:gw.Win32Window = gw.getWindowsWithTitle('All The Mods 10 v')[0]
    #box = (m_window.left, m_window.top, m_window.width, m_window.height)
    m_window.maximize()
    time.sleep(0.05)

    pyautogui.click(1044,152)
    print('world loading ')
    os.startfile(r'C:\Windows\Explorer.EXE')
    m_window.activate()

    counter = 0
    while True:
        try:
            loc = pyautogui.locateOnScreen(str(path/'backtogame.png'),confidence=0.8)
            pyautogui.click(loc)
            print('backtogame pressed')
            break
        except pyautogui.ImageNotFoundException:
            counter+=1
            print(f'locating back to game {counter=}')
            time.sleep(2)

    for f in range(1, 4):
        time.sleep(5)
        keyboard.press_and_release("F5")
        print(f"{f=}")
    
    lang = f2.get_language()
    if lang == 'en':
        keyboard.press_and_release("`")
    else:
        keyboard.press_and_release('ё')
    time.sleep(3)

    if lang == "en":
        keyboard.press_and_release("`")
    else:
        keyboard.press_and_release("ё")
    time.sleep(0.5)
    keyboard.press_and_release("esc")
    tt = round(time.time() - t1)
    print(f"LOADED!!!!! ({tt // 60}:{tt % 60})") 


if __name__ == '__main__':
    main()