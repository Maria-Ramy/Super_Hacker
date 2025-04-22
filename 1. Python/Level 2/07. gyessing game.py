#Create a basic number guessing game
import random
guess_num = random.randint(1, 10)
chances = 3
counter=0
while counter < chances:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == guess_num:
        print("You won!")
        break
    else:
        print("Try again!")
        counter += 1
if user_guess != guess_num:
    print(f"Sorry, you lost. The number was {guess_num}")
