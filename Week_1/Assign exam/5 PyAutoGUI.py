import pyautogui
from time import sleep
sleep(5)
row=int(input("Enter number of row:"))
for i in range(row):
        pyautogui.write('#'*(i+1))
        pyautogui.write('\n')