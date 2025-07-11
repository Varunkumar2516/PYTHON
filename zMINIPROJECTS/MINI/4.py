"""Project 4: Random Password Generator 

Goal :
Generate a random password using letters, numbers, and symbols based on user input for password length.
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Random Password Generator ")
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")

# Concepts used:

# - string module for characters

# - random.choice() for selecting characters

# - Handling errors with try-except

# - Creating secure passwords in seconds!
