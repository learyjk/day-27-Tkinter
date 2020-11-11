from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

calculated_label = Label(text="0")
calculated_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

def calculate_pressed():
    calculated_label["text"] = float(miles_entry.get()) * 1.609


calculate_button = Button(text="Calculate", command=calculate_pressed)
calculate_button.grid(column=1, row=2)

window.mainloop()