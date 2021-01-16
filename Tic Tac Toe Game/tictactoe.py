# Varun Shourie, CIS345, Tuesday/Thursday, 12:00PM-1:15PM, A7

from tkinter import *
from tkinter import font
from tkinter import messagebox


def add_x_or_o(button_number):
    """If the button number is between 0 and 8, add an X if it is Player 1's turn and an O if it is Player 2's turn.
    Upon each click, the button is also disabled to prevent further clicks of the same button. If Player 1 or
    Player 2 either have winning combinations, then the game declares a winner using a message. If not, the game allows
    the players to only engage in 9 turns since there are only 9 boxes, then declaring a draw ("Cats Game")."""
    global buttons, turn_count, player_selections

    # Checks the button number to ensure the correct number was provided from external code in the program.
    if button_number in range(0, len(buttons)):
        button = buttons[button_number]

        if turn_count % 2 == 0:
            button.config(text='X', state=DISABLED)
            player_selections[0].append(button_number)
        else:
            button.config(text='O', state=DISABLED)
            player_selections[1].append(button_number)

        turn_count += 1
        player_number = check_for_winner()

        if player_number in (1, 2):
            messagebox.showinfo(title='Winner', message=f'Player {player_number} is the winner!')
            clear_board()
        elif turn_count == 9:
            messagebox.showinfo(title='Draw', message='Cats Game')
            clear_board()


def check_for_winner():
    """To provide some context, box 0 starts at the top left corner. It is the box at row 0, column 0. Box 1 is at
    row 0, column 1. Box 2 is at row 0, column 2. Similarly, box 3 is at row 1, column 0. The pattern follows for
    the rest of the buttons...

    If either player gets full Xs or Os in an entire row, column, or diagonal with the correct box numbers, the
    player's number is returned as the winner of the Tic Tac Toe game. If either player has not won yet, a -1 will
    be returned to signify this fact when checking for a winner. """
    global player_selections
    solutions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2))
    box_count = 0

    for solution in solutions:
        for player_number in range(0, 2):
            for selection in player_selections[player_number]:
                if selection in solution:
                    box_count += 1

                # If a player has won, return the player's incremented number since it's meaningful to the user.
                if box_count == 3:
                    return player_number + 1

            box_count = 0

    return -1


def clear_board():
    """Resets the board to its initial state for replaying the game, such as resetting the count of turns taken
    by the players, enabling all buttons, and resetting the list of each player's selections."""
    global turn_count, buttons, player_selections

    turn_count = 0
    for button in buttons:
        button.config(text='', state=NORMAL)
    player_selections = [list(), list()]


window = Tk()
window.title('Tic Tac Toe')
window.geometry('413x360')

# Tracks the number of turns performed by users and the buttons clicked in the program by the two users.
turn_count = 0
buttons = []
player_selections = [list(), list()]

# Customize the font and buttons' appearance like the deliverable screenshots on instructions.
app_font = font.Font(family='Arial', size=20)
btn_width = 8
btn_height = 3
fg_color = 'gray'

# The button's assigned index in the buttons list is passed using an anonymous function.
# Below, the first row of buttons are initialized, styled, and numbered to be tracked in the future.
first_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(0))
first_button.grid(row=0, column=0)
buttons.append(first_button)

second_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(1))
second_button.grid(row=0, column=1)
buttons.append(second_button)

third_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(2))
third_button.grid(row=0, column=2)
buttons.append(third_button)

# Below, the second row of buttons are initialized, styled, and numbered to be tracked in the future.
fourth_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(3))
fourth_button.grid(row=1, column=0)
buttons.append(fourth_button)

fifth_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(4))
fifth_button.grid(row=1, column=1)
buttons.append(fifth_button)

sixth_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(5))
sixth_button.grid(row=1, column=2)
buttons.append(sixth_button)

# Below, the third row of buttons are initialized, styled, and numbered to be tracked in the future.
seventh_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(6))
seventh_button.grid(row=2, column=0)
buttons.append(seventh_button)

eighth_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(7))
eighth_button.grid(row=2, column=1)
buttons.append(eighth_button)

ninth_button = Button(fg=fg_color, width=btn_width, height=btn_height, font=app_font, command=lambda: add_x_or_o(8))
ninth_button.grid(row=2, column=2)
buttons.append(ninth_button)

window.mainloop()
