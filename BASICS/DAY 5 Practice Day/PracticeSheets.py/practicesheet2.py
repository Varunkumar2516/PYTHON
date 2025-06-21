"""
Problems
1.Take an input from a user as a string then, reverse it.
2.Write a program to check if a string contains only digits.
3.Write a program to check if a string is palindrome.
4.Write a program to find number of vowels in a string.
5.Write a program to check if every word in a string begins with a capital letter."""

#1
print("\n 1.Program to reverse string  ")
str=input("Enter the string ::")
#Method1
rev=str[::-1]
print(" Method 1:Reverse of string is ::",rev)

#Method 2
rev1=""
for i in str:
      rev1=i+rev1
print(" Method 2:Reverse of string is ::",rev1)



#2
print("\n 2.Program to check string consist of only digits  ")
str=input("Enter the string :: ")
if str.isdigit():
      print(f"String {str} consist of only digits")
else:
      print(f"String {str} consist of other letters")




#3
print("\n 3.Program to check string Is Palindrome or not  ")
str=input("Enter the string :: ")
rev=str[len(str)-1:-1:-1]
if rev==str:
      print(f"String {str} is Palindrome")
else:
      print(f"String {str} is Not a Palindrome")




#4
print("\n 4.Program to count Number of Vowels in given string ")
str=input("Enter the string :: ")
vowel=0
for i in str:
      if i in "aeiou" or i in "AEIOU":
            vowel=vowel+1

print("Number of Vowels in given String is ",vowel)



#4
print("\n 5.Program to check if every word in a String begins with a Capital letter (Title)")
str=input("Enter the string :: ")
if str.istitle():
      print(f"{str} is Title and have every starting letter of word is capital")