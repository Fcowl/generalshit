import time
import threading
from PIL import Image
import pystray
from pystray import MenuItem as item

# Пути к вашим иконкам (замените на свои файлы)
ICON_1_PATH = r"C:\Users\Fcowl\Desktop\записьесть.png"
ICON_2_PATH = r"status_red.png"


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
        time.sleep(5)
        if icon.visible:  # Проверяем, не закрыли ли приложение
            icon.icon = load_icon(ICON_2_PATH)
            icon.title = "Авто-апдейт: Обнаружена ошибка"

        time.sleep(5)
        if icon.visible:
            icon.icon = load_icon(ICON_1_PATH)
            icon.title = "Авто-апдейт: Всё ок"


def main():
    # Загружаем стартовую иконку
    start_image = load_icon(ICON_1_PATH)

    # Создаем контекстное меню, которое открывается по правому клику
    menu = pystray.Menu(
        item("Включить зеленый статус", change_to_first),
        item("Включить красный статус", change_to_second),
        item("Выход", on_exit),
    )

    # Инициализируем сам значок в трее
    # Парамeтры: Системное имя, Картинка, Всплывающая подсказка при наведении, Меню
    icon = pystray.Icon("StatusApp", start_image, "Мое Python Приложение", menu)

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
