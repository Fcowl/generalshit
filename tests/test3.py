import sys
import threading
import time
import atexit

atexit.register(lambda:print('exited'))


def t1():
    while True:
        print('t1')
        time.sleep(1)

def t2():
    while True:
        print('t2')
        time.sleep(4)
        print( 't2')
        time.sleep(1)
        break
    print('exiting')
    sys.exit()


threading.Thread(target=t1,daemon=True).start()
threading.Thread(target=t2,daemon=False).start()

