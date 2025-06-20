# **************************************#
#      STring  ::: Practice SHeet Day 5 #
# **************************************#

"""
Problem 1 :: A="OOTD.YOLO.BRB.GTG.OTW"
1.Write a program to separate the following string into Coma(,) Separated Values
2.Write a Program to Sort strings Alpahbeticcaly in python
3.Write a Program To remove a given character from a string
"""

A="OOTD.YOLO.BRB.GTG.OTW"
print("String : A= ",A)

#1
print("\n1.")
B=A.split('.')
print("Separated List by (.) :: ",B)

#2
print("\n2.")
B=A.split('.')
print("Simple List: ",B)
B.sort()
print("Sorted List: ",B)



#3
print("\n3.")
print("Simple List: ",A)
char=input("Enter the single character to remove from string")
B=A.replace(char,"")
print("New String :: ",B)



"""
Problem 2 :: Z="F.R.I.E.N.D.S"
1.Write a program to Remove dot (.)from the string
2.Write a Program to check the number of occurence of 'o'
"""

Z="F.R.I.E.N.D.S"
print("\n New problem String",Z)
#1
print("\n1.")
A=Z.replace(".","")
print("New string without Comma(,) :: " , A)

#2
print("\n2.")
Substring=input("Enter the substring From FRIENDS")
print("Occurence of Substring is",A.count(Substring))




