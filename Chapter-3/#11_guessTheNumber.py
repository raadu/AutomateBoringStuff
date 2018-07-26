# My program is slightly different from the one in the book example page 74.
# This program asks user to take numbers between 1 to 10. It asks the
# user highest 6 times.
import random

secretNumber=random.randint(1,10)

for guessNumber in range(0,6):
    print("Guess a number between 1 to 10:")
    guess=int(input())

    if guess>10 or guess<1:
        print("Sorry, please select numbers between 1 to 10.")
    elif guess>secretNumber:
        print("Your guessed number is greater\n")
    elif guess<secretNumber:
        print("Your guessed number is smaller\n")

    else:
        break

if guess==secretNumber:
    print("Congratz! you guessed the right number in "+str(guessNumber)+" tries")
else:
    print("Sorry you guessed the wrong number.")