import ctypes
import os
import time
from datetime import datetime
import sys

import keyboard
import pyautogui
import pygetwindow as gw
import threading

#sys.path.append(str(Path(__file__).parent))
sys.path.append(r'C:\Users\Fcowl\PycharmProject\GeneralShit')
import functions2

def startgenshin():
    print('startgenshin started')
    try:
        console:gw.Win32Window = gw.getWindowsWithTitle("Genshin Launcher")[0]
        console.moveTo(-1000,400)
    except IndexError:
        print('console not found, ide likely')


    os.startfile(r"C:\Users\Fcowl\Desktop\genshin\3DMigotoLoader.lnk")
    print("мигото запущен")

    os.startfile(r"C:\Users\Fcowl\Desktop\genshin\fpsLNK.lnk")
    print("игра запущена")

    while "Genshin Impact" not in gw.getAllTitles():
        time.sleep(2)

    print('game found')
    #try:
    #functions2.activate(path=r"G:\Genshin Impact\Genshin Impact game\GenshinImpact.exe")
    while True:
        try:
            functions2.activate(target_title="Genshin Impact")
            break
        except Exception:
            print('nf ')
            time.sleep(1)
            continue

    # первый клик
    title_path = (
        r"C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\title.png"
    )
    counter = 0
    while True:
        try:
            pyautogui.locateOnScreen(title_path, confidence=0.6)
            pyautogui.click(1255, 800)
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print(f'title not found {counter}')
            counter+=1
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + "первый клик сделан")

    # запуск аде
    os.startfile(r"C:\Users\Fcowl\Desktop\shortcuts\Genshin Impact (ADE).lnk")
    print("ade запущено ")

    # второй клик/клик у двери
    door_path = r"C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\door.png"
    counter = 0
    while True:
        try:
            pyautogui.locateOnScreen(door_path, confidence=0.8)
            pyautogui.click(1255, 800)
            break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print(f'door not found {counter}')
            counter+=1
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]") + "второй клик")
    time.sleep(10)

    # 100% открытие карты
    x_path = r"C:\Users\Fcowl\PycharmProject\GeneralShit\Genshin\media\wish_logo.png"
    counter = 0
    while True:
        try:
            pyautogui.locateOnScreen(x_path, confidence=0.8)
            lang = functions2.get_language()
            if lang == 'ru':
                keyboard.press_and_release('ь')
            else:
                keyboard.press_and_release('m')
            print('карта открыта')
            return

        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print(f'wish logo not found {counter}')
            counter+=1

def is_genshin_running():
    time.sleep(20)
    print("is genshin running started")
    while True:
        if not functions2.is_process_running("GenshinImpact.exe"):
            print("genshin not running, exiting ")
            os._exit(1)
        time.sleep(1)

if __name__ == "__main__":
    if not functions2.is_admin():
        print("Запрос прав администратора...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Genshin Launcher")
        if not functions2.is_process_running("GenshinImpact.exe"):
            threading.Thread(target=is_genshin_running, daemon=False).start()
            startgenshin()
            os._exit(0)
        else:
            print("геншин уже запущен")
            functions2.activate(
                path=r"G:\Genshin Impact\Genshin Impact game\GenshinImpact.exe"
            )

        
