#------------------------------------------------------------------------------------------------------------------------------
# Write a program in Python that displays a window to the user that asks them to enter an integer N and displays its factorial.
#------------------------------------------------------------------------------------------------------------------------------

from tkinter import *

window = Tk()

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def validate():
  n = int(entry.get())
  factorial_result = factorial(n)
  label_result.config(text=f"The factorial of {n} is {n}! = {factorial_result}")


# hannlers
window.geometry("350x100+1000+200")
window.resizable(False,False)
label_enter_number = Label(window, text="Enter a number: ")
entry = Entry(window)
button_calculate = Button(window, text="Validate", command=validate)
label_result = Label(window, text="")

# placing

label_enter_number.pack()
entry.pack()
button_calculate.pack()
label_result.pack()

window.mainloop()
