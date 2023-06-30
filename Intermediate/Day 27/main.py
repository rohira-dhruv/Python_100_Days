from tkinter import *


def calculate():
    miles = float(input_text.get())
    kms = round(miles * 1.609)
    result_label.config(text=f"{kms}")


window = Tk()
window.title("My first GUI program.")
window.config(padx=20, pady=20)

input_text = Entry(width=10)
input_text.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)
equals_label.config(padx=10, pady=10)

result_label = Label()
result_label.grid(row=1, column=1)
result_label.config(padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=5, pady=5)

window.mainloop()
