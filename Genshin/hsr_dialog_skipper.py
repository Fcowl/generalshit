import os
import time

import pyautogui
import keyboard
import threading
from pathlib import Path
import pygetwindow as gw
#import psutil

media_path = Path(__file__).parent / 'media'

skip_button_box = (1900,65,240,32)

little_x_box = (2294,296,53,52)

white_target_color =(223, 223, 220)
gray_target_color = (206, 206, 206)
loc = pyautogui.locateOnScreen(str(media_path / 'skip_button.png'), confidence=0.5)
print(loc)

def main():
    print('dialog skipper started')
    while True:
        #time.sleep(1)
        keyboard.wait('b')
        print('')
        try:
            print('locating')
            loc = pyautogui.locateOnScreen(str(media_path / 'skip_button.png'), confidence=0.5, region=skip_button_box)
        except pyautogui.ImageNotFoundException:
            print("skip button not found")
            print('trying to locate message box')
            pix1 = pyautogui.pixelMatchesColor(2360, 851, white_target_color, tolerance=20)
            pix2 = pyautogui.pixelMatchesColor(2346, 943, gray_target_color, tolerance=20)

            #print(pix1,pix2,pyautogui.pixel(2360,851),pyautogui.pixel(2346,943))
            if not (pix1 and pix2):
                print('message box not found')
                continue

            print('message box found')
            while pix1 and pix2 and gw.getActiveWindow().title == 'Honkai: Star Rail':
                try:
                    pyautogui.locateOnScreen(str(media_path / 'little x.png'),confidence=0.8,region=little_x_box)
                    pyautogui.click(little_x_box)
                    break
                except pyautogui.ImageNotFoundException:
                    pyautogui.click(x=1935, y=956)
                #pix1 = pyautogui.pixelMatchesColor(2360, 851, white_target_color, tolerance=20)
                #pix2 = pyautogui.pixelMatchesColor(2346, 943, gray_target_color, tolerance=20)
                time.sleep(0.1)

            print('message box closed')
        else:
            print('clicking')
            pyautogui.click(loc,clicks=2)
            time.sleep(0.10)
            pyautogui.click(x=1588, y=894)
            pyautogui.click(x=1484, y=1017)

def hsr_running():
    print('is running started')
    while True:
        try:
            gw.getWindowsWithTitle('Honkai: Star Rail')[0]
        except IndexError:
            print('hsr not found')
            os._exit(0)
        else:
            time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=main).start()
    threading.Thread(target=hsr_running).start()
    #main()

