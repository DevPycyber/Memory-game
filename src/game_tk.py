from tkinter import *

Home_page = Tk()
Home_page.title("Mémoire séquence visuelle")
Home_page.geometry("500x400")
Home_page.config(bg="white")

#variables for colors
bg_game = "#E3DDDC"
bg_home = "#BDA5A2" #type of grey
#texts
home_text="Welcome to the memory game"
presentation="the goal is pretty simple, you have to memorise a sequence of color\nbutton which will appear when you will click on play. After that you must try \n to replicate the sequence to reach the level"


#labels
label_home_title = Label(Home_page, text=home_text, fg="black", bg="white", font=("Helvetica", 20))
label_game_presentation = Label(Home_page, text=presentation, fg='black', bg="white", font=("Helvetica", 12))


#game_button

#play_button
def print_game():
    for c in Home_page.winfo_children():
        c.destroy()
    puzzle_frame = Frame(Home_page, width=150, height=200)
    Level = Label(Home_page, text="Level 1", justify=CENTER, fg='black', font=("Fancy", 20))
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
    Level.pack(side=TOP)
    puzzle_frame.place(x=170, y=100)
    Home_page.config(background=bg_home)
    

    

play_button = Button(Home_page, text="play", width=4, height=2, bg="yellow", fg="blue", font="Fancy",command=print_game)
#print widget
label_home_title.pack(side='top')
label_game_presentation.place(x=50, y=100)

play_button.place(x=210, y=200)
Home_page.mainloop()
        











