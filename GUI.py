import numpy as np
import random
from colorama import init, Fore, Style
from tkinter import *


def set_difficulty_level():
    while True:
        level = int()
        dif = choose_difficulty(level)
        if dif.isdigit() and int(dif) in [1, 2, 3]:
            return int(dif)
        else:
            print("Invalid input. Please choose a number between 1 and 3.")

def choose(choosenumber):
    number = str(radio_state.get())
    choosenumber = number
    return choosenumber

def choose_difficulty(dif_num):
    number = str(dif_state.get())
    dif_num = number
    return dif_num

def close():
    window.quit()

window = Tk()
window.title("Difficulty and Algorithm")
window.minsize(width=500,height=300)

my_label1 = Label(text="Welcome to connect 4 ",font=("Arial",24,"bold"))
my_label2 = Label(text="Choose Algorithm Type")
my_label1.pack()
my_label2.pack()
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Minimax Algorithm",value=1,variable=radio_state)
radiobutton1.pack()
radiobutton2 = Radiobutton(text="Minimax Alpha-Beta Algorithm",value=2, variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()

my_label3 = Label(text="Choose difficulty of the game",font=("Arial",16,"bold"))
my_label3.pack()
dif_state = IntVar()
difficulty1 = Radiobutton(text="1",value=1,variable=dif_state)
difficulty2 = Radiobutton(text="2",value=2,variable=dif_state)
difficulty3 = Radiobutton(text="3",value=3,variable=dif_state)
difficulty1.pack()
difficulty2.pack()
difficulty3.pack()

button = Button(window,text= "Play!", font=("Calibri",14,"bold"), command=close)
button.pack()

window.mainloop()
