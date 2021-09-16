#Just simple guessing game...
from random import randint



for i in range(1, 20, 1):
    GuessNumber = int(input("Please enter your guess number : "))
    RandomNumber = randint(1,5)


    if GuessNumber == RandomNumber:
        print("You have won")

    else:
        print("You have lost!!")
        print("Random number was : ", RandomNumber)




