# List A Problems
A = ["Ross", "Rachel", "Monica", "Joe"]

# 1. Write a program to swap the first and fourth elements.
#First Element A[0],3rd Element A[2]
print("1.")
print("Before Swapping :",A)
A[0],A[2]=A[2],A[0]
print("After Swapping :",A)




# 2. Write a program to add a new value at the second position.
A.insert(2,"Varun")
print("After Insertion ",A)



# 3. Write a program to delete a value from the third position.
A.pop(3)
print("After Deletion",A)
#OR
#A.pop(3)


# List B Problems
B = [13, 7, 12, 10]

# 1. Write a program to multiply all the numbers in the list.
Multi=1
for i in B:
   Multi*=i
print("Multiplication of all Numbers in list",Multi)


# 2. Write a program to get the largest number from the list.
greatest=B[0]
for i in range(1,len(B)):
    if B[i]>greatest:
        greatest=B[i]
print("Greatest Element of the list is:: ",greatest)
"""
alterantive Method
B.sort()
greatest=B[-1]
print(greatest)"""





# 3. Write a program to get the smallest number from the list.
smallest=B[0]
for i in range(1,len(B)):
    if B[i]<smallest:
        smallest=B[i]
print("Greatest Element of the list is:: ",smallest)
"""
alterantive Method
B.sort()
smallest=B[1]
print(smallest)"""