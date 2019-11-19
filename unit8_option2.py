# created by Allison Dixon
# last modified November 19, 2019
# unit 8 option 2 project- calculator

from tkinter import *

root = Tk()

title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)

result_bar = Entry(root)
result_bar.grid(row=2, column=1, columnspan=4)

clear_button = Button(root, text="Clear", width=5, font="Helvetica 14")
clear_button.grid(row=3, column=1, sticky="W")

negative_button = Button(root, text="+/-", width=5, font="Helvetica 14")
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=5, font="Helvetica 14")
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=5, font="Helvetica 14")
divide_button.grid(row=3, column=4, sticky="E")

seven_button = Button(root, text="7", width=5, font="Helvetica 14")
seven_button.grid(row=4, column=1, sticky="W")

eight_button = Button(root, text="8", width=5, font="Helvetica 14")
eight_button.grid(row=4, column=2)

nine_button = Button(root, text="9", width=5, font="Helvetica 14")
nine_button.grid(row=4, column=3)

multiply_button = Button(root, text="*", width=5, font="Helvetica 14")
multiply_button.grid(row=4, column=4, sticky="E")

four_button = Button(root, text="4", width=5, font="Helvetica 14")
four_button.grid(row=5, column=1, sticky="W")

five_button = Button(root, text="5", width=5, font="Helvetica 14")
five_button.grid(row=5, column=2)

six_button = Button(root, text="6", width=5, font="Helvetica 14")
six_button.grid(row=5, column=3)

subtract_button = Button(root, text="-", width=5, font="Helvetica 14")
subtract_button.grid(row=5, column=4, sticky="E")

one_button = Button(root, text="1", width=5, font="Helvetica 14")
one_button.grid(row=3, column=1, sticky="W")

negative_button = Button(root, text="+/-", width=5, font="Helvetica 14")
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=5, font="Helvetica 14")
percent_button.grid(row=3, column=3)

division_button = Button(root, text="/", width=5, font="Helvetica 14")
division_button.grid(row=3, column=4, sticky="E")

root.mainloop()