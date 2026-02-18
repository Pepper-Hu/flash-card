import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 30, "italic", "bold")
WORD_FONT = ("Ariel", 50, "bold")

# ---------------------------- CREATE NEW CARD ------------------------------- #
# TODO - Read the data from the french_words.csv file in the data folder: use pandas to access the CSV file and generate a data frame. To get all the words/translation rows out as a list of dictionaries
# TODO -  Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.

data = pd.read_csv("data/french_words.csv")
word_to_learn_dic = data.to_dict(orient="records")
current_card = {}

def create_new_card():
    global current_card, flip_timer

    # cancel existing timer
    window.after_cancel(flip_timer)

    current_card = random.choice(word_to_learn_dic)
    print(current_card["French"])

    # set words
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # set background
    canvas.itemconfig(card_background, image=card_front_img)

    # set new timer
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
# TODO - After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
# TODO - The card image should change to the card_back.png and the text colour should change to white. The title of the card should change to "English" from "French".
def flip_card():
    # change words
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

    # change background
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- cross/unknown ------------------------------- #
def cross_on_click():
    pass

# ---------------------------- tick/known ------------------------------- #
def tick_on_click():
    pass

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# canvas
# canvas size = img size
canvas = tk.Canvas(bg=BACKGROUND_COLOR,width=800, height=526, highlightthickness=0)

# TODO - create card
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# create_img location = middle of the canvas (half width, half height)
card_background = canvas.create_image(400, 263, image=card_front_img)

# TODO - create text
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text=f"word", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

# btn
cross_img = PhotoImage(file="images/wrong.png")
cross_btn = tk.Button(image=cross_img,
                      highlightthickness=0,
                      borderwidth=0,
                      command=create_new_card)
cross_btn.grid(row=1, column=0)

tick_img = PhotoImage(file="images/right.png")
tick_btn = tk.Button(image=tick_img,
                     highlightthickness=0,
                     borderwidth=0,
                     command=create_new_card)
tick_btn.grid(row=1, column=1)

create_new_card()

window.mainloop()