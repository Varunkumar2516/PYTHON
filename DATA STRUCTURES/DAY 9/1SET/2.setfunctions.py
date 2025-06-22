# ===============================
# Day 9:More Function /Methods Set 
# ===============================

# Create sets for examples
A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2}
D = {1, 2, 3, 4, 5}
E = set()  # Empty set

# ---------------------------------
print("\n1. isdisjoint()")
# Definition: Returns True if two sets have no elements in common
print("A:", A)
print("B:", B)
print("A.isdisjoint(B):", A.isdisjoint(B))  # False, common element: 3
print("A.isdisjoint(E):", A.isdisjoint(E))  # True, empty set has no elements

# ---------------------------------
print("\n2. issubset()")
# Definition: Returns True if all elements of one set are in the other
print("C:", C)
print("A:", A)
print("C.issubset(A):", C.issubset(A))  # True (1,2 are in A)
print("A.issubset(D):", A.issubset(D))  # True (A is part of D)
print("A.issubset(C):", A.issubset(C))  # False
print("E.issubset(A):", E.issubset(A))  # True (empty set is subset of all sets)

# ---------------------------------
print("\n3. issuperset()")
# Definition: Returns True if the set contains all elements of another
print("A:", A)
print("C:", C)
print("A.issuperset(C):", A.issuperset(C))  # True (A has all of C)
print("C.issuperset(A):", C.issuperset(A))  # False
print("A.issuperset(E):", A.issuperset(E))  # True (any set is superset of empty set)

# ---------------------------------
print("\n4. update()")
# Definition: Adds elements from another set (or iterable) to the current set
print("Original A:", A)
A.update(B)  # Adds 3, 4, 5 to A (3 already exists, no duplication)
print("A after A.update(B):", A)

print("Original E (empty):", E)
E.update([10, 20])
print("E after E.update([10, 20]):", E)