import os
import time
from pathlib import Path

import keyboard
import pyautogui
import pygetwindow as gw

from pygetwindow import Win32Window
import subprocess

import sys
sys.path.append(r"C:\Users\Fcowl\PycharmProject\GeneralShit")
from functions2 import is_admin

media = Path(__file__).parent / "media"

def genshin():
    windows:list[Win32Window] = gw.getWindowsWithTitle('Genshin Impact')
    for window in windows:
        if window.title == 'Genshin Impact':
            window.restore()
            window.activate()
            break
    wish_x_path = str(media / 'wish_x.png')
    wish_x_reg = (2091, 305, 77, 76)
    
    history_path = str(media / "history.png")
    history_reg = (600, 1334, 236, 60)

    x_path = str(media / 'x.png')
    x_reg = (2418, 24, 78, 78)

    wish_path = str(media / 'wish_logo.png')
    wish_reg = (2102, 28, 71, 68)

    def open_gensh_wish():
        try:
            pyautogui.locateOnScreen(wish_x_path,confidence=0.8,region=wish_x_reg)
            return True
        except pyautogui.ImageNotFoundException:
            pass

        try:  
            pyautogui.locateOnScreen(history_path, confidence=0.8,region=history_reg)
            pyautogui.click(history_reg)
            return True
        except pyautogui.ImageNotFoundException:
            pass

        try:
            pyautogui.locateOnScreen(wish_path,confidence=0.7,region=wish_reg)
            keyboard.press_and_release('F3')
            return False
        except pyautogui.ImageNotFoundException:
            pass
    
        try: # закрытие карты
            pyautogui.locateOnScreen(x_path,confidence=0.8,region=x_reg)
            keyboard.press_and_release('escape')
            return False
        except pyautogui.ImageNotFoundException:
            pass

    while not open_gensh_wish():
        time.sleep(0.5)
        
    pyautogui.moveTo(710, 1375)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    command = r'''Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex "&{$((New-Object System.Net.WebClient).DownloadString('https://gist.github.com/MadeBaruna/1d75c1d37d19eca71591ec8a31178235/raw/getlink.ps1'))} global"'''
    print('getting_link')
    subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    print('link obtained')

    subprocess.run('start https://paimon.moe/wish/import',shell=True,encoding='utf-8',text=True)
    while 'Wish Counter - Paimon.moe - Opera' not in gw.getAllTitles():
        print('waiting for opera window')
        time.sleep(0.5)

    opera_win:Win32Window = gw.getWindowsWithTitle('Wish Counter - Paimon.moe - Opera')[0]
    prev_pos = opera_win.box

    opera_win.restore()
    opera_win.activate()
    opera_win.moveTo(1, 1)
    opera_win.maximize()
    time.sleep(1)

    pyautogui.click(400, 1212)
    keyboard.press_and_release("CTRL+V")
    pyautogui.click(400, 1292)

    opera_win.moveTo(prev_pos[0],prev_pos[1])
    opera_win.resizeTo(prev_pos[2],prev_pos[3])
    opera_win.maximize()
    print('data imported')

def hsr():
    windows: list[Win32Window] = gw.getWindowsWithTitle("Honkai: Star Rail")
    for window in windows:
        if window.title == "Honkai: Star Rail":
            window.restore()
            window.activate()
            break

    history_loc = str(media / 'history_hsr.png')
    history_reg = (1461,252,163,42)

    details_path = str(media / "view_details.png")
    details_reg = (449,1288,295,65)
    
    wish_logo_path = str(media / "wish_logo_hsr.png")
    wish_logo_reg = (1991,32,63,63)
    
    x_path = str(media / "x_hsr.png")
    x_reg = (2457,61,56,56)
        
    def open_hsr_wish():
        try:
            pyautogui.locateOnScreen(history_loc,confidence=0.8,region=history_reg)
            pyautogui.click(history_reg)
            return True
        except pyautogui.ImageNotFoundException:
            pass

        try:
            pyautogui.locateOnScreen(details_path,confidence=0.8,region=details_reg)
            pyautogui.click(details_reg)
            return False
        except pyautogui.ImageNotFoundException:
            pass
        
        try:
            pyautogui.locateOnScreen(wish_logo_path,confidence=0.8,region=wish_logo_reg)
            keyboard.press_and_release('F3')
            return False
        except pyautogui.ImageNotFoundException:
            pass
        
        try:
            pyautogui.locateOnScreen(x_path,confidence=0.8,region=x_reg)
            keyboard.press_and_release('escape')
            return False
        except pyautogui.ImageNotFoundException:
            pass

    while not open_hsr_wish():
        time.sleep(0.5)
    
    print('getting link')
    command = r"""[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12; Invoke-Expression (New-Object Net.WebClient).DownloadString("https://gist.githubusercontent.com/Star-Rail-Station/2512df54c4f35d399cc9abbde665e8f0/raw/get_warp_link_os.ps1?cachebust=srs")"""
    _ = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    print('link obtained')

    subprocess.run("start https://starrailstation.com/en/warp#import", shell=True, encoding="utf-8", text=True)
    while 'Warp Tracker | Star Rail Station Wiki - Opera' not in gw.getAllTitles():
        time.sleep(0.5)

    opera_win:Win32Window = gw.getWindowsWithTitle('Warp Tracker | Star Rail Station Wiki - Opera')[0]
    prev_loc = opera_win.box

    opera_win.moveTo(1,1)
    opera_win.restore()
    opera_win.activate()

    opera_win.moveTo(1,1)
    opera_win.resizeTo(2550,1400)
    time.sleep(1)

    pyautogui.moveTo(949,738)
    pyautogui.scroll(-2000)
    time.sleep(0.5)
    pyautogui.click(1330,1042)
    keyboard.press_and_release('CTRL+V')
    pyautogui.click(1330,1113)

    opera_win.move(prev_loc[0],prev_loc[1])
    opera_win.resizeTo(prev_loc[2],prev_loc[3])
    print('data imported')

if __name__ == '__main__':
    if not is_admin():
        print("not admin")
        os._exit(0)
    wins = gw.getAllTitles()
    if 'Genshin Impact' in wins and 'Honkai: Star Rail' in wins:
        print('открыто обе игры, какую выбрать?')
        if input() == '1':
            genshin()
        else:
            hsr()
    elif 'Genshin Impact' in wins:
        genshin()
    elif 'Honkai: Star Rail' in wins:
        hsr()
    else:
        print("Игра не найдена")
