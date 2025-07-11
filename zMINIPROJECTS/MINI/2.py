
#  Project 2: Simple Calculator App ➕➖✖➗


# Goal :
# Let the user input two numbers and choose an operation. Return the result.



def calculator():
    print("Simple Calculator")
    while True:
         
        num1 = float(input("Enter first number: "))
        
        num2 = float(input("Enter second number: "))

        while True:
            op = input("Choose operation (+, -, *, /): ")
            if op == '+':
                print("Result:", num1 + num2)
            elif op == '-':
                print("Result:", num1 - num2)
            elif op == '*':
                print("Result:", num1 * num2)
            elif op == '/':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero!")
            else:
                print("Invalid operation!")
            myinput=input("\nEnter (Yes/No) For Again :")
            if myinput.lower()=="no":
                break
        myinput=input("\nEnter (Yes/No) For New Numbers :")
        if myinput.lower()=="no":
            break
        

calculator()

# Concepts used :

# - Working with float numbers

# - Conditional logic (if-elif-else)

# - Handling division by zero

# - Creating reusable code with functions

