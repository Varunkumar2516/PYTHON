# ===============================
#  Day 9: Set Theory in Python
# ===============================
# Definition:
# A Set is an unordered collection of unique elements.
# Sets support mathematical operations like union, intersection,
# difference, and symmetric difference.

# Create two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Both Sets\nA=",A,"\nB=",B)


#Set Operations ?? NOt CHANGE ORIGINAL SETS 
#Only provide the new set for simple view and use
# -------------------------------
print("\n1. Union - A ∪ B")
# Combines all elements from both sets, no duplicates
print("Union using | :", A | B)
print("Union using .union():", A.union(B))

# -------------------------------
print("\n2. Intersection - A ∩ B")
# Returns elements common to both sets
print("Intersection using & :", A & B)
print("Intersection using .intersection():", A.intersection(B))

# -------------------------------
print("\n3. Difference - A - B")
# Elements in A but not in B
print("Difference A - B using - :", A - B)
print("Difference A - B using .difference():", A.difference(B))

# -------------------------------
print("\n4. Symmetric Difference - A △ B")
# Elements in either A or B but not both
print("Symmetric Difference using ^ :", A ^ B)
print("Symmetric Difference using .symmetric_difference():", A.symmetric_difference(B))

# -------------------------------
print("\n5. Membership Test")
# Check if an element exists in a set
print("Is 3 in A?", 3 in A)
print("Is 10 not in B?", 10 not in B)
C=A|B
print("A U B",C)
n=int(input("Enter the Number to check in A ∪ B"))
print(f"IS {n} in A ∪ B",n in C)

# -------------------------------
print("\n6. Length of Set")
print("Length of A:", len(A))

# -------------------------------
print("\n7. Add and Remove Elements")
C = set()
print("Initial Empty Set:", C)
#Adds element x to the set
C.add(10)
print("After adding :", C)

C.update([20, 30])
print("After adding multiple values:", C)

#Removes x from the set. Does nothing if x is not present.
k=C.discard(23634)
print("After discarding 20:", C)

#Removes x from the set. Raises an error if x is not present.
C.remove(20)
print("After removing 10:", C)

# -------------------------------
print("\n8. Set Clearing and Popping")
C.add(99)


print("Before pop:", C)
#Removes and returns an arbitrary element. Raises an error if empty.
x=C.pop()
print("After pop:",x, C)
#Removes all elements from the set. Set becomes empty.
C.clear()
print("After clearing:", C)

# -------------------------------
print("\n9. Empty Set Definition")
# IMPORTANT: {} is an empty dictionary, not a set
empty_set = set()
print("Empty set:", empty_set)
print("Type check:", type(empty_set))

