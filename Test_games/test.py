from tkinter import*
import threading
from time import sleep
import random
import os

win = Tk()
win.geometry("200x200")

l = []
l.append(1)
l.append(2)
lock = threading.RLock()
print(l)
a = False
b = False

def play():
    for e in l:
        if e == 1:
            B.config(bg="orange")
            
            if B["background"] == "white":
                print("orange 1")
       
        elif e == 2:
            B2.config(bg="orange")
            os.system("pause")
            if B2["background"] == "white":
                
                    print("orange 2")


B = Button(win, text="click on me", bg="white")
B2 = Button(win, text="button 2", bg="white")
Start = Button(win, text="start", bg="white", command=play)

B.pack()
B2.pack()
Start.pack()

win.mainloop()