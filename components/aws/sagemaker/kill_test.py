import time
import signal

y = 9
def unset_y():
    global y
    y = 14

def signal_term_handler(signalNumber, frame):
    i = 1
    print("term", i, frame.f_globals['y'], frame.f_locals['y'], y)
    unset_y()
    while (True):
        i = i+1
        print("term", i, frame.f_globals.keys(), frame.f_locals.keys(), y)
        time.sleep(2)

signal.signal(signal.SIGTERM, signal_term_handler)



try:
    i = 1
    global y
    y = 10
    while (True):
        print("hello", i)
        i = i+1
        time.sleep(2)
except:
    i = 1
    y = 11
    while (True):
        print("except", i)
        i = i+1
        time.sleep(1)
finally:
    i = 1
    y = 12
    while (True):
        print("finally", i)
        i = i+1
        time.sleep(1)
