#=======================================================
#  Day 11: Functions As First Class Citizen
#========================================================


#  What is a First Class Citizen?????
# In Python, functions are first-class citizens, meaning they are treated like any 
# other object — 
# you can assign them to variables,
#  pass them as arguments,
#  return them from other functions,
#  and store them in data structures.

print("1.Assign to a variable")
def square(n):
    return n**2

myvariable=square
print(type(myvariable))
#using varibale as function
print(myvariable(5))


#simialr  to CLosures
#A closure is a function that remembers the environment in which it was created.
# Even after the outer function  finishes, the inner function  retains access to 
# the variables that were in scope when it was defined 
#example: nested functions
print("\n 2. Return function and assign it to variable. explained in 1.")
def multiplier(x):

    def multiply(y):
        return x*y
    return multiply
#multiply is closure fucntion

double1=multiplier(2) #it becomes function multiply() with x=2
cube=multiplier(3)    #it becomes function multiply()  with x=3

print(double1(3))
print(cube(5))


print("\n3.Pass Function as Argument")
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    print(func("Hello"))

speak(shout)   # Output: HELLO
speak(whisper) # Output: hello


print("\n 4.  Store FUnction data structures")

def square1(x): return x * x
def cube(x): return x * x * x

# adding functions in list
list = [square1, cube]

#iterte over list to call functions
for i in list:
    print(i(3))
# Output:
# 9
# 27


print("\n 5.  Delete functions")
def mysquare(n):
     return n*n
print(mysquare(5))
del mysquare
print("mysquare is deleted")


