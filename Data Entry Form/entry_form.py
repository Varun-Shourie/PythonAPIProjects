# Varun Shourie, CIS345, Tuesday/Thursday, 12:00PM-1:15Pm, PE13

from tkinter import *
from tkinter import ttk
from student_classes import Student, GradStudent


def save_student_click():
    """Once the user clicks to save student information, the function will construct either a student or grad
    student object appropriately. If the user is editing a student, the student will be inserted at the position
    of the original student in the listbox. If not, then the student is appended to the listbox and the roster
    of students in the program. Lastly, the program is refreshed to allow for further user input. """
    global edit_mode, student_listbox, student_roster, edit_index, student_type, thesis, fname, lname, major

    if student_type.get() == 2:
        temp = GradStudent(thesis.get(), fname.get(), lname.get(), major.get())
    else:
        temp = Student(fname.get(), lname.get(), major.get())

    if edit_mode:
        student_roster[edit_index] = temp
        student_listbox.delete(edit_index)
        student_listbox.insert(edit_index, temp)
        edit_mode = False
    else:
        student_roster.append(temp)
        student_listbox.insert(END, temp)

    clear_form()


def edit_student(event):
    """When a user double clicks a student in the textbox, edit mode is toggled on. Next, the currently selected
    item is acquired from the roster of students and is checked to see if the student is a grad student or not.
    If so, then the student type radio button is toggled towards "Graduate Student"; if not, then "Student".
    Lastly, all entry fields are repopulated with the original entry to make it convenient for editing. """
    global edit_mode, edit_index, student_type, fname, lname, thesis

    edit_mode = True
    edit_index = student_listbox.curselection()[0]

    edited_student = student_roster[edit_index]
    if isinstance(edited_student, GradStudent):
        student_type.set(2)
        thesis.set(edited_student.thesis)
    else:
        student_type.set(1)

    toggle_thesis()

    fname.set(edited_student.fname)
    lname.set(edited_student.lname)
    major.set(edited_student.major)


def toggle_thesis():
    """Depending on whether if a grad student or not, the thesis is disabled or enabled for user input. """
    global student_type, thesis_tbox
    if student_type.get() == 2:
        thesis_tbox.config(state=NORMAL)
    elif student_type.get() == 1:
        thesis_tbox.config(state=DISABLED)


def clear_form():
    """Clears all entry widgets and input opportunities for the user to their initial state."""
    fname.set('')
    lname.set('')
    major_combobox.current(0)
    thesis.set('')
    student_type.set(0)


# Objects used to access students and edit them throughout the course of the program.
student_roster = []
edit_mode = False
edit_index = 0

bg_color = 'light cyan'
frame_bg_color = 'cornsilk'

# Create a window object and style its color
window = Tk()
window.title('Student Entry Form')
window.geometry('410x500')
window['bg'] = bg_color

# Variables used to store the values provided by user entry in the GUI. 
student_type = IntVar()
fname = StringVar()
lname = StringVar()
thesis = StringVar()
major = StringVar()

# List of majors which user can choose from when inputting the student's major.
majors = ['ACC', 'BDA', 'CIS', 'MGT', 'SCM']

# Creates properly formatted label and radiobutton contained within a frame for delineation.
frame = Frame(window, bg=frame_bg_color, width=300, height=80, borderwidth=1, relief=SUNKEN)
frame.pack_propagate(0)
frame.grid(row=0, column=0, padx=50, pady=20, columnspan=2)

student_type_label = Label(frame, text='Student Type', bg=frame_bg_color)
student_type_label.pack(anchor=W)

student_radiobutton = Radiobutton(frame, bg=frame_bg_color, text='Student', variable=student_type, value=1,
                                  command=toggle_thesis)
student_radiobutton.pack(side=LEFT, padx=20)
gradstudent_radiobutton = Radiobutton(frame, bg=frame_bg_color, text='Graduate Student', variable=student_type, value=2,
                                      command=toggle_thesis)
gradstudent_radiobutton.pack(side=RIGHT, padx=30)

# Below, labels and textboxes/comboboxes for first name, last name, and major are created, inserted, and styled.
fname_label = Label(window, bg=bg_color, width=10, text='First Name: ', justify=RIGHT)
fname_label.grid(row=1, column=0, padx=20, pady=5, sticky=E)
fname_tbox = Entry(window, background='white', justify=LEFT, width=30, textvariable=fname)
fname_tbox.grid(row=1, column=1, sticky=W, pady=5)

lname_label = Label(window, bg=bg_color, width=10, justify=LEFT, text='Last Name: ')
lname_label.grid(row=2, column=0, padx=20, pady=5, sticky=E)
lname_tbox = Entry(window, background='white', justify=LEFT, width=30, textvariable=lname)
lname_tbox.grid(row=2, column=1, sticky=W, pady=5)

major_label = Label(window, bg=bg_color, justify=RIGHT, text='Major: ')
major_label.grid(row=3, column=0, padx=35, pady=5, sticky=E)
major_combobox = ttk.Combobox(window, width=27, values=majors, textvariable=major)
major_combobox.current(0)
major_combobox.grid(row=3, column=1, sticky=W, pady=5)

# Below, the label and textbox for a GRADUATE student's first name, last name, and major are created, inserted, styled.
thesis_label = Label(window, bg=bg_color, justify=RIGHT, text='Thesis: ')
thesis_label.grid(row=4, column=0, padx=35, pady=5, sticky=E)
thesis_tbox = Entry(window, background='white', justify=LEFT, width=30, textvariable=thesis)
thesis_tbox.grid(row=4, column=1, sticky=W, pady=5)

save_button = Button(window, text='Save Student', command=save_student_click)
save_button.grid(row=5, column=0, sticky=E, columnspan=2, padx=50, pady=5)

# Displays a text box which allows users to double click to edit to change student attributes.
instructions_label = Label(window, bg=bg_color, text='(Double-Click to Edit a Student)')
instructions_label.grid(row=6, column=0, sticky=W, columnspan=2, padx=50)
student_listbox = Listbox(window, width=50)
student_listbox.bind('<Double-Button-1>', edit_student)
student_listbox.grid(row=7, column=0, sticky=W, columnspan=2, padx=50)

window.mainloop()
