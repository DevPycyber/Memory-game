from tkinter import *

Home_page = Tk()
Home_page.title("Mémoire séquence visuelle")
Home_page.geometry("500x400")
Home_page.config(bg="white")


#variables for colors
bg_game = "#E3DDDC"

window_game = Frame(Home_page, width=500, height=400, bg=bg_game)
puzzle_frame = Frame(window_game, width=150, height=200)

#texts
home_text="Welcome to the memory game"
presentation="the goal is pretty simple, you have to memorise a sequence of color button, which whill appear when you will click on play \
    after that you must try to replicate the sequence to won the level"


#labels
label_home_title = Label(Home_page, text=home_text, fg="black")
label_game_presentation = Label(Home_page, text=presentation, bg='black')


#game_button
Button_1 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_2 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_3 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_4 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_5 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_6 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_7 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_8 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)
Button_9 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER)

#play_button
def print_game():
    puzzle_frame.place(x=180, y=80) 
    window_game.pack()
    
play_image = PhotoImage(file="./assets/play.png")
    

play_button = Button(Home_page, text="", image=play_image, width=4, height=4, command=print_game)


#print widget
label_home_title.pack(side='top')
label_game_presentation.place(x=200, y=200)
Button_1.grid(row=0, column=0)
Button_2.grid(row=0, column=1)
Button_3.grid(row=0, column=2)
Button_4.grid(row=1, column=0)
Button_5.grid(row=1, column=1)
Button_6.grid(row=1, column=2)
Button_7.grid(row=2, column=0)
Button_8.grid(row=2, column=1)
Button_9.grid(row=2, column=2)
play_button.pack(side="bottom")




Home_page.mainloop()
        











