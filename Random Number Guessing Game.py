
# importing packages
from random import random
import string
import tkinter as tk
import random
from sklearn.utils import shuffle
import customtkinter as ctk
from tkinter import *
from tkinter import ttk


# setting the initial number that the computer chooses
computer_number = random.randint(1,10)
# set the counter that counts the guesses
counter = 1


def guess():
    '''this function runs and checks whether guess is correct'''
    # sets global variables so the counter can be increased and the guess is stored globally
    global counter 
    global user_guess
    # gets the users input guess
    user_guess = int(userinput.get())
    # checks if answer is correct
    if user_guess == computer_number:
        # if it is and had less than 3 guesses, runs correct, otherwise game over
        if counter <= 3:
            load_correct()
        else:
            game_over()
    else:
        # if incorrect and less than 3 guesses, increases counter and runs incorrect screen. 
        #otherwise game over
        if counter < 3:
            counter +=1
            load_incorrect()
        else:
            game_over()



def load_main():
    ''' This function loads the main screen'''
    # sets global variable so it can be used in guess function
    global userinput
    #clears other frames and raises main frame
    clear_widgets(correct)
    clear_widgets(incorrect)
    clear_widgets(gameover)
    main.tkraise()
    # adds a label telling to guess
    tk.Label(main, text="Guess A Number From 1 to 10",bg=background,
        fg="white",
        font=("Rockwell", 50)
        ).place(rely=0.4,relx=0.5,anchor=CENTER)
    # user entry box
    userinput = ctk.CTkEntry(
    main)
    userinput.place(rely=0.5,relx=0.5, anchor=CENTER)
    # guess button which runs guess function
    ctk.CTkButton(
    main,
    text="GUESS",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=lambda:guess()
        ).place(rely=0.7,relx=0.5, anchor=CENTER)



def load_correct():
    '''this function loads teh screen that shows with a correct answer'''
    # clears widgets and raise correct frame
    clear_widgets(main)
    clear_widgets(incorrect)
    clear_widgets(gameover)
    correct.tkraise()
    # label telling correct answer
    tk.Label(correct, text="That's Correct!",bg=background,
        fg="white",
        font=("Rockwell", 50)
        ).pack(padx=20,pady=20)
    # asks user to play again. This then runs play again function
    ctk.CTkButton(
    correct,
    text="PLAY AGAIN?",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=lambda: play_again()
        ).pack(padx=20,pady=20)
    # gives option to quit
    ctk.CTkButton(
    correct,
    text="EXIT",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=window.destroy
        ).pack(padx=20,pady=20)


def load_incorrect():
    '''this function loads the screen that shows when the guess is incorrect'''
    # clears the widgets and raises incorrect screen
    clear_widgets(main)
    clear_widgets(correct)
    clear_widgets(gameover)
    incorrect.tkraise()
    # label letting user know they were wrong
    tk.Label(incorrect, text="Sorry, That's Incorrect. Guess Again!",bg=background,
        fg="white",
        font=("Rockwell", 50)
        ).pack(padx=20,pady=20)
    
    # button to guess again which loads main frame
    ctk.CTkButton(
    incorrect,
    text="GUESS AGAIN",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=lambda: load_main()
        ).pack(padx=20,pady=20)
    
    # checks if the guess needs to be higher or lower and adds a label telling user
    if computer_number < user_guess:
            tk.Label(incorrect, text="Guess Lower",bg=background,
        fg="white",
        font=("Rockwell", 20)
        ).pack(padx=20,pady=20)
    else:
        tk.Label(incorrect, text="Guess Higher",bg=background,
        fg="white",
        font=("Rockwell", 20)
        ).pack(padx=20,pady=20)
    
    # label displaying guesses remaining
    tk.Label(incorrect, text=f"{4-counter} Guesses Remaining",bg=background,
        fg="white",
        font=("Rockwell", 20)
        ).pack(padx=20,pady=20)



def play_again():
    '''this function runs when a new game is requested'''
    global computer_number
    global counter
    # generates a new computer number
    computer_number = random.randint(1,10)
    #resets counter
    counter = 1
    # loads main frame
    load_main()



def game_over():
    '''this function runs when the user fails to guess the number'''
    # clear widgets
    clear_widgets(correct)
    clear_widgets(incorrect)
    clear_widgets(main)
    gameover.tkraise()
    
    # label displaying what the actual number was
    tk.Label(gameover, text=f"Too Many Guesses. Game Over. The Number Was {computer_number}",bg=background,
        fg="white",
        font=("Rockwell", 30)
        ).pack()
    
    # asks user to play again. runs play again function
    ctk.CTkButton(
    gameover,
    text="PLAY AGAIN?",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=lambda: play_again()
        ).pack()
    
    # exit button which closer the UI
    ctk.CTkButton(
    gameover,
    text="EXIT",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=window.destroy
        ).pack(padx=20,pady=20)



def clear_widgets(frame):
    'this function destroys all the widgets on the specified frame'
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()



# this initialises the UI settings
background='#323050'
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')

# this initialises tkinter
window = ctk.CTk()
window.title("Password Generator")
window.geometry("1200x500+10+10")

#this defines the 4 frames
main = tk.Frame(window, width=2000, height=1500, bg=background)
incorrect = tk.Frame(window, bg=background)
correct = tk.Frame(window, bg=background)
gameover = tk.Frame(window, bg=background)

# place frame widgets in window
for frame in (main, incorrect, correct, gameover):
    frame.place(rely=0.5,relx=0.5, anchor = CENTER)

# load the main frame
load_main()

#runs the window
window.mainloop()

