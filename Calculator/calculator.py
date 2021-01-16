# Varun Shourie, CIS345, Tuesday/Thursday, 12:00PM-1:15PM, A6
from tkinter import *
import math


def add_number(button):
    """When the user presses a numerical button, this function will check if the button pressed is a number or decimal
     point. If a decimal, the function will check to see another decimal is not present in the number before adding
     another decimal. If a number, the function will check to see if the output so far is either a zero, negative zero,
     or non-zero value and append the output accordingly. """
    global output, calculation_done_recently
    # Objects used to validate the expression and check for decimals and characteristics of output.
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    add_decimal = True
    operator_present = False
    index = -1

    if calculation_done_recently:
        output.set("0")
        calculation_done_recently = False

    # Scope of this variable is altered to allow for validation above.
    current_output = output.get()

    if button == ".":
        while index >= -1 * len(current_output) and add_decimal:
            # If a decimal is present before an operator is found, the number in question already has a decimal.
            if current_output[index] in operators:
                operator_present = True
            elif current_output[index] == button and not operator_present:
                add_decimal = False

            index -= 1

        if add_decimal:
            output.set(f"{current_output}.")
    elif button in numbers:
        if current_output != "0" and current_output != "-0":
            output.set(f"{current_output}{button}")
        elif current_output == "-0":
            output.set(f"-{button}")
        else:
            output.set(f"{button}")


def append_operator(button):
    """When the user presses an operator, this function will perform validation on the mathematical expression
    to see if (1) the button provided is an operator, and (2) an operator is already not present in the math expression
    at the point of insertion. """
    global output, calculation_done_recently, operators
    current_output = output.get()
    add_operator = True

    if calculation_done_recently:
        calculation_done_recently = False

    if button in operators:
        # If there is already an operator separated by a space before the current position in output, or an operator
        # at the current position in input, do not add an operator whatsoever.
        if (len(current_output) >= 2 and current_output[-2] in operators and current_output[-1] == " "
                or current_output[-1] in operators):
            add_operator = False

        if add_operator:
            output.set(f"{current_output} {button} ")


def perform_calculation(button):
    """When the user presses the equals button, the function will evaluate the math expression and round results
    to 10 decimal places to offset calculation error. If the user presses the sqrt button, the calculator will
    evaluate the existing formula and then take the square root of that answer. If the calculation result can be a whole
    number, then it'll be rounded down. Furthermore, this function prevents program crashing from bad user input."""
    global output, calculation_done_recently
    current_output = output.get()

    if button == "sqrt" or button == "=":
        try:
            # Rounding is necessary to overcome error from floating point variables.
            calculation = round(eval(current_output), 10)
            if button == "sqrt":
                calculation = math.sqrt(calculation)

            if calculation == int(calculation):
                calculation = int(calculation)

            output.set(f"{calculation}")
        # Handles when the user divides by zero, enters an invalid expression, or attempts to sqrt a negative value.
        except (ZeroDivisionError, SyntaxError, ValueError):
            output.set("Error")
        finally:
            calculation_done_recently = True


def perform_utility(button):
    """When the user clicks a utility, the function will alter the mathematical expression as stated below:
    Pressing clear resets the expression to zero.
    Pressing plus/minus toggles the most recently entered number between positive and negative signs, even
    when the last input entered was an operator.
    Pressing backspace deletes one character at a time, until the character count reaches 2. If there is a negative
    number, removing the second to last character makes output a zero. If not, characters will be removed as normal.
    """
    global output, calculation_done_recently, operators
    current_output = output.get()

    if calculation_done_recently:
        calculation_done_recently = False

    if button == "AC":
        output.set("0")
    elif button == "+/-":
        # Objects used to modularize the math expression into digestible pieces of operators and numbers.
        expression_parts = list(current_output.split(" "))
        number_not_found = True
        toggled_string = str()
        index = -1

        # Toggles the most recently found number in the expression to positive or negative depending on its sign.
        while number_not_found and index >= -1 * len(expression_parts):
            if expression_parts[index] not in operators and not expression_parts[index] == "":
                number_not_found = False

                if "-" not in expression_parts[index]:
                    expression_parts[index] = f"-{expression_parts[index]}"
                else:
                    expression_parts[index] = f"{expression_parts[index][1:]}"

            index -= 1

        # Rewrites the entire math expression to include the toggled value.
        for part in expression_parts:
            if part in operators:
                toggled_string += f" {part} "
            else:
                toggled_string += f"{part}"

        output.set(toggled_string)
    elif button == "-->":
        # The output also needs to be checked if there's only a negative single digit number to backspace correctly.
        if len(current_output) == 1 or len(current_output) == 2 and "-" in current_output:
            output.set("0")
        else:
            output.set(f"{current_output[:-1]}")


# Configures the window object for later usage.
window = Tk()
window.config(bg="dim gray")
window.geometry("245x330")
window.title("Calculator")

# Objects used to ensure correct functionality and display of numbers throughout the program, including functions.
calculation_done_recently = False
operators = ("*", "/", "+", "-")
output = StringVar()
output.set("0")

# Frame which holds the contents of the calculator and helps simulate design of a calculator as shown in requirements.
calculator_frame = Frame(window, background="dark blue", width=40)
calculator_frame.pack(pady=5)

# Text box object for the calculator which shows program output.
output_entry = Entry(calculator_frame, width=34, justify=RIGHT, textvariable=output)
output_entry.pack(pady=10, ipady=10)
output_entry.bind("<KeyPress>", lambda x: "break")

# Label with all buttons created inside to delineate sections for input/output in the calculator.
button_section_label = Label(calculator_frame, background="dark blue")
button_section_label.pack(padx=5)

# First row of buttons are created below in the calculator.
clear_button = Button(button_section_label, bg="red", text="AC", fg="white", width=5, height=2,
                      command=lambda: perform_utility("AC"))
clear_button.grid(row=1, column=0, padx=5)

backspace_button = Button(button_section_label, bg="dark gray", text="-->", fg="white", width=5, height=2,
                          command=lambda: perform_utility("-->"))
backspace_button.grid(row=1, column=1, padx=5, pady=5)

plus_minus_button = Button(button_section_label, bg="dark gray", text="+/-", fg="white", width=5, height=2,
                           command=lambda: perform_utility("+/-"))
plus_minus_button.grid(row=1, column=2, padx=5, pady=5)

sqrt_button = Button(button_section_label, bg="dark gray", text="sqrt", fg="white", width=5, height=2,
                     command=lambda: perform_calculation("sqrt"))
sqrt_button.grid(row=1, column=3, padx=5, pady=5)

# Second row of buttons are inserted into the calculator.
seven_button = Button(button_section_label, bg="black", text="7", fg="white", width=5, height=2,
                      command=lambda: add_number("7"))
seven_button.grid(row=2, column=0, pady=5)

eight_button = Button(button_section_label, bg="black", text="8", fg="white", width=5, height=2,
                      command=lambda: add_number("8"))
eight_button.grid(row=2, column=1, pady=5)

nine_button = Button(button_section_label, bg="black", text="9", fg="white", width=5, height=2,
                     command=lambda: add_number("9"))
nine_button.grid(row=2, column=2, pady=5)

divide_button = Button(button_section_label, bg="gray", text="/", fg="white", width=5, height=2,
                       command=lambda: append_operator("/"))
divide_button.grid(row=2, column=3, pady=5)

# Third row of buttons are inserted into the calculator.
four_button = Button(button_section_label, bg="black", text="4", fg="white", width=5, height=2,
                     command=lambda: add_number("4"))
four_button.grid(row=3, column=0, pady=5)

five_button = Button(button_section_label, bg="black", text="5", fg="white", width=5, height=2,
                     command=lambda: add_number("5"))
five_button.grid(row=3, column=1, pady=5)

six_button = Button(button_section_label, bg="black", text="6", fg="white", width=5, height=2,
                    command=lambda: add_number("6"))
six_button.grid(row=3, column=2, pady=5)

multiplication_button = Button(button_section_label, bg="gray", text="*", fg="white", width=5, height=2,
                               command=lambda: append_operator("*"))
multiplication_button.grid(row=3, column=3, pady=5)

# Fourth row of buttons are inserted into the calculator.
one_button = Button(button_section_label, bg="black", text="1", fg="white", width=5, height=2,
                    command=lambda: add_number("1"))
one_button.grid(row=4, column=0, pady=5)

two_button = Button(button_section_label, bg="black", text="2", fg="white", width=5, height=2,
                    command=lambda: add_number("2"))
two_button.grid(row=4, column=1, pady=5)

three_button = Button(button_section_label, bg="black", text="3", fg="white", width=5, height=2,
                      command=lambda: add_number("3"))
three_button.grid(row=4, column=2, pady=5)

subtract_button = Button(button_section_label, bg="gray", text="-", fg="white", width=5, height=2,
                         command=lambda: append_operator("-"))
subtract_button.grid(row=4, column=3, pady=5)

# Fifth and final row of buttons are inserted into the calculator.
zero_button = Button(button_section_label, bg="black", text="0", fg="white", width=5, height=2,
                     command=lambda: add_number("0"))
zero_button.grid(row=5, column=0, pady=5)

decimal_button = Button(button_section_label, bg="black", text=".", fg="white", width=5, height=2,
                        command=lambda: add_number("."))
decimal_button.grid(row=5, column=1, pady=5)

equals_button = Button(button_section_label, bg="green", text="=", fg="white", width=5, height=2,
                       command=lambda: perform_calculation("="))
equals_button.grid(row=5, column=2, pady=5)

add_button = Button(button_section_label, bg="gray", text="+", fg="white", width=5, height=2,
                    command=lambda: append_operator("+"))
add_button.grid(row=5, column=3, pady=5)

window.mainloop()
