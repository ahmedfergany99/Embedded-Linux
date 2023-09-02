#------------------------------------------------------------------------------------------------------------------
# Create a graphical application in Python Tkinter that asks the user to enter two integers and displays their sum.
#------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import *

# functions when pressing the buttons

def sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    sum = num1 + num2
    label3.config(text="the sum is : "+str(sum))

def sub():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    sub = num1 - num2
    label3.config(text="the subtraction is : "+str(sub))

def validate():
    if radio_button.get() == "Add":
        sum()
    elif radio_button.get() == "Sub":
        sub()

window = tk.Tk()

radio_button = tk.StringVar()


# handlers

label1 = tk.Label(window, text="Enter the value of M :")
label2 = tk.Label(window, text="Enter the value of N :")
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
label3 = tk.Label(window)

radiobutton1 = tk.Radiobutton(window, text="Add",variable=radio_button,value="Add")
radiobutton2 = tk.Radiobutton(window, text="Sub",variable=radio_button ,value="Sub")

button3 = tk.Button(window,text="validate",command=validate)

# placing
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
label3.grid(row=2,column=0)
radiobutton1.grid(row=3,column=0)
radiobutton2.grid(row=4,column=0)
button3.grid(row=3,column=1)

window.mainloop()
