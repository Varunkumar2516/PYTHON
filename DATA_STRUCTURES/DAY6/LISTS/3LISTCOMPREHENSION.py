##########################
#  LIST COMPREHENSION    #
##########################

"""List comprehension is a concise way to create lists using a single line of code.
It lets you generate a new list by applying an expression to each item in an iterable 
(like a range, string, or another list)."""

"""
BASIC SYNTAX::
result=[expression for item in iterable]
This is equivalent to::

result = []
for item in iterable:
    result.append(expression)
"""


#1. Create List of Square of numbers from 0 to 10:
print("\n1. LIST OF: Square of numbers from 0 to 10 ")
square=[i**2 for i in range(0,11)]
print(square)

#2. LIST OF: Create a list of even numbers from 0 to 10. 
print("\n2. LIST OF: Create a list of even numbers from 0 to 10. ")
even=[i for i in range(0,11) if i%2==0]
print(even)


#3.LIST OF: Create a list of PRIME numbers from 0 to 20.
print("\n3.LIST OF: Create a list of PRIME numbers from 0 to 20.")
prime=[
    i for i in range(2,21)
    if all(i%j!=0 for j in range(2,int(i**0.5)+1))
]
print(prime)


#4 LIST OF: Convert all strings to uppercase from another strings
print("\n#4 LIST OF: Convert all strings to uppercase from another strings")
OldList=["Apple","Banana","Cherry","Mango"]
Newlist=[i.upper() for i in OldList]
print(Newlist)

#5. LIST OF: Remove spaces from a list of strings
print("\n5. LIST OF: Remove spaces from a list of strings")
Num=["  1  ","  2  ","  3  "]
print("Num List With Unnessary spaces",Num)
NewNum=[i.strip() for i in Num]
print("New List ::",NewNum)
