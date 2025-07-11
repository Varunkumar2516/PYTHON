"""
Project: Rock, Paper, Scissors 

Goal :
User selects rock, paper, or scissors — computer randomly picks — and then compare who wins.

"""
import random

choices = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors Game ")
user_win=0
user_lose=0
while True:
    user = input("Choose rock, paper or scissors (or 'quit' to stop): ").lower()
    if user == 'quit':
        print("Thanks for playing!")
        break
    if user not in choices:
        print("Invalid choice. Try again!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)
    
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        user_win+=1
        print("You win! ",user_win," times")
        


    else:
        user_lose+=1
        print("You lose! ",user_lose," times")
        

print("\t","--"*20)
print("\t\t\tResult ")
print("\t","--"*20)
print(f"User Wins : {user_win} times \nUser Lose : {user_lose} times")
if user_win==user_lose:
    print("Tie between you and computer")
if user_win>user_lose:
    print("User Is Winner ! ")
else:
    print("User Lose Better Luck Next time")
#  Concepts used: 

# - User interaction & decision-making logic

# - Using random.choice() for randomness

