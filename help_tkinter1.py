from tkinter import *

window = Tk()
# write code below
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# adding padding
window.config(padx=20, pady=20)

# create a label in Tkinter
my_label = Label(text="Welcome to Tkinter", font=("Arial", 24, "bold "))
my_label.grid(row=0, column=0)


def button_clicked():
    my_label.config(text=f"Welcome {my_input.get()}!")


# create a button in Tkinter
button = Button(text="Click Me!", command=button_clicked)
button.grid(row=1, column=1)

# create a button in Tkinter
button_sec = Button(text="Click Me!", command=button_clicked)
button_sec.grid(row=0, column=3)

# input field in Tkinter
my_input = Entry(width=10)
my_input.grid(row=3, column=4)

# write code above
window.mainloop()
