import tkinter as tk 
from tkinter import ttk 

window = None

def play_again():
    global window
    window.destroy()

    from ui.views.startup import start_game
    start_game()

def close_game():
    global window
    window.destroy()

def win_gameover_view(win_player):
    global window
    # Creating tkinter window 
    window = tk.Tk() 
    window.title('TIC-TAC-TOE EXIT') 
    window.geometry('500x250')

    # label text for title 
    ttk.Label(window, text = "GAME OVER!!", 
            font = ("Times New Roman", 15)).grid(row = 0, column = 2, padx = 10, pady = 25) 

    # label 
    ttk.Label(window, text = "CONGRATULATIONS "+win_player +" !!", 
            font = ("Times New Roman", 15)).grid(column = 2, 
            row = 5, padx = 10, pady = 25) 

    # Creating a button with specified options
    button = tk.Button(window, 
                    text="Play Again!!", 
                    command=lambda : play_again(),
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

    button1 = tk.Button(window, 
                    text="Close", 
                    command=lambda : close_game(),
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
    button1.grid(column = 2, row = 10)

    window.mainloop() 

def nowin_gameover_view():
    global window
    # Creating tkinter window 
    window = tk.Tk() 
    window.title('TIC-TAC-TOE EXIT') 
    window.geometry('500x250')

    # label text for title 
    ttk.Label(window, text="GAME OVER!!", 
              font=("Times New Roman", 15)).grid(row=0, column=0, columnspan=4, padx=10, pady=25) 

    # label 
    ttk.Label(window, text="OOPS NO WINNERS..", 
              font=("Times New Roman", 15)).grid(column=0, row=5, columnspan=4, padx=10, pady=25) 

    # Creating a button with specified options
    button = tk.Button(window, 
                       text="Play Again!!", 
                       command=lambda: play_again(),
                       activebackground="blue", 
                       activeforeground="white",
                       anchor="center",
                       bd=3,
                       bg="lightgray",
                       cursor="hand2",
                       fg="black",
                       font=("Arial", 12),
                       height=1,
                       padx=10,
                       pady=5,
                       width=15)
    button.grid(column=1, row=10, padx=10, pady=5)

    button1 = tk.Button(window, 
                        text="Close", 
                        command=lambda: close_game(),
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        padx=10,
                        pady=5,
                        width=15)
    button1.grid(column=2, row=10, padx=10, pady=5)

    window.mainloop() 

nowin_gameover_view()