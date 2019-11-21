# created by Allison Dixon
# last modified November 20, 2019
# unit 8 option 2 project- a calculator

from tkinter import *

root = Tk()
root.configure(background="powder blue")


def add_zero():
    new_result = display_result.get()
    new_result += "0"
    display_result.set(new_result)


def add_one():
    new_result = display_result.get()
    new_result += "1"
    display_result.set(new_result)


def add_two():
    new_result = display_result.get()
    new_result += "2"
    display_result.set(new_result)


def add_three():
    new_result = display_result.get()
    new_result += "3"
    display_result.set(new_result)


def add_four():
    new_result = display_result.get()
    new_result += "4"
    display_result.set(new_result)


def add_five():
    new_result = display_result.get()
    new_result += "5"
    display_result.set(new_result)


def add_six():
    new_result = display_result.get()
    new_result += "6"
    display_result.set(new_result)


def add_seven():
    new_result = display_result.get()
    new_result += "7"
    display_result.set(new_result)


def add_eight():
    new_result = display_result.get()
    new_result += "8"
    display_result.set(new_result)


def add_nine():
    new_result = display_result.get()
    new_result += "9"
    display_result.set(new_result)


def clear():
    new_result = ""
    display_result.set(new_result)


def divide():
    new_result = display_result.get()
    new_result += "/"
    display_result.set(new_result)


def add():
    new_result = display_result.get()
    new_result += "+"
    display_result.set(new_result)


def subtract():
    new_result = display_result.get()
    new_result += "-"
    display_result.set(new_result)


def multiply():
    new_result = display_result.get()
    new_result += "*"
    display_result.set(new_result)


def decimal():
    new_result = display_result.get()
    new_result += "."
    display_result.set(new_result)


def equals():
    new_result = display_result.get()
    new_result = eval(new_result)
    display_result.set(new_result)


def percent():
    new_result = display_result.get()
    new_result = float(new_result) / 100
    display_result.set(new_result)


def negative():
    new_result = display_result.get()
    new_result = float(new_result) * -1
    display_result.set(new_result)


display_result = StringVar()

ariana_pic = PhotoImage(file="ariana_20.png")
liana_pic = PhotoImage(file="liana_20.png")
title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)
title.configure(background="powder blue")

result_bar = Entry(root, textvariable=display_result, width=20, justify="right")
result_bar.grid(row=2, column=1, columnspan=4)
result_bar.configure(background="black")
result_bar.configure(foreground="powder blue")

clear_button = Button(root, text="Clear", width=4, font="Helvetica 18", command=clear)
clear_button.grid(row=3, column=1, sticky="W")

negative_button = Button(root, text="+/-", width=4, font="Helvetica 18", command=negative)
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=4, font="Helvetica 18", command=percent)
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=4, font="Helvetica 18", command=divide)
divide_button.grid(row=3, column=4, sticky="E")

seven_button = Button(root, text="7", width=4, font="Helvetica 18", command=add_seven)
seven_button.grid(row=4, column=1, sticky="W")

eight_button = Button(root, text="8", width=4, font="Helvetica 18", command=add_eight)
eight_button.grid(row=4, column=2)

nine_button = Button(root, text="9", width=4, font="Helvetica 18", command=add_nine)
nine_button.grid(row=4, column=3)

multiply_button = Button(root, text="*", width=4, font="Helvetica 18", command=multiply)
multiply_button.grid(row=4, column=4, sticky="E")

four_button = Button(root, text="4", width=4, font="Helvetica 18", command=add_four)
four_button.grid(row=5, column=1, sticky="W")

five_button = Button(root, text="5", width=42, font="Helvetica 18", command=add_five, image=ariana_pic)
five_button.grid(row=5, column=2)

six_button = Button(root, text="6", width=4, font="Helvetica 18", command=add_six)
six_button.grid(row=5, column=3)

subtract_button = Button(root, text="-", width=4, font="Helvetica 18", command=subtract)
subtract_button.grid(row=5, column=4, sticky="E")

one_button = Button(root, text="1", width=42, font="Helvetica 18", command=add_one, image=liana_pic)
one_button.grid(row=6, column=1, sticky="W")

two_button = Button(root, text="2", width=4, font="Helvetica 18", command=add_two)
two_button.grid(row=6, column=2)

three_button = Button(root, text="3", width=4, font="Helvetica 18", command=add_three)
three_button.grid(row=6, column=3)

add_button = Button(root, text="+", width=4, font="Helvetica 18", command=add)
add_button.grid(row=6, column=4, sticky="E")

zero_button = Button(root, text="0", width=4, font="Helvetica 18", command=add_zero)
zero_button.grid(row=7, column=1, sticky="W")

decimal_button = Button(root, text=".", width=4, font="Helvetica 18", command=decimal)
decimal_button.grid(row=7, column=2)

equals_button = Button(root, text="=", width=8, font="Helvetica 18", command=equals)
equals_button.grid(row=7, column=3, sticky="NESW", columnspan=2)


root.mainloop()