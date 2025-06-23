# Day 10 – Part 3: Higher-Order Functions in Python

"""
A Higher-Order Function is a function that:
     Takes one or more functions as arguments
     Returns a function as its result

This is possible because functions in Python are first-class citizens.
"""

#  1. Passing a function as an argument
print("\n1. Function as Argument")

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    result = func("Hello World")
    return result

print(speak(shout))   # Output: HELLO WORLD
print(speak(whisper)) # Output: hello world


#  2. Returning a function from another function
print("\n2. Returning a Function")

def multiplier(x):

    def multiply(y):
        return x*y
    return multiply
#multiply is closure fucntion

double1=multiplier(2) #it becomes function multiply() with x=2
cube=multiplier(3)    #it becomes function multiply()  with x=3

print(double1(4))
print(cube(4))



#  3. Higher-order with lambda
print("\n3. Higher Order + Lambda")

def multiplier(x):
    return lambda y: x * y

double = multiplier(2)
triple = multiplier(3)

print(double(4))  # 8
print(triple(4))  # 12

#4.Create List Of Squares from list of numbers with HOF 
print("#4.Create List Of Squares from list of numbers with HOF ")
List=[1,2,3,4,5,6,7,8,9]
print(List)

def multiply(x):
    return x**2

def HOF(f,L):
    mylist=[]
    for i in L:
     mylist.append(f(i))
    return mylist

newlist=HOF(multiply,List)
print(newlist)


#5 Same Above thing with Lambda function :: No need of the multiply function
print("\n\n#5 Same Above thing with Lambda function :: No need of the multiply function")
List=[1,2,3,4,5,6,7,8,9]
print(List)

def HOF(f,L):
    mylist=[]
    for i in L:
     mylist.append(f(i))
    return mylist

newlist=HOF(lambda x:x**2,List)
print(newlist)
print("\n\n     Alterntive")
#similar method for less lines of codes using list comprehension
def HOF(func, data):
    return [func(x) for x in data]

squares = HOF(lambda x: x**2, List)
print(squares)  


#  6. Built-in map() as higher-order
print("\n6. Using Built-in map()")

doubled = list(map(lambda x: x * 2, List))
print(doubled)  


#  Summary:
"""
- Higher-order functions are powerful for abstraction.
- Python allows passing and returning functions because functions are first-class objects.
- Common examples: map(), filter(), decorators.
"""
