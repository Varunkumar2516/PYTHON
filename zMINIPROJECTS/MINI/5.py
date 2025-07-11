
"""Project 5: Dice Rolling Simulator 
 
Goal :
Generate and display a random number between 1 and 6 each time the user rolls.

"""

from random import randint

def roll_dice():
    return randint(1, 6)

print("Dice Rolling Simulator ")

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == "yes":
        print("You rolled:", roll_dice())
    elif roll == "no":
        print("Thanks for playing!")
        break
    else:
        print("Please type 'yes' or 'no'")

# Concepts Used :

# - Using random.randint()

