# Day 31 - Flash Card Capstone Project
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


def gen_word():
    global timer, current_word
    window.after_cancel(timer)
    current_word = random.choice(data_list)
    canvas.itemconfig(tagOrId=card_img, image=card_front_img)
    canvas.itemconfig(tagOrId=language_label, text="French", fill="black")
    canvas.itemconfig(tagOrId=word_label, text=current_word["French"], fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(word_label, text=current_word["English"], fill="white")
    canvas.itemconfig(language_label, text="English", fill="white")


def update_word_list():
    data_list.remove(current_word)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    gen_word()


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_list = data.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card, "")

canvas = Canvas(height=530, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 265, image=card_front_img)
language_label = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 265, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=gen_word)
wrong_btn.grid(row=1, column=0)
right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                   command=update_word_list)
right_btn.grid(row=1, column=1)

gen_word()

window.mainloop()
