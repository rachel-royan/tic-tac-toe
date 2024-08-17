import tkinter as tk 
from tkinter import ttk 

from src.board import Board

def display_cross(b):
    b.config(text="X")

def display_circle(b):
    b.config(text="O")

def check_turn(b):
    b.config(text="O")
    b.config(text="X")

def play_game(player_mode, root):
    root.destroy()
    window = tk.Tk() 
    window.title('TIC-TAC-TOE STARTUP') 
    window.geometry('500x250')

    new_board = Board(player_mode)

    buttons = []
    # Create a 2x3 grid of buttons
    buttons = []
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="??", width=10, height=5)
            button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            button['command'] = lambda b=button: display_cross(b)
            buttons.append(button)



    # Configure the grid to resize with the buttons
    for i in range(3):
        window.grid_rowconfigure(i, weight=1)
    for j in range(3):
        window.grid_columnconfigure(j, weight=1)

    ttk.Label(window, text = "Turn :", 
		font = ("Times New Roman", 20)).grid(column = 1, 
		row = 3, padx = 10, pady = 25) 
    
    window.mainloop() 