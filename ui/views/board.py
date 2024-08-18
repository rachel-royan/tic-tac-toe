import tkinter as tk 
from tkinter import ttk 

from src.GameFactory import GameFactory
from ui.views.gameover import win_gameover_view, nowin_gameover_view

window = None

def display_cross(b):
    b.config(text="X", state="disabled")

def display_circle(b):
    b.config(text="O", state="disabled")

def check_turn(new_game, b):
    turn, win = new_game.check_turn(b.grid_info()['row'], b.grid_info()['column'])
    if turn == "PX":
        display_cross(b)
    elif turn == "PO":
        display_circle(b)
    
    if win:
        window.destroy()
        win_gameover_view(new_game.turn)
    if new_game.check_board_full():
        window.destroy()
        nowin_gameover_view()


def play_game(player_mode, root):
    global window
    root.destroy()

    window = tk.Tk() 
    window.title('LET\'S PLAY!!!') 
    window.geometry('500x250')

    new_game = GameFactory._create_play(player_mode)

    buttons = []
    # Create a 2x3 grid of buttons
    buttons = []
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="??", width=10, height=5)
            button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            button['command'] = lambda b=button: check_turn(new_game, b)
            buttons.append(button)

    # Configure the grid to resize with the buttons
    for i in range(3):
        window.grid_rowconfigure(i, weight=1)
    for j in range(3):
        window.grid_columnconfigure(j, weight=1)

    ttk.Label(window, text = "Turn : "+new_game.turn, 
		font = ("Times New Roman", 20)).grid(column = 1, 
		row = 3, padx = 10, pady = 25) 
    
    window.mainloop() 