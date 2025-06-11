#PRACTICE_SECTION 2

#Program 1: Write a program to check if a number is positive or not.
num=int(input("ENter the any number "))
if num>0:print(f" Number {num} is Positive ")
elif num==0: print(f"Number is {num}")
else : print(f"Number {num} is Negative")

#Program 2: Write a program to check whether number is odd or even
a=int(input("Enter the any number"))  
#using shorthand if-else statement
print("Number is even ") if a%2==0 else print("Number is odd")

#program 3: Write a program to create area calculator
len=int(input("Enter the length of rectangle"))
breadth=int(input("ENter the breadth of the rectangle"))
result=len*breadthz