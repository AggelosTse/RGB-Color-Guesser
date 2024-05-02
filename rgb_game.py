from tkinter import (
    Tk,
    Label,
    Frame,
    Scale,
    HORIZONTAL,
    Button,
    ttk,
    DISABLED,
    NORMAL,
)
from random import randint
import utils

previous_color = None  


def generate_random_color():
    """Generates 3 random RGB values for the randomly picked color."""
    global random_red, random_green, random_blue, tries, bingo, previous_color
    tries = 0
    bingo = False
    previous_color = None
    random_red = randint(0, 255)    #gives a random value from 0 to 255
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    random_color = "#{:02x}{:02x}{:02x}".format(random_red, random_green, random_blue) #displays the color in GUI
    color_label_random.config(bg=random_color)
    result_label.config(text="")


def display_color():
    """Takes user's picked color and displays the results in GUI."""
    global tries, bingo, previous_color

    slider_red = slide_red.get()    #takes the value from slider
    slider_green = slide_green.get()
    slider_blue = slide_blue.get()
    user_color = "#{:02x}{:02x}{:02x}".format(slider_red, slider_green, slider_blue)

    # Check if the current color is the same as the previous color
    if user_color != previous_color:
        previous_color = user_color  # Update previous_color
        tries += 1  # Increment tries

    # Display user's color
    color_label_user.config(bg=user_color)

    # Calculate color distance
    distance = utils.colordistance(
        slider_red, slider_green, slider_blue, random_red, random_green, random_blue
    )
    distance_label.config(
        text="Color Distance: {:.2f}% Tries: {}".format(distance, tries) #displays a text in GUI
    )

    if distance < 10:
        bingo = True
        result_label.config(text="Bingo!")
        button_test.config(state=DISABLED)
        button_next.config(state=DISABLED)

    if tries == 5 and not bingo:
        result_label.config(text="You lost")
        button_test.config(state=DISABLED)
        button_next.config(state=DISABLED)


def enable_buttons():
    """Enables the GUI's buttons."""
    button_test.config(state=NORMAL)
    button_next.config(state=NORMAL)


tries = 0
bingo = False

window = Tk()
window.title("Basic Color Combinations")
window.geometry("600x400+200+200")  # Increased width to accommodate larger colors

color_label_random = Label(
    window, padx=200, pady=50, font=("Helvetica", 30)
)  # Increased padding and font size
color_label_random.pack()

#create first slider
frame1 = Frame(window)
frame1.pack()
slide_text1 = ttk.Label(frame1, text="R", font=("Helvetica", 18))  # Increased font size
slide_text1.pack(side="left")
slide_red = Scale(frame1, from_=0, to=255, orient=HORIZONTAL, length=400)
slide_red.pack()

#create second slider
frame2 = Frame(window)
frame2.pack()
slide_text2 = ttk.Label(frame2, text="G", font=("Helvetica", 18))  # Increased font size
slide_text2.pack(side="left")
slide_green = Scale(frame2, from_=0, to=255, orient=HORIZONTAL, length=400)
slide_green.pack()

#create third slider
frame3 = Frame(window)
frame3.pack()
slide_text3 = ttk.Label(frame3, text="B", font=("Helvetica", 18))  # Increased font size
slide_text3.pack(side="left")
slide_blue = Scale(frame3, from_=0, to=255, orient=HORIZONTAL, length=400)
slide_blue.pack()

color_label_user = Label(
    window, padx=200, pady=50, font=("Helvetica", 30)
)  # Increased padding and font size
color_label_user.pack()

distance_label = Label(
    window, text="Color Distance: ", font=("Helvetica", 20)
)  # Increased font size
distance_label.pack(pady=20)

result_label = Label(window, text="", font=("Helvetica", 20))  # Increased font size
result_label.pack()

#create the test button
button_test = Button(
    window,
    text="Test",
    bd=5,
    command=display_color,
    font=("Helvetica", 20),  # Increased font size
)
button_test.pack()

#create the Next button
button_next = Button(
    window,
    text="Next",
    bd=5,
    command=lambda: (generate_random_color(), enable_buttons()),
    font=("Helvetica", 20),  # Increased font size
)
button_next.pack()

generate_random_color()

window.mainloop()
