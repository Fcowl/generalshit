import pyautogui
import time
from pathlib import Path
import threading
import sys
import pygetwindow as gw
import keyboard
import functions2
import atexit

# todo должна быть кнопка которая остановит прокачку арта до достижения макс уровня
condition = True
def main():
    global condition
    windows: list[gw.Win32Window] = gw.getWindowsWithTitle("Honkai: Star Rail")
    for window in windows:
        if window.title == "Honkai: Star Rail":
            hsr_window:gw.Win32Window = window
            break
    path = Path(r'C:\Users\Fcowl\PycharmProject\GeneralShit\Genshin\media')

    autoadd_reg = (2270, 853, 240, 44)
    autoadd_path = str(path/'autoadd.png')

    levelup_reg = (1986, 1282, 523, 79)
    levelup_path = str(path/'levelup.png')

    trash_reg = (357, 610, 52, 52)
    trash_path = str(path/'trash.png')

    dust_reg = (1235, 99, 92, 106)
    dust_path = str(path/'dust.png')

    maxlevel_reg = (1987, 1283, 523, 78)
    maxlevel_path = str(path/'maxlevel.png')

    condition = True
    def stop_loop():
        global condition
        condition = False
    keyboard.add_hotkey('shift+u',stop_loop)

    atexit.register(keyboard.unhook_all)
    print('waiting for u')
    while True:
        keyboard.wait('u')
        if not hsr_window.isActive:
            print('hsr_window not active')
            continue
        try:
            pyautogui.locateOnScreen(autoadd_path, region=autoadd_reg, confidence=0.8)
        except pyautogui.ImageNotFoundException:
            print("upgrade meny not found")
            continue

        condition = True
        while hsr_window.isActive and condition:

            try:
                loc = pyautogui.locateOnScreen(autoadd_path,region=autoadd_reg,confidence=0.8)
                pyautogui.click(loc)
                print('autoadd pressed')
            except pyautogui.ImageNotFoundException:
                pass

            try:
                loc = pyautogui.locateOnScreen(levelup_path,region=levelup_reg,confidence=0.8)
                pyautogui.click(loc)
                print('levelup pressed')
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                pass

            try:
                pyautogui.locateOnScreen(trash_path,region=trash_reg,confidence=0.8)
                keyboard.press_and_release('esc')
                print('esc pressed')
                time.sleep(0.2)
            except pyautogui.ImageNotFoundException:
                pass

            try:
                pyautogui.locateOnScreen(dust_path,region=dust_reg,confidence=0.8)
                keyboard.press_and_release('esc')
            except pyautogui.ImageNotFoundException:
                pass

            try:
                pyautogui.locateOnScreen(maxlevel_path,region=maxlevel_reg,confidence=0.8)
                print('maxlevel detected, ending ')
                break
            except pyautogui.ImageNotFoundException:
                print('max level not detected, continuing')
                time.sleep(0.5)

            time.sleep(0.1)
        else:
            print('while condition false, upgrading stopped')



def is_hsr_running():
    print("if hsr running started")
    time.sleep(5)
    while True:
        if not functions2.is_process_running("StarRail.exe"):
            print("hsr not running, exiting ")
            sys.exit()
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=main,daemon=True).start()
    threading.Thread(target=is_hsr_running,daemon=False).start()
