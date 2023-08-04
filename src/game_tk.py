
from tkinter import *
from time import *
from random import randint



bg_game = "#E3DDDC"
bg_home = "#BDA5A2" #type of grey
#variables globales
user_colors = []
color_computer = []
level = 0
loose = False
victory_var = False
#play_button
def computer_play() -> None:
    global color_computer
    color_computer = choice_level()
    for value in color_computer:
        if value == 1:
            def color_button_1():
                Button_1.config(bg="orange")
                Button_1.after(2000, lambda : Button_1.config(bg="white"))
            color_button_1()
        elif value == 2:
            def color_button_2():
                Button_2.config(bg="orange")
                Button_2.after(2000, lambda : Button_2.config(bg="white"))
            color_button_2()
        elif value == 3:
            def color_button_3():
                Button_3.config(bg="orange")
                Button_3.after(2000, lambda : Button_3.config(bg="white"))
            color_button_3()
        elif value == 4:
            def color_button_4():
                Button_4.config(bg="orange")
                Button_4.after(2000, lambda : Button_4.config(bg="white"))
            color_button_4()
        elif value == 5:
            def color_button_5():
                Button_5.config(bg="orange")
                Button_5.after(2000, lambda : Button_5.config(bg="white"))
            color_button_5()
        elif value == 6:
            def color_button_6():
                Button_6.config(bg="orange")
                Button_6.after(2000, lambda : Button_6.config(bg="white"))
            color_button_6()
           
        elif value == 7:
            def color_button_7():
                Button_7.config(bg="orange")
                Button_7.after(2000, lambda : Button_7.config(bg="white"))
            color_button_7()
        elif value == 8:
            
            def color_button_8():
                Button_8.config(bg="orange")
                Button_8.after(2000, lambda : Button_8.config(bg="white"))
            color_button_8()

        elif value == 9:
            def color_button_9():
                Button_9.config(bg="orange")
                Button_9.after(2000, lambda : Button_9.config(bg="white"))
            color_button_9()

    
def reset_values(func):
    def wrapper():
        global user_colors
        user_colors = []
        return func()
    return wrapper

@reset_values
def loose_game() -> None:
    global loose_window, loose
    loose = True
    Game_window.destroy()
    loose_window = Tk()
    loose_window.title("Mémoire séquence visuelle")
    loose_window.geometry("500x400")
    loose_window.config(bg="white") 

    End_title = Label(loose_window, text="Vous avez perdu", font=("Arial", 20), foreground="black")
    Recommencer = Button(loose_window, text="try again", font=("Helvetica", 15), command=print_game)
    Return_home = Button(loose_window, text="Menu", font=("Helvetica", 15), command=Home_page)
    loose_window.config(bg="grey")
    End_title.pack(side=TOP)
    Recommencer.place(x=55, y=200)
    Return_home.place(x=150, y=200)
    loose_window.mainloop()

@reset_values
def victory() -> None:
    global victory_var, Victory_window
    victory_var = True
    Game_window.destroy()
    Victory_window = Tk()
    Victory_window.title("Mémoire séquence visuelle")
    Victory_window.geometry("500x400")
    Victory_window.config(bg="white") 
    victory = Label(Victory_window, text="Vous avez gagné !!!", font=("Arial", 20), foreground="black")
    Recommencer = Button(Victory_window, text="try again", font=("Helvetica", 15), command=print_game)
    Return_home = Button(Victory_window, text="Menu", font=("Helvetica", 15), command=Home_page)
    victory.pack(side=TOP)
    Recommencer.place(x=55, y=200)
    Return_home.place(x=150, y=200)
    Victory_window.mainloop()

    

def retry_func(func):
    def wrapper():
        global victory_var, loose
        if victory_var == True: 
            victory_var = False
            loose = False
            Victory_window.destroy()
            try:
                Home.destroy()
            except TclError:
                pass
            else:
                Home.destroy()

        elif loose == True:
            loose = False
            victory_var = False
            loose_window.destroy()
            try:
                Home.destroy()
            except TclError:
                pass
            else:
                Home.destroy()
        elif victory_var == False and loose == False:
            Home.destroy()
        return func()
    return wrapper

def return_Home(func):
    def wrapper():
        global loose, victory_var
        if loose == True:
            loose = False
            loose_window.destroy()
        elif victory_var == True:
            victory_var = False
            Victory_window.destroy()
        return func()
    return wrapper


@retry_func
def print_game() -> None:
    global Button_1, Button_2, Button_3, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9
    global level, number_cases, Game_window
    level = 1
    number_cases = 0
    Game_window = Tk()
    Game_window.title("Mémoire séquence visuelle")
    Game_window.geometry("500x400")
    Game_window.config(bg="white") 

    puzzle_frame = Frame(Game_window, width=150, height=200)
    Level = Label(Game_window, text="Level 1", justify=CENTER, fg='black', font=("Fancy", 20))
    Button_1 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_1_user)
    Button_2 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_2_user)
    Button_3 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_3_user)
    Button_4 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_4_user)
    Button_5 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_5_user)
    Button_6 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_6_user)
    Button_7 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_7_user)
    Button_8 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_8_user)
    Button_9 = Button(puzzle_frame, text="", background="white", relief="groove", height=4, width=5, justify=CENTER, command=button_9_user)
    Start_button = Button(Game_window, text="start !", background="yellow", fg="blue", height=3, width=2, justify=CENTER, command=computer_play)


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
    Start_button.place(x=170, y=50)
    Game_window.config(background=bg_home)
    Game_window.mainloop()





def choice_level() -> list:
    global number_cases, user_colors
    colors_liste_computer = []
    older_value = 0
    new_value = 0
    if level == 1:
        number_cases = 3
        for i in range(number_cases):   # testé , fonctionne bien
            older_value = randint(1, 9)
            if colors_liste_computer != []:
                if colors_liste_computer[-1] == older_value:
                    new_value = randint(1, 9)
                    while colors_liste_computer[-1] == new_value and new_value in colors_liste_computer:
                        new_value = randint(1, 9)
                    colors_liste_computer.append(new_value)
                else:
                    colors_liste_computer.append(older_value)
            else:
                colors_liste_computer.append(older_value)
    return colors_liste_computer



def verif_end() -> None:
    verif_list = []
    k=0
    if len(user_colors) == len(color_computer):
        for i in range(0, len(color_computer)):
            if color_computer[i] in user_colors:
                verif_list.append(True)
            else:
                verif_list.append(False)
        for e in verif_list:
            if e:
                k+=1
        if k==len(color_computer):
            victory()
        else: 
            loose_game()

@return_Home 
def Home_page() -> None:
    global Home, victory_var
    Home = Tk()
    Home.title("Mémoire séquence visuelle")
    Home.geometry("500x400")
    Home.config(bg="white")
    home_text="Welcome to the memory game"
    presentation="the goal is pretty simple, you have to memorise a sequence of color\nbutton which will appear when you will click on play. After that you must try \n to replicate the sequence to reach the level"
    label_home_title = Label(Home, text=home_text, fg="black", bg="white", font=("Helvetica", 20))
    label_game_presentation = Label(Home, text=presentation, fg='black', bg="white", font=("Helvetica", 12))

    play_button = Button(Home, text="play", width=4, height=2, bg="yellow", fg="blue", font="Fancy",command=print_game)
    label_home_title.pack(side='top')
    label_game_presentation.place(x=50, y=100)

    play_button.place(x=210, y=200)
    Home.mainloop()


    
def button_1_user():
    global user_colors, index_color_user
    Button_1.config(bg="orange")
    user_colors.append(1)
    verif_end()
        
def button_2_user():
    global user_colors, index_color_user
    Button_2.config(bg="orange")
    user_colors.append(2)
    verif_end()

def button_3_user():
    global user_colors, index_color_user
    Button_3.config(bg="orange")
    user_colors.append(3)
    verif_end()

def button_4_user():
    global user_colors, index_color_user
    Button_4.config(bg="orange")
    user_colors.append(4)
    verif_end()

def button_5_user():
    global user_colors, index_color_user
    Button_5.config(bg="orange")
    user_colors.append(5)
    verif_end()

def button_6_user():
    global user_colors, index_color_user
    Button_6.config(bg="orange")
    user_colors.append(6)
    verif_end()

def button_7_user():
    global user_colors, index_color_user
    Button_7.config(bg="orange")
    user_colors.append(7)
    verif_end()

def button_8_user():
    global user_colors, index_color_user
    Button_8.config(bg="orange")
    user_colors.append(8)
    verif_end()

def button_9_user():
    global user_colors, index_color_user
    Button_9.config(bg="orange")
    user_colors.append(9)
    verif_end()

if __name__ == "__main__":
    Home_page()







