import time
import pyautogui
import keyboard
import pygetwindow as gw
from pathlib import Path



REF_W = 2440
REF_H = 1440

WHITE = (223, 223, 220)
GRAY = (206, 206, 206)


def get_window():
    windows = gw.getWindowsWithTitle('Honkai: Star Rail')
    if not windows:
        return None
    hsr = windows[0]
    w, h, left, top = hsr.width, hsr.height, hsr.left, hsr.top
    if top != 0:
        top += 30
    return w, h, left, top


def rx(x, w):
    return int(x * w / REF_W)


def ry(y, h):
    return int(y * h / REF_H)


def main():
    while True:
        keyboard.wait('-')
        print()

        win = get_window()
        if win is None:
            print('Window not found')
            continue
        w, h, left, top = win

        print('locating')
        skip_x = left + int(w - w / 5.638)
        skip_y = top + int(h / 18)
        pyautogui.click(skip_x, skip_y)
        time.sleep(0.1)

        p1x = left + rx(2360, w)
        p1y = top + ry(851, h)
        p2x = left + rx(2346, w)
        p2y = top + ry(943, h)

        pix1 = pyautogui.pixelMatchesColor(p1x, p1y, WHITE, tolerance=20)
        pix2 = pyautogui.pixelMatchesColor(p2x, p2y, GRAY, tolerance=20)

        if pix1 and pix2:
            print('message box detected, closing...')
            while pix1 and pix2:
                cx = left + rx(1935, w)
                cy = top + ry(956, h)
                pyautogui.click(x=cx, y=cy)
                time.sleep(0.1)
                pix1 = pyautogui.pixelMatchesColor(p1x, p1y, WHITE, tolerance=20)
                pix2 = pyautogui.pixelMatchesColor(p2x, p2y, GRAY, tolerance=20)
            print('message box closed')
        else:
            print('clicking')
            pyautogui.click(x=left + rx(1588, w), y=top + ry(894, h))
            pyautogui.click(x=left + rx(1484, w), y=top + ry(1017, h))


if __name__ == '__main__':
    main()
