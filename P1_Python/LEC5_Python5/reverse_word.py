#------------------------------------------------------------------------------
# Write a program that asks the user to type and return him its reverse a word.
#------------------------------------------------------------------------------

import tkinter as tk

def reverse_word():
  word = entry.get()
  reversed_word = ""
  for i in reversed(word):
    reversed_word += i
  label.config(text=reversed_word)

window = tk.Tk()

window.title("task_2")
window.geometry("265x70+1000+200")
window.resizable(False,False)
window.configure(background="white")

# handlers
label1 = tk.Label(window,text="Enter a word: ")
entry = tk.Entry(window)
button = tk.Button(window, text="validate", command=reverse_word)
label = tk.Label(window)

# placing
label1.grid(row=0,column=0)
entry.grid(row=0,column=1)
button.grid(row=2,column=1)
label.grid(row=1,column=1)


window.mainloop()
