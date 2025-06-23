#  Day 10: Nested Functions

#  What is a Nested Function
# A nested function is a function defined inside another function.
# It's useful for encapsulation, closures, and creating function factories.

# Syntax:
# def outer():
#     def inner():
#         # inner code
#     # outer code

print("\n1. Simple Nested Function")
def outer():
    def inner():
        print("This is the inner function.")
    inner()
    print("This is the outer function.")
outer()

print("\n 2. Nested function")
def f():
    def g():
        print("Inside function g")
    g()
    print("Inside function f")
f()


print("\n3. Nested Function Returning Value")
def greet_user(name):
    def format_name(n):
        return n.strip().title()
    formatted = format_name(name)
    return f"Hello, {formatted}!"

print(greet_user("  aman "))



print("\n4. Nested Function with No Return")
def logger(message):
    def log():
        print(f"LOG: {message}")
    log()

logger("File loaded successfully.")

print("\n5. Nested Function Used for Repeated Code")
def calculator():
    def square(n):
        return n * n
    print(square(2))
    print(square(3))
    print(square(4))

calculator()



#CLOSURE EXAMPLES
print("\n6. Returning Inner Function (Closure)")
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = multiplier(2)    # it basically makes the double as function multiply    or """double=multiply""" double becomes now function
#python allows to function as first class citizens we will understand it in further next file
#in python we can assign functions to the other varible to make the variable as function
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15


print("\n7. Accessing Outer Variable (Closure Example)")
def power_raiser(n):
    def raise_power(x):
        return x ** n
    return raise_power

square = power_raiser(2)
cube = power_raiser(3)

print(square(4))  # 16
print(cube(2))    # 8

print("\n7. Using Nonlocal Keyword")
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
