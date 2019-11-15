# created by Allison Dixon
# last modified November 15, 2019
# unit 8 daily exercises

from tkinter import *

root = Tk()

# problem 1

# hello_label = Label(root, text="Hello, World")
# hello_label.grid(row=1, column=1)

# problem 2
user_name = StringVar()
enter_name = Entry(root, textvariable=user_name)
enter_name.grid(row=2, column=1)
hello_name = Label(root, text="Hello," + user_name)

root.mainloop()