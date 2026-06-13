import psutil
from pathlib import Path
import os

with open(r'C:\Users\Fcowl\PycharmProject\GeneralShit\procesess\краш.txt' ,'w',encoding='UTF-8') as f:
    f.write('\n лист крашит \n')
    for proc in psutil.process_iter():
        #print(proc.name())
        f.write(f"{proc.name()} \n")


