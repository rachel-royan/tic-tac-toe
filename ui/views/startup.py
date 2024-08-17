import tkinter as tk 
from tkinter import ttk 

from ui.views.board import play_game

# Creating tkinter window 
window = tk.Tk() 
window.title('TIC-TAC-TOE STARTUP') 
window.geometry('500x250')

# label text for title 
ttk.Label(window, text = "PLAY MODE SELECTION", 
		font = ("Times New Roman", 15)).grid(row = 0, column = 1, padx = 10, pady = 25) 

# label 
ttk.Label(window, text = "Select the Mode :", 
		font = ("Times New Roman", 10)).grid(column = 0, 
		row = 5, padx = 10, pady = 25) 

# Combobox creation 
n = tk.StringVar() 
playerchosen = ttk.Combobox(window, width = 27, textvariable = n) 

# Adding combobox drop down list 
playerchosen['values'] = ('Single-Player', 
						'Multi-Player', 
						) 

playerchosen.grid(column = 1, row = 5)

# Creating a button with specified options
button = tk.Button(window, 
                   text="Start Game!", 
                   command=lambda : play_game(n.get(), window),
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
button.grid(column = 1, row = 10)

window.mainloop() 
