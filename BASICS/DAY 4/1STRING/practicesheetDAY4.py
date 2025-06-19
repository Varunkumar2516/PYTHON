#*****************************#
#       Practice sheet day 4  #
#        STRING               #
#*****************************#
STRING="Why Fit in ,When You Are Born to Stand Out!"
print("String",STRING)
"""Problems:
1.Write a Program to Find the length of the following String
2.Write a program to Check how many Time alphabet o is occuring
3.write a program to convert whole string into lower and upper cases
4.Write a program to convert the following string into a title
5.Write a program to find the index of 'fit in'"""

#1
print("\n1. LENGTH OF STRING :")
print(len(STRING))


#2
print("\n2. o Occuring in STRING ",end=" ")
print(STRING.count("o"),"Times")


#3
print("\n3. Whole String in Lower and Upper CASE")
print("Lower Case :: ",STRING.lower())
print("upper Case :: ",STRING.upper())



#4
print("\n4. TITLE FORMAT:: ",STRING.title())


#5
print("\n5. Index Number of 'Fit in'")
print(STRING.find("Fit in"))
print(STRING.index("Fit in"))
print(STRING.find("z"))