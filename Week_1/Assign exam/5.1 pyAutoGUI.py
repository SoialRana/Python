import pyautogui
row = int(input("Enter the number of row: "))

for i in range(row):
    for j in range(i + 1):
        print("#", end="")
    print()