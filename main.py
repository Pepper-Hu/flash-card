import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 30, "italic", "bold")
WORD_FONT = ("Ariel", 50, "bold")
current_card = {}

# ---------------------------- CREATE NEW CARD ------------------------------- #
# TODO - Read the data from the french_words.csv file in the data folder: use pandas to access the CSV file and generate a data frame. To get all the words/translation rows out as a list of dictionaries
# TODO -  Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words_to_learn_dic = original_data.to_dict(orient="records")
else:
    words_to_learn_dic = data.to_dict(orient="records")


def create_new_card():
    global current_card, flip_timer

    # cancel existing timer
    window.after_cancel(flip_timer)

    current_card = random.choice(words_to_learn_dic)
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
# TODO -  Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.

# ---------------------------- tick/known ------------------------------- #
# TODO - When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word should be removed from the list of words that might come up
# TODO - The updated data should be saved to a new file called words_to_learn.csv
# TODO - The next time the program is run, it should check if there is a words_to_learn.csv file. If it exists, the program should use those words to put on the flashcards. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it should use the words in the french_words.csv
def tick_on_click():
    words_to_learn_dic.remove(current_card)
    print(len(words_to_learn_dic))

    data_updated = pd.DataFrame(words_to_learn_dic)
    # set index to False otherwise each write to words_to_learn will add a column of index number
    data_updated.to_csv("data/words_to_learn.csv", index=False)

    create_new_card()

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
# unknown - create another card
cross_img = PhotoImage(file="images/wrong.png")
cross_btn = tk.Button(image=cross_img,
                      highlightthickness=0,
                      borderwidth=0,
                      command=create_new_card)
cross_btn.grid(row=1, column=0)

# known - remove current card and create another card
tick_img = PhotoImage(file="images/right.png")
tick_btn = tk.Button(image=tick_img,
                     highlightthickness=0,
                     borderwidth=0,
                     command=tick_on_click)
tick_btn.grid(row=1, column=1)

create_new_card()

window.mainloop()