
#-----------------------------------------------------------------------
#Using “Pyautogui” to open Emails and change Emails from unread to read.
#-----------------------------------------------------------------------


import webbrowser
import pyautogui
import time

while True:
    x ,y= pyautogui.position()
    print(x,y)

webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)
pyautogui.click(x=1438,y=143)
time.sleep(2)
pyautogui.write("label:unread ")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.click(x=1535,y=261)
time.sleep(2)
pyautogui.click(x=1472,y=291)
time.sleep(2)
