# created by Allison Dixon
# last modified November 15, 2019
# unit 8 daily exercises

from tkinter import *

root = Tk()

# problem 1

# hello_label = Label(root, text="Hello, World")
# hello_label.grid(row=1, column=1)

# problem 2


# def say_hi():
#     other_name = user_name.get()
#     your_name.set(other_name)
#     if other_name == "":
#         your_name.set("You forgot to enter your name")
#     else:
#         your_name.set("Hello, " + other_name)
#
#
# user_name = StringVar()
# your_name = StringVar()
# enter_name = Entry(root, textvariable=user_name)
# enter_name.grid(row=1, column=1)
# say_hello = Button(root, text="Say Hello", command=say_hi)
# say_hello.grid(row=3, column=1)
#
# hello = Label(root, textvariable=your_name)
# hello.grid(row=2, column=1)

# problem 3

def convert():

degrees_f = Label(root, text="degrees F:")
degrees_f.grid(row=1, column=1)
f_entry = Entry(root)
f_entry.grid(row=1, column=2)
degrees_c = Label(root, text="degrees C:")
degrees_c.grid(row=2, column=1)
c_label = Label(root)
c_label.grid(row=2, column=2)
convert = Button(root, text="Convert")
convert.grid(row=3, column=2)


root.mainloop()
