# Varun Shourie, CIS345, Tuesday/Thursday 12:00PM-1:15PM, PE12

from tkinter import *
from tkinter import ttk
import random


def reset_game():
    """Initializes all data for the game resetting all variables. This includes the
    user's guess, feedback, the game's counter for user tries, the progress bar,
    and the submit button becoming clickable. """
    global answer, count, feedback, guess, counter, submit_button, progress
    guess.set("")
    answer = random.randint(1, 10)
    feedback.set("Enter guess 1")

    count = 0
    counter.set(f"Guess {count}/3")

    submit_button["state"] = NORMAL
    progress["value"] = 0


def check_answer():
    """Tests if the user guesses the right number. If so, this function tells the user they
    have won. If not, it will let them know if the guess was too high or too low.
    When the user runs out of tries, the submit button will be deactivated. """
    global answer, count, counter, progress, guess, submit_button, feedback

    # Note one guess made by the user.
    count += 1
    counter.set(f"Guess {count}/3")
    progress.step(100)

    # The possible exception that user input may not be a number is addressed here.
    try:
        g = int(guess.get())
    except ValueError:
        guess = 0
        g = 0

    # Provide feedback to the user if they won, lost, or have more tries left.
    if g == answer:
        feedback.set("You Win!!!!")
        submit_button.config(state=DISABLED)
    else:
        if g > answer:
            feedback.set(f"{g} is too high.")
        else:
            feedback.set(f"{g} is too low.")

        guess.set("")
        guess_textBox.focus()

        if count == 3:
            feedback.set(f"Answer was {answer}. You lose!")
            submit_button.config(state=DISABLED)


'''
# Creating icon using Pillow - all libraries and imports deleted.
original_img = Image.open("my_img.jpg")
new_img = original_img.resize((16, 16))
new_img.save("pic.ico")
'''

# Create window object and set its title, size, and icon in the top left corner.
window = Tk()
window.title("Guess Game")
window.geometry("250x195")
window.iconbitmap("pic.ico")

# Objects used to track the user's responses and tries, and then provide feedback.
answer = int()
count = int()
feedback = StringVar()
guess = StringVar()
counter = StringVar()

# Link the menu and window together
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Add dropdown list to menu called "File" with "Reset" and "Exit" as options.
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Reset", command=reset_game)
file_menu.add_command(label="Exit", command=window.quit)

# Creates and inserts all widgets such as labels, textbox, progress bar, and a submit button.
feedback_label = Label(window, textvariable=feedback, justify=LEFT)
feedback_label.pack(pady=5, anchor=CENTER)

guess_textBox = Entry(window, textvariable=guess, justify=RIGHT, width=23)
guess_textBox.pack(pady=5)

progress = ttk.Progressbar(window, orient="horizontal", maximum=301, mode="determinate", length=143)
progress.pack(pady=10)

counter_label = Label(window, textvariable=counter, justify=CENTER)
counter_label.pack()

submit_button = Button(text="Submit", command=check_answer, width=23)
submit_button.pack()

reset_game()
window.mainloop()
