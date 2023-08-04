import threading
from tkinter import *
import random
import time


win = Tk()
win.title("test")
win.geometry("200x200")

L = [random.randint(1, 2)]
if L[0] == 1: L.append(2)
else: L.append(1)

def timer_button():
    timing = None
    time1 = int(time.time())
    while True:
        time2 = time.time()
        timing = int(time2-time1)
        while int(time.time()) - time1 == timing:
            continue
        if timing >= 2:
            break
          
timer_button()


def red1():
    B1.config(bg="orange")

def white1():
    mylock = threading.Lock()
    mylock.acquire(blocking=True, timeout=3)
    mylock.release()
    B1.config(bg="white")


def start_button():
    th1.start()
    th2.start()
    th1.join()
    th2.join()
            
th1 = threading.Thread(target=red1)
th2 = threading.Thread(target=white1)
start = Button(win, text="start", command=start_button)
B1 = Button(win, text="click on me ")
B2 = Button(win, text="click on 2")
B1.pack()
B2.pack()


start.pack()
win.mainloop()



