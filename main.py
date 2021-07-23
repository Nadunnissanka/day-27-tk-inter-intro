from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=30)


# function convert
def convert_miles_to_km():
    miles_need_to_convert = miles_input.get()
    one_mile_equal_to_km = 1.60934
    total_km = round(one_mile_equal_to_km * float(miles_need_to_convert))
    converted_label.config(text=f"{total_km}")


# layout grid
# Miles Entry
miles_input = Entry(width=10)
miles_input.grid(row=1, column=1)

# miles label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=1, column=2)

# equal label
equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(row=2, column=0)

# converted value
converted_label = Label(text="0", font=("Arial", 12))
converted_label.grid(row=2, column=1)

# converted type label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(row=2, column=2)

# convert button
convert_button = Button(window, text="Convert", command=convert_miles_to_km)
convert_button.grid(row=3, column=1)

window.mainloop()
