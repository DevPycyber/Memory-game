from tkinter import *

windows = Tk()
windows.title("Mémoire séquence visuelle")
windows.geometry("500x400")
windows.config(bg="#E3DDDC")
puzzle_frame = Frame(windows, width=150, height=200)


Button_1 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_2 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_3 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_4 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_5 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_6 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_7 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_8 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_9 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)

Button_1.grid(row=0, column=0)

Button_2.grid(row=0, column=1)

Button_3.grid(row=0, column=2)
Button_4.grid(row=1, column=0)
Button_5.grid(row=1, column=1)
Button_6.grid(row=1, column=2)
Button_7.grid(row=2, column=0)
Button_8.grid(row=2, column=1)
Button_9.grid(row=2, column=2)

puzzle_frame.place(x=180, y=80)
windows.mainloop()
        











