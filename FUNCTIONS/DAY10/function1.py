#+=============================
#     DAY 10 FUNCTIONS
#==============================

#A **function** is a reusable block of code that performs a specific task.

print("\n1. Simple Function with Parameters")
def add(a, b):
    return a + b
print(add(2, 3))  # Output: 5

print("\n1.1. Simple Function without Parameters")
def greet():
    print("Hello")
greet()


#Different argument of fuction
#1.Default argument
print("\n2. Function with Default Value")
def ADD(A=0,B=0):
    return A+B
print(ADD(2,3))
print(1)
print()
print(5)

print("\n2. Function with keyword Argument")
def ADD(A=0,B=0):
    return A-B

print(ADD(A=9,B=2))
print(ADD(B=2,A=9))
print(ADD(B=9,A=2))
print(ADD(B=10,A=2))


# *args is used to handle the variable number of arguments 
# args basically create the tuple of arguments 
print("\n\n3. Function with *args (Multiple Values) Cretes Tuple of arguments passed")
def multiply_all(*args):
    result = 1
    for n in args:
        result *= n
    print(args,type(args))
    return result
    
print(multiply_all(2, 3, 4)) 
print(multiply_all(2, 3, 4,5,6)) 
print(multiply_all(2, 3, 4,34,2,4,7,2,1,3)) 


print("\n4. Function with **kwargs (Multiple Keyword Values)")
def user_info(**kwargs):
    for (key, value) in kwargs.items():
        print(f"{key} = {value}")
    print(kwargs)        
user_info(name="Aman", age=25, country="India")
# Output:
# name = Aman
# age = 25


#anaother function
print("Capital function")
def capital_function(**dict):
    for key,value in dict.items():
     print(f"{key} = {value}")

capital_function(india='delhi',srilanka='colombo',nepal='kathmandu')


print("\n5. To see the defination of any fucntion ::")
print("1...print fucntion documentation :")
print(print.__doc__,end="\n\n")

print("2...list function documentation :")
print(list.__doc__)



