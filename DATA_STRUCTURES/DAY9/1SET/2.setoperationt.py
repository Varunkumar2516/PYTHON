#SImple doubt regrading the set operations

A = {1, 2, 3}
B = {3, 4, 5}

#they return the New Set 
#it does not change the original set
# 1. Union (combines all unique elements)
print(A.union(B))           # {1, 2, 3, 4, 5}
K=A.union(B)
print(K)

# 2. Intersection (common elements)
print(A.intersection(B))    # {3}

# 3. Difference (elements in A not in B)
print(A.difference(B))      # {1, 2}

# 4. Symmetric Difference (elements in A or B but not both)
print(A.symmetric_difference(B))  # {1, 2, 4, 5}

print("A after all:", A)  # A remains {1, 2, 3}



##they return the same modified Set 
#it change the original set
A = {1, 2, 3}
B = {3, 4, 5}

# 5. update() — adds B’s elements to A
K=A.update(B)
print("A after update:", K)  # {1, 2, 3, 4, 5}

# Reset A
A = {1, 2, 3}

# 6. intersection_update() — keep only common elements
A.intersection_update(B)
print("A after intersection_update:", A)  # {3}

# Reset A
A = {1, 2, 3}

# 7. difference_update() — remove elements from A that are also in B
A.difference_update(B)
print("A after difference_update:", A)  # {1, 2}

# Reset A
A = {1, 2, 3}

# 8. symmetric_difference_update() — A becomes elements in A or B but not both
A.symmetric_difference_update(B)
print("A after symmetric_difference_update:", A)  # {1, 2, 4, 5}


"""Important 
Update () funtions return changed Original array
"""



A={1,2,3}
B={4,5,6}
A.difference_update(B)
print(A)