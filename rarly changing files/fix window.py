import win32gui
import pygetwindow as gw

#todo автоматический детект съехавшего окна и фикс его
def move_window_no_resize(window_title, x, y):
    # Ищем окно по точному названию
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print("Окно не найдено")
        return

    # Получаем текущие координаты и размер окна
    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect

    width = right - left
    height = bottom - top

    # Перемещаем окно, сохраняя размер
    win32gui.MoveWindow(hwnd, x, y, width, height, True)

# Пример: переместить Блокнот в позицию (200, 200)
title:str = r'Opera'
title = gw.getWindowsWithTitle(title)[0].title

move_window_no_resize(title, 0, 0)