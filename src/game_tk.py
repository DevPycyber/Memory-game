from tkinter import *
import random

main = Tk()
main.title("memory game")
main.geometry("600x400")

#intialisation des variables

#variable de boutons
Button1 = Button(main, text="...", font=("Arial", 20))
Button2 = Button(main, text="...", font=("Arial", 20))
Button3 = Button(main, text="...", font=("Arial", 20))
Button4 = Button(main, text="...", font=("Arial", 20))
Button5 = Button(main, text="...", font=("Arial", 20))
Button6 = Button(main, text="...", font=("Arial", 20))
Button7 = Button(main, text="...", font=("Arial", 20))
Button8 = Button(main, text="...", font=("Arial", 20))
Button9 = Button(main, text="...", font=("Arial", 20))


#listes
liste_boutons = [Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8]
ligne1 = [Button1, Button2, Button3]
ligne2 = [Button4, Button5, Button6]
ligne3 = [Button7, Button8, Button9]
lignes = [ligne1, ligne2, ligne3]

x = 100
y = 50  
for buttons in ligne1:
    buttons.place(x=x, y=y)
    x += 48

x = 100
y = 105
for buttons in ligne2:
    buttons.place(x=x, y=y)
    x+=48

x = 100
y = 160
for buttons in ligne3:
    buttons.place(x = x, y = y)
    x+= 48





main.mainloop()


liste_pc = liste_boutons
coup_user = 0
liste_boutton_user = []
pc_nb_cases_a_allumer = 0

#variables de lancement
continuer_jeu = True




    
    












