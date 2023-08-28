import pyautogui
import time

# Press the Windows key (Start button)
pyautogui.hotkey('win')
# Pause for 1 second
time.sleep(1)

# Type 'vs'
pyautogui.write('vs')
# Pause for 1 second
time.sleep(1)

# Press Enter key
pyautogui.hotkey('enter')
# Pause for 1 second
time.sleep(1)

# Press Ctrl + Shift + X keys to open Extensions
pyautogui.hotkey('ctrl', 'shift', 'x')
# Pause for 1 second
time.sleep(1)

# Install 'clangd'
pyautogui.write('clangd')
time.sleep(6)
pyautogui.click(x=248, y=277)
time.sleep(2)
pyautogui.doubleClick(x=281, y=166)
time.sleep(2)
pyautogui.press('backspace')
time.sleep(2)

# Install 'c++ testmate'
pyautogui.write('c++ testmate')
time.sleep(6)
pyautogui.click(x=248, y=277)
time.sleep(2)
pyautogui.tripleClick(x=281, y=166)
time.sleep(2)
pyautogui.press('backspace')
time.sleep(2)

# Install 'c++ helper'
pyautogui.write('c++ helper')
time.sleep(6)
pyautogui.click(x=248, y=277)
time.sleep(2)
pyautogui.tripleClick(x=281, y=166)
time.sleep(2)
pyautogui.press('backspace')
time.sleep(2)

# Install 'cmake'
pyautogui.write('cmake')
time.sleep(6)
pyautogui.click(x=248, y=277)
time.sleep(2)
pyautogui.doubleClick(x=281, y=166)
time.sleep(2)
pyautogui.press('backspace')
time.sleep(2)

# Install 'cmake tools'
pyautogui.write('cmake tools')
time.sleep(6)
pyautogui.click(x=248, y=277)
time.sleep(2)
pyautogui.tripleClick(x=281, y=166)
time.sleep(2)
pyautogui.press('backspace')
time.sleep(2)

# Press Ctrl + W (close tab/window) , back to the code
pyautogui.hotkey('ctrl', 'w')
