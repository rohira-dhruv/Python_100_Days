from tkinter import *


def add(*args):
    return sum(args)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(4, add=3, multiply=5)

print(add(1, 2, 4, 5))

window = Tk()
window.title("My first GUI program.")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "normal"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    input_text = input_box.get()
    my_label.config(text=input_text)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Input
input_box = Entry(width=30)
input_box.insert(END, string="Some text to begin with.")
input_box.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


def spinbox_used():
    print(spinbox.get())


# Spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# CheckButton


def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", command=checkbutton_used, variable=checked_state)
checkbutton.pack()

# RadioButton


def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# ListBox


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Cherry", "Orange", "Pear"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
