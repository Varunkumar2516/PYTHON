# ----------------------------------
# Day 7: Tuples in Python
# ----------------------------------

#TUPLE:
# A tuple is an ordered, immutable collection of values.
# It can store elements of different data types.

#  Syntax:
# my_tuple = (item1, item2, item3)


# 1. Creating a tuple
print("\n\n1. Creating a tuple")
tuple1 = (10, 20, 30, 40)
print("Tuple:", tuple1)  # Output: (10, 20, 30, 40)

# 2. Tuple with mixed data types
print("\n\n2. Tuple with mixed data types")
tuple2 = ("Data", 101, 3.14)
print("Mixed Tuple:", tuple2)

# 3. Accessing tuple elements
print("\n\n3. Accessing tuple elements")
print(" First Element:", tuple1[0])  # Output: 10
print("   Last Element:", tuple1[-1])  # Output: 40


# 4. Slicing a tuple
print("\n\n4. Slicing a tuple")
print("tuple1[1:3]:", tuple1[1:3])  # Output: (20, 30)
print("Tuple[:2]",tuple1[:2])
print("Reverse Tuple",tuple1[::-1])
newtuple=tuple1[::-1]
print("Reverse with assigned",newtuple)
rev=()
for i in range(len(tuple1)-1,-1,-1):
    rev=rev+(tuple1[i],)
print(rev)




# 5. Tuple unpacking
print("\n\n5. Tuple unpacking")
name, roll, pi = tuple2
print("Unpacked:", name, roll, pi)



# 6. Iterating over tuple
print("\n\n6. Iteration:")
for item in tuple1:
    print("  Item:", item)



# 7. Tuple methods: count() and index()
print("\n\n7. Tuple methods: count() and index()")
tuple3 = (1, 2, 3, 2, 2, 4)
print(" Count of 2:", tuple3.count(2))   # Output: 3
print("   Index of 4:", tuple3.index(4))   # Output: 5




# 8. Nesting tuples
print("\n\n8. Nesting tuples")
tuple4 = (tuple1, tuple2)
print(" Nested Tuple:", tuple4)



# 9. Converting list to tuple
print("\n\n9. Converting list to tuple")
list1 = [100, 200, 300]
# tuple5 = tuple(list1)
tuple5=()
for i in list1:
    tuple5=tuple5+(i,)
print(" Converted Tuple:", tuple5)



# 10. Immutability of Tuples
# tuple1[0] = 999  #  TypeError: 'tuple' object does not support item assignment


# -----------------------------
# Advanced Tuple Usages
# -----------------------------

# 11. Tuple Comparison
print("\n\n11. Tuple Comparison")
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
print(" Tuple Comparison: tuple_a < tuple_b =", tuple_a < tuple_b)  # True

# 12. Tuple as Dictionary Key
print("\n\n12. Tuple as Dictionary Key")
location = (27.2046, 77.4977)  # latitude, longitude
weather_data = {
    location: "Clear skies"
}
print("Weather at location:", weather_data[location])

# 13. Return Multiple Values from Function
print("\n\n13. Return Multiple Values from Function")
def min_max(values):
    return (min(values), max(values))

numbers = [4, 7, 2, 8, 1]
result = min_max(numbers)
print("Min and Max:", result)  # Output: (1, 8)

# 14. Enumerate with Tuple
print("\n\n14. Enumerate with Tuple")
print("Enumerate Example:")
colors = ('Red', 'Green', 'Blue')
for index, value in enumerate(colors):
    print(f"  Index {index}: {value}")

# ----------------------------------
# End of Tuple theory
# ----------------------------------
