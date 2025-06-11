#===================
#PRACTICE_SECTION 2
#===================
"""A set of 5 beginner-level Python programs to improve basic logic:
1. Check if a number is positive, negative, or zero.
2. Determine if a number is even or odd using shorthand.
3. Menu-driven area calculator (square, rectangle, circle, triangle).
4. Check if a letter is a vowel or consonant.
5. Detect the number of digits in a number (up to 5 digits)."""
import math

#Program 1: Write a program to check if a number is positive or not.
num=int(input("1.. ENter the any number "))
if num>0:print(f" Number {num} is Positive ")
elif num==0: print(f"Number is {num}")
else : print(f"Number {num} is Negative")

#Program 2: Write a program to check whether number is odd or even
a=int(input("2.. Enter the any number"))  
#using shorthand if-else statement
print("Number is even ") if a%2==0 else print("Number is odd")

#program 3:  Create Area calculator
print("3..******AREA CALCULATOR*******")
print("Press input according to following ")
print("PRESS 1. for SQUARE area")
print("PRESS 2. for RECTANGLE area")
print("PRESS 3. for  CIRCLE area")
print("PRESS 4. for TRAINGLE area")
choice=int(input("Enter the choice"))

if choice==1:
    len=float(input("Enter the side of square"))
    area=len*len
    print(f"Area of square is :: {area}")
elif choice==2:
     length=float(input("Enter the length of rectangle"))
     breadth=float(input("Enter the breadth of the rectangle"))
     area=length*breadth 
     print(f"Area of rectangle is :: {area}")   
elif choice==3:
     radius=float(input("Enter the radius of circle"))
     area=(22/7)*radius*radius
     print(f"Area of circle is :: {area}")
elif choice==4 :
     base=float(input("Enter the base of traingle"))
     height=float(input("Enter the height of traingle"))
     area=0.5*base*height
     print(f"Area of traingle is :: {area}")
else:
     print("Invalid choice")

#program 4: Write a program check whether the passed letter is vowel or not
letter =input("Enter the single letter")
# if letter =='a' or letter =='e' or letter =='i' or letter =='o' or letter =='u':
#      print("The given letter is Vowel")
if letter in "aeiouAEIOU":
     print("The letter is Vowel")
else:
     print("The letter is consonent")

#program 5:Write a program to check if a number is a single digit number
#2-digit number or so on /..... upto 5 digit.
num=int(input("Enter the any number atmost of 5 digits:: "))
if num >=0 and num<=9:
     print(f"{num} is one digit Number")
if num >=10 and num<=99:
     print(f"{num} is two digit NUMBER")
if num >=100 and num<=999:
     print(f"{num} is  three digit NUmber")
if num >=1000 and num<=9999:
     print(f"{num} is Four digit NUmber")
if num >=10000 and num<=99999:
     print(f"{num} is FIve digit Number" )



       