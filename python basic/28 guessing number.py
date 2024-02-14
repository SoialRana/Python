#import random
from random import randint
for x in range(1,6):
    guessingNumber = int(input("Enter no between 1 to 5: "))
    randomNumber = randint(1,5)  #randomNumber = random()*100
    if randomNumber==guessingNumber:
        print("You have won")
    else:
        print("You have loss.")
        print("The random number was: ",randomNumber)