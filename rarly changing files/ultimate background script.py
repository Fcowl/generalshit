#todo автоматическая остановка записи и обоев если нет активности 10 минут, уведомление о выключенной записи при обноружнении активности , вкл обоев (обои с помощью фонового процесса)
import os
from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import threading
from pathlib import Path

import keyboard

log_path = Path(r"C:\Users\Fcowl\AppData\Local\NVIDIA Corporation\NVIDIA Overlay\CxNative_NVIDIA Overlay.log")



def find_new_sessions(lines):
    new_ses = []
    for line in lines[::-1]:
        if 'Created new capture session type' in line:
            new_ses.append(line[-17:][:-1])
    return new_ses


def find_closed_sessions(lines):
    closed_ses =[]
    for line in lines[::-1]:
        if 'DestroyCaptureSession session' in line:
            closed_ses.append(line[-17:][:-1])
    return closed_ses

def find_active_sessions():
    lines = log_path.read_text().splitlines()
    #print(lines[-1])
    active = find_new_sessions(lines)
    closed = find_closed_sessions(lines)
    return len(active) - len(closed) >=1


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    last_input_info = LASTINPUTINFO()
    last_input_info.cbSize = sizeof(last_input_info)
    windll.user32.GetLastInputInfo(byref(last_input_info))

    # Время последней активности в миллисекундах
    last_time = last_input_info.dwTime

    # Текущее время системы в миллисекундах
    current_time = windll.kernel32.GetTickCount()

    # Разница — это время бездействия
    return (current_time - last_time) / 1000.0

# todo после нажатия комбинаций клавиш нужно к времени активности прибавлять 10 минут (или сколько нужно для выполления скрипта)
def main():
    stopped = False
    while True:
        time.sleep(1)
        d = get_idle_duration()
        print(d)
        if d > 10:
            if stopped:
               continue
            os.startfile(Path() / r"C:\Users\Fcowl\PycharmProject\GeneralShit\dist\stop_wallpaper.exe")
            if find_active_sessions():
                keyboard.press_and_release('alt+shift+f10')
            stopped = True
        else:
            if not stopped:
                continue
            os.system('taskkill /F /IM stop_wallpaper.exe')
            if not find_active_sessions():
                keyboard.press_and_release('alt+shift+f10')



if __name__ == '__main__':
    threading.Thread(target=main,daemon=False).start()
