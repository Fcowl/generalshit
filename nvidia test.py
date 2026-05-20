from pathlib import Path
import time
import threading
from PIL import Image
import pystray
from pystray import MenuItem as item

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




#find_active_sessions()

# Пути к вашим иконкам (замените на свои файлы)
ICON_1_PATH = r"C:\Users\Fcowl\Desktop\записьесть.png"
ICON_2_PATH = r"C:\Users\Fcowl\Desktop\записинет.png"


def load_icon(path):
    """Безопасно загружает изображение для трея"""
    try:
        return Image.open(path)
    except FileNotFoundError:
        # Если картинок нет, создаем заглушку (синий квадрат) вручную
        print(f"Файл {path} не найден, создана временная заглушка.")
        return Image.new("RGB", (64, 64), color=(0, 100, 255))


def change_to_first(icon, item):
    """Переключает на первую иконку через меню"""
    icon.icon = load_icon(ICON_1_PATH)
    icon.title = "Статус: Отлично"


def change_to_second(icon, item):
    """Переключает на вторую иконку через меню"""
    icon.icon = load_icon(ICON_2_PATH)
    icon.title = "Статус: Внимание!"


def on_exit(icon, item):
    """Красиво закрывает приложение"""
    icon.stop()


def auto_update_loop(icon):

    """
    Фоновая функция. Здесь может быть ваша логика:
    проверка почты, парсинг сайтов, мониторинг нагрузки процессора и т.д.
    """
    # Ждем, пока иконка отобразится в трее
    time.sleep(2)

    # Пример: мигаем или меняем значок каждые 5 секунд

    while icon.visible:

        if find_active_sessions():
            icon.icon = load_icon(ICON_1_PATH)
            icon.title = "Запись работает"
        else:
            icon.icon = load_icon(ICON_2_PATH)
            icon.title = "Запись не работает"


        time.sleep(10)






def main():
    # Загружаем стартовую иконку
    start_image = load_icon(ICON_1_PATH)


    # Инициализируем сам значок в трее
    # Парамeтры: Системное имя, Картинка, Всплывающая подсказка при наведении, Меню
    icon = pystray.Icon("StatusApp", start_image, "Мое Python Приложение")

    # Важно: метод icon.run() полностью блокирует поток, в котором запущен.
    # Поэтому фоновые задачи (проверки, таймеры) нужно запускать ДО него в отдельном потоке.
    background_thread = threading.Thread(
        target=auto_update_loop, args=(icon,), daemon=True
    )
    background_thread.start()

    # Запускаем трей (код дальше этой строчки не пойдет, пока вы не выйдете из приложения)
    icon.run()


if __name__ == "__main__":

    main()
    pass
