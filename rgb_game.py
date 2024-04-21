from tkinter import *
from tkinter import ttk

window = Tk()   #creates the window

window.geometry("1080x800+200+200")     #changes window's scale

frame1 = Frame(window)
frame1.pack()
slidetext1 = ttk.Label(frame1, text="R")
slidetext1.pack(side = LEFT)
slide1 = Scale(frame1, from_=0, to=255, orient = HORIZONTAL)
slide1.pack()

frame2 = Frame(window)
frame2.pack()
slidetext2 = ttk.Label(frame2, text="G")
slidetext2.pack(side = LEFT)
slide2 = Scale(frame2, from_=0, to=255, orient = HORIZONTAL)
slide2.pack()

frame3 = Frame(window)
frame3.pack()
slidetext3 = ttk.Label(frame3, text="B")
slidetext3.pack(side = LEFT)
slide3 = Scale(frame3, from_=0, to=255, orient = HORIZONTAL)
slide3.pack()

mainloop()  #opens the window

