import time

import pyautogui
import os
import sys
import logging
import functions2
from pathlib import Path
from datetime import datetime
#parent_dir = os.media_path.abspath(os.media_path.join(os.media_path.dirname(__file__), ".."))
#sys.media_path.append(parent_dir)

def log():
    # 1. Настройка логирования (в файл + консоль)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(r'C:\Users\Fcowl\PycharmProject\GeneralShit\logs\ Startup.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
log()
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # Логируем ошибку
    logging.error("Неперехваченная ошибка:", exc_info=(exc_type, exc_value, exc_traceback))
    logging.error("Произошла ошибка, детали в Startup.log")
sys.excepthook = handle_exception

def start_tg():
    # красивый запуск тг
    pos_before = pyautogui.position()
    if not functions2.is_process_running("Telegram.exe"):
        telegram_icon = r"C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\image_assets\telegram_logo.png"
        try:
            location = pyautogui.locateOnScreen(telegram_icon,confidence=0.8)
            if location:
                pyautogui.click(location)
                print("telegram starting (click)")
                pyautogui.moveTo(pos_before)
        except pyautogui.ImageNotFoundException:
            # если по какой-то причине не получилось найти иконку и кликнуть
            print("не получилось запустить тг кликом")


def find_last_playtime_counter_v():
    path = Path(r"C:\Users\Fcowl\PycharmProject\Playtime_Counter_git\dist")
    files = list(path.glob("playtime_*.exe"))
    latest = max(
        files,
        key=lambda f: datetime.strptime(
            f.stem.removeprefix("playtime_"),
            "%d-%m-%Y"
        )
    )
    return latest.name, latest

def startup():
    try:
        pl_counter = find_last_playtime_counter_v()
    except ValueError:
        logging.error("pl counter broken")

    proc_path:dict[str,str] = {'Telegram.exe':r"C:\Users\Fcowl\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk",
                               'Discord.exe':r"C:\Users\Fcowl\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
                               'opera.exe':r"C:\Users\Fcowl\AppData\Local\Programs\Opera GX\opera.exe",
                               'Spotify.exe':r"C:\Users\Fcowl\AppData\Roaming\Spotify\Spotify.exe",
                               f'{pl_counter[0]}':f"{pl_counter[1]}"}
                               #'SpotifyGlobal.exe':r'C:\Users\Fcowl\PycharmProject\FinallyWorkingDs\spotify global\SpotifyGlobal.exe'}

    logging.info("Начался запуск начальных приложений")
    start_tg()
    for proc,path in proc_path.items():
        if not functions2.is_process_running(proc):
            try:
                os.startfile(path)
            except FileNotFoundError:
                logging.error(f'Не удается найти указанный файл: {path}')
            else:
                logging.info(f"{proc} starting")
    logging.info("Все запущено, выход")
    time.sleep(1)

if __name__ == '__main__':
    logging.info('')
    startup()