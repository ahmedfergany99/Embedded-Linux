#-----------------------------------------------------------
# Make this template and each button display different name.
#-----------------------------------------------------------

from tkinter import *

window = Tk()

# functions when pressing the buttons

def button_1():
    print("button 1 is pressed")
    
def button_2():
    print("button 2 is pressed")
    
def button_3():
    print("button 3 is pressed")
    
def button_4():
    print("button 4 is pressed")

# sizing of the window

window.title("task_1")
window.geometry("255x100+1000+200")
window.resizable(False,False)
window.configure(background="black")

# handlers

button1 = Button(window,text="Butten 1",command=button_1)
button2 = Button(window,text="Butten 2",command=button_2)
button3 = Button(window,text="Butten 3",command=button_3)
button4 = Button(window,text="Butten 4",command=button_4)



# placing

button1.grid(row=0,column=1)
button2.grid(row=1,column=0)
button3.grid(row=1,column=2)
button4.grid(row=2,column=1)

# loop to keep running untill i close it 

window.mainloop()
