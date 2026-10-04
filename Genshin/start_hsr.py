import ctypes
import os
import subprocess
import time

import keyboard
import pyautogui
import psutil
import sys
import logging
import threading
import pygetwindow as gw
from pygetwindow import Win32Window


from pyinjector import injector, inject

#sys.argv.append('--logging')
def load_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        r"C:\Users\Fcowl\PycharmProject\GeneralShit\logs\ Startup.log", encoding="UTF-8"
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(stream_handler)
    try:
        if sys.argv[1] == '--logging':
            logger.addHandler(file_handler)
    except IndexError:
        pass
load_logger()

def is_process_running(name:str) -> bool:
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False

def inject_migoto():
    global proc
    logging.info('injecting 3dmigoto')

    while True:
        for proc in psutil.process_iter():
            try:
                if proc.name() == "StarRail.exe":
                    inject(proc.pid, r'C:\Users\Fcowl\Desktop\genshin\hsr\3dmigoto\d3d11.dll')
                    logging.info('3dmigoto загружен')
                    return


            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except injector.InjectorException:
                logging.info('нет админ прав, как ты сюда попал (инжект 3дмигото)')
                input()


def start_hsr():
    logging.info("something")
    try:
        starrail_launcher:Win32Window = gw.getWindowsWithTitle("StarRail Launcher")[0]
        starrail_launcher.moveTo(-1000,400)
    except IndexError:
        logging.info('консоль не найдена, скорее всего запуск через ide')


    threading.Thread(target=inject_migoto, daemon=True).start()
    os.startfile(r"C:\Users\Fcowl\PycharmProject\GeneralShit\Genshin\hsrFPS.cmd")
    print('hsr fps started')

    while 'Honkai: Star Rail' not in gw.getAllTitles():
        time.sleep(1)
    hsr_window:Win32Window = gw.getWindowsWithTitle('Honkai: Star Rail')[0]

    logging.info("hsr запущен")

    for k in range(10, 0, -1):
        logging.info(f"инициализация hsr {k}")
        time.sleep(1)

    hsr_window.activate()
    logging.info("цикл первого клика начинается")
    
    logo_atts = 0
    while True:
        try:
            pyautogui.locateOnScreen(r'C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\hsr\1st_logo.png',
                                     confidence=0.8)
        except pyautogui.ImageNotFoundException:
            logo_atts += 1
            logging.info(f"попытка на логотипе #{logo_atts}")
            time.sleep(1)
        else:
            for k in range(10):
                pyautogui.click(x=1300, y=700)
                time.sleep(0.3)
                logging.info(f"первый клик #{k}")

            logging.info('первый клик сделан')
            break

    logging.info("цикл второго клика начинается")
    button_atts = 0
    while True:
        try:
            pyautogui.locateOnScreen(r'C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\hsr\2nd_button.png',
                                     confidence=0.8)
        except pyautogui.ImageNotFoundException:
            button_atts += 1
            logging.info(f'попытка на кнопке #{button_atts}')
            time.sleep(1)
        else:
            pyautogui.click(x=1300, y=700)
            logging.info('второй клик сделан')
            break

    logging.info("цикл третьего клика начинается ")
    character_atts = 0
    while True:
        try:
            pyautogui.locateOnScreen(r'C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\hsr\3rd_character.png',
                                     confidence=0.8)
        except pyautogui.ImageNotFoundException:
            character_atts += 1
            logging.info(f'попытка на третьем клике #{character_atts}')
            time.sleep(1)
        else:
            time.sleep(0.3)
            # открытие карты вне зависимости от раскладки клавиатуры
            keyboard.press("m")
            time.sleep(0.1)
            keyboard.release("m")
            try:
                keyboard.press("ь")
                time.sleep(0.1)
                keyboard.release("ь")
            except ValueError:
                pass

            logging.info("карта открыта")
            break
    try:
        starrail_launcher.minimize()
    except UnboundLocalError:
        pass
    
    subprocess.run(
        r"py -3.14 C:\Users\Fcowl\PycharmProject\GeneralShit\Genshin\hsr_dialog_skipper.py",
        text=True,
        capture_output=False,
        shell=False,
        encoding="utf-8",
    )
    os._exit(0)

def is_hsr_running():
    print("if hsr running started")
    time.sleep(5)
    while True:
        if not is_process_running("StarRail.exe"):
            logging.info("hsr not running, exiting ")
            os._exit(1)
        time.sleep(1)

if __name__ == '__main__':
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    if admin:
        ctypes.windll.kernel32.SetConsoleTitleW("StarRail Launcher")
        if not is_process_running("StarRail.exe"):
            threading.Thread(target=is_hsr_running, daemon=False).start()
            start_hsr()
        else:
            logging.info("хср уже запущен")
    else:
        print("Запрос прав администратора...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)







