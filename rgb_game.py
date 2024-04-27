from tkinter import *
from tkinter import ttk
from random import randint
import utils

tries = 0
bingo = False

window = Tk()
window.title("Basic Color Combinations")
window.geometry("400x300+200+200")

color_label_random = Label(window, padx=100, pady=20)
color_label_random.pack()

frame1 = Frame(window)
frame1.pack()
slide_text1 = ttk.Label(frame1, text="R")
slide_text1.pack(side=LEFT)
slide_red = Scale(frame1, from_=0, to=255, orient=HORIZONTAL)
slide_red.pack()

frame2 = Frame(window)
frame2.pack()
slide_text2 = ttk.Label(frame2, text="G")
slide_text2.pack(side=LEFT)
slide_green = Scale(frame2, from_=0, to=255, orient=HORIZONTAL)
slide_green.pack()

frame3 = Frame(window)
frame3.pack()
slide_text3 = ttk.Label(frame3, text="B")
slide_text3.pack(side=LEFT)
slide_blue = Scale(frame3, from_=0, to=255, orient=HORIZONTAL)
slide_blue.pack()

color_label_user = Label(window, padx=100, pady=20)
color_label_user.pack()

distance_label = Label(window, text="Color Distance: ")
distance_label.pack(pady=10)

result_label = Label(window, text="")
result_label.pack()

def generate_random_color():
    global random_red, random_green, random_blue, tries, bingo
    tries = 0
    bingo = False
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    random_color = "#{:02x}{:02x}{:02x}".format(random_red, random_green, random_blue)
    color_label_random.config(bg=random_color)
    result_label.config(text="")

def display_color():
    global tries, bingo
    if tries < 5 and not bingo:
        slider_red = slide_red.get()
        slider_green = slide_green.get()
        slider_blue = slide_blue.get()
        user_color = "#{:02x}{:02x}{:02x}".format(slider_red, slider_green, slider_blue)
        color_label_user.config(bg=user_color)
        distance = utils.colordistance(slider_red, slider_green, slider_blue, random_red, random_green, random_blue)
        distance_label.config(text="Color Distance: {:.2f}% Tries: {}".format(distance, tries))
        tries += 1

        if distance < 10:
            bingo = True
            result_label.config(text="Bingo!")
            # Disable Test and Next buttons if bingo is achieved
            button_test.config(state=DISABLED)
            button_next.config(state=DISABLED)
        
        if tries == 5 and not bingo:
            result_label.config(text="You lost")
            # Disable Test and Next buttons if no bingo is achieved after 5 tries
            button_test.config(state=DISABLED)
            button_next.config(state=DISABLED)

def enable_buttons():
    # Enable Test and Next buttons
    button_test.config(state=NORMAL)
    button_next.config(state=NORMAL)

button_test = Button(window, text='Test', bd=5, command=display_color)
button_test.pack()

button_next = Button(window, text='Next', bd=5, command=lambda: (generate_random_color(), enable_buttons()))
button_next.pack()

generate_random_color()

window.mainloop() 
