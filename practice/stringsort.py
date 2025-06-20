str=input("Enter the string")

A=list(str)
print("List format",A)
A.sort()
B=sorted(A)
print("Sorted List Format",A)
print("Sorted List Format",B)

C=''.join(A)
print("String Sorted Format",C)
