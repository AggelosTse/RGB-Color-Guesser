from tkinter import *
from tkinter import ttk
from random import randint

def generate_random_color():
    # Generate random colors
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    
    # Configure color_label_random with the random color
    random_color = "#{:02x}{:02x}{:02x}".format(random_red, random_green, random_blue)
    color_label_random.config(bg=random_color)

def display_color():
    # Retrieve slider values when the button is clicked
    slider_red = slide_red.get()
    slider_green = slide_green.get()
    slider_blue = slide_blue.get()
    
    # Configure color_label_user with the selected color
    user_color = "#{:02x}{:02x}{:02x}".format(slider_red, slider_green, slider_blue)
    color_label_user.config(bg=user_color)

# Window initialization
window = Tk()
window.title("Basic Color Combinations")
window.geometry("1080x800+200+200")

# Label for displaying random color (left side)
color_label_random = Label(window, padx=273, pady=1)
color_label_random.pack(side=LEFT, fill=Y)

# Generate the initial random color
generate_random_color()

# Slider creation
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

# Label for displaying user-selected color (right side)
color_label_user = Label(window, padx=273, pady=1)
color_label_user.pack(side=RIGHT, fill=Y)

# Button for testing
button_test = Button(window, text='Test', bd=5, command=display_color)
button_test.pack(side=TOP)

# Button for generating a new random color
button_next = Button(window, text='Next', bd=5, command=generate_random_color)
button_next.pack(side=TOP)

window.mainloop()
