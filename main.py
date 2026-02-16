import tkinter as tk
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 30, "italic", "bold")
WORD_FONT = ("Ariel", 50, "bold")

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

# canvas
# canvas size = img size
canvas = tk.Canvas(bg=BACKGROUND_COLOR,width=800, height=526, highlightthickness=0)

# TODO - create card
card_front_img = PhotoImage(file="images/card_front.png")
# create_img location = middle of the canvas (half width, half height)
canvas.create_image(400, 263, image=card_front_img)

# TODO - create text
canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text=f"word", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

# btn
cross_img = PhotoImage(file="images/wrong.png")
cross_btn = tk.Button(image=cross_img,
                      highlightthickness=0,
                      borderwidth=0,
                      command=cross_on_click)
cross_btn.grid(row=1, column=0)

tick_img = PhotoImage(file="images/right.png")
tick_btn = tk.Button(image=tick_img,
                     highlightthickness=0,
                     borderwidth=0,
                     command=tick_on_click)
tick_btn.grid(row=1, column=1)

window.mainloop()