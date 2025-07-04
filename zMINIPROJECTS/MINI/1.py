import random

number_to_guess = random.randint(1, 100)
guess = None
attempts = 0
guesslist=[0,100]
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(guesslist)
while guess != number_to_guess:
    
    guess = int(input(f"Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        if guess>guesslist[0]:
            guesslist[0]=guess
        print(f"Too low! Try again. in between ",guesslist)

    elif guess > number_to_guess:
        if guess<guesslist[1]:
            guesslist[1]=guess
       
        print(f"Too high! Try again. in between",guesslist)
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")


"""
Concepts used :
- random.randint() for generating numbers

- Taking user input using input() & converting input to integers

- Using while loops and if-else logic


"""