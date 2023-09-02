#-----------------------------
# task of GUI led (on or off).
#-----------------------------


from tkinter import *

root = Tk()
root.resizable(False,False)

# functions of led off and on

def led_on():
    canvas.itemconfig(circle, fill="red")
    label3.config(text="Led is on")

def led_off():
    canvas.itemconfig(circle, fill="white")
    label3.config(text="Led is off")

# handlers

canvas = Canvas(root, width=200, height=200)
circle = canvas.create_oval(50, 50, 150, 150, fill="white")
button_on = Button(root, text="LED On", command=led_on)
button_off = Button(root, text="LED Off", command=led_off)
label3 = Label(root)
# placing

canvas.pack()
label3.pack()
button_on.pack()
button_off.pack()


root.mainloop()
