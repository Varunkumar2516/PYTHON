str=input("Enter the string : ")

A=list(str)
print("List format",A)
A.sort()  #first way
B=sorted(A)   #2nd way
print("Sorted List Format",A)
print("Sorted List Format",B)

C=''.join(A)
print("String Sorted Format",C)

#output
"""Enter the string : I AM VARUN
List format ['I', ' ', 'A', 'M', ' ', 'V', 'A', 'R', 'U', 'N']       
Sorted List Format [' ', ' ', 'A', 'A', 'I', 'M', 'N', 'R', 'U', 'V']
Sorted List Format [' ', ' ', 'A', 'A', 'I', 'M', 'N', 'R', 'U', 'V']
String Sorted Format   AAIMNRUV"""