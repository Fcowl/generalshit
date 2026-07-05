import time


import keyboard
import pyautogui
import pygetwindow as gw

from pygetwindow import Win32Window
import subprocess


def genshin():
    windows:list[Win32Window] = gw.getWindowsWithTitle('Genshin Impact')
    for window in windows:
        if window.title == 'Genshin Impact':
            window.restore()
            window.activate()
            break

    box = (2418, 24, 78, 78)
    box2 = (2102, 28, 71, 68)
    box3 = (600, 1334, 236, 60)
    ready_to_go = False

    try:  # если мы уже в меню гемблинга
        pyautogui.locateOnScreen("history.png", confidence=0.8,region=box3)
    except pyautogui.ImageNotFoundException:
        pass
    else:
        print('already in wish menu')
        ready_to_go= True
        
    if not ready_to_go:
        print("проверка на кретстик")
        try: # закрытие карты
            pyautogui.locateOnScreen('x.png',confidence=0.8,region=box)
        except pyautogui.ImageNotFoundException:
            pass
        else:
            print('крестик найден, нажимаем escape')
            keyboard.press_and_release('escape')

    time.sleep(1)
    if not ready_to_go:
        print('проверка на звездочку')
        try: # потдвтверждение видимости меню виша
            pyautogui.locateOnScreen('wish_logo.png',confidence=0.7,region=box2)
        except pyautogui.ImageNotFoundException:
            pass
        else:
            print('звезда найдена, pressing f3')
            ready_to_go = True
            keyboard.press_and_release('F3')

    # open wish menu
    if not ready_to_go:
        print('непосадочное положение')
        return


    time.sleep(1)
    pyautogui.moveTo(710, 1375)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    command = r'''Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex "&{$((New-Object System.Net.WebClient).DownloadString('https://gist.github.com/MadeBaruna/1d75c1d37d19eca71591ec8a31178235/raw/getlink.ps1'))} global"'''
    print('getting_link')
    _ = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True).stdout.split()[3]
    # no val needed due to link being auto copied to the clipboard

    print('link obtained')


    subprocess.run('start https://paimon.moe/wish/import',shell=True,encoding='utf-8',text=True)
    while 'Wish Counter - Paimon.moe - Opera' not in gw.getAllTitles():
        time.sleep(0.5)

    opera_window:Win32Window = gw.getWindowsWithTitle('Wish Counter - Paimon.moe - Opera')[0]
    prev_pos = opera_window.box

    opera_window.moveTo(1,1)
    opera_window.restore()
    opera_window.activate()
    keyboard.press_and_release('F11')

    time.sleep(1)
    pyautogui.click(414,1157)
    time.sleep(0.1)

    keyboard.press_and_release('CTRL+V')
    pyautogui.click(400,1212)

    for i in range(1,20):
        print(f'waiting for data to load {i}/20')
        time.sleep(1)
    pyautogui.scroll(-500)
    time.sleep(0.5)

    pyautogui.click(410,1144)
    keyboard.press_and_release('F11')
    opera_window.moveTo(prev_pos[0],prev_pos[1])
    print('data imported')

def hsr():
    pass

if __name__ == '__main__':
    wins = gw.getAllTitles()
    if 'Genshin Impact' in wins:
        genshin()
    elif 'Honkai: Star Rail' in wins:
        hsr()
    else:
        print("Игра не найдена")
