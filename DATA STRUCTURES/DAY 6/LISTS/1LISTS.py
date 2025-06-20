#******************************#
#         Day-6                #
#          LIST                #
#*****************************8#

"""A list is a mutable, ordered collection of
 items in Python. You can store multiple values
 in a single variable using square brackets [].
 Lists are ordered, mutable collections: `[]`
- 🎯 Use `.append()`, `.insert()`, `.remove()`, `.pop()`, `len()`, `.sort()`
- 🔁 Loop or use list comprehensions for data transformation
- 🔍 Great for tabular data, string parsing, and preprocessing in Data Science"""


# Creating a list
fruits = ['apple', "banana", "cherry"]
print(fruits)   # Output: ['apple', 'banana', 'cherry']
print(type(fruits))


#LIST OPERATIONS
# ----------------------------------------
print("\n\n1. Accessing Elements:same as the string")
print(fruits[0])      # First item: apple
print(fruits[-1])     # Last item: cherry

# ----------------------------------------
print( "\n\n2. Slicing Lists")
#same as strings fruits[start:end:step]
print(fruits[1:3])    # Output: ['banana', 'cherry']
print(fruits[:2])     # Output: ['apple', 'banana']
print(fruits[::-1])   #Reverse of List 
# ----------------------------------------
print("\n\n3.Adding Elements") 
fruits.append("orange")  # Add at end
fruits.insert(1, "kiwi") # Insert at index 1 :: for specific index
print(fruits)            # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# ----------------------------------------
print("\n\n4. Removing Elements")
fruits.remove("banana")  # Remove by value
fruits.pop()             # Remove last item : also the index can be provided to delete that index item
print(fruits)            # ['apple', 'kiwi', 'cherry']

# ----------------------------------------
print("\n\n5.Updating Elements")
fruits[0] = "grape"      # Replace 'apple' with 'grape'
print(fruits)            # ['grape', 'kiwi', 'cherry']

# ----------------------------------------
print(" \n\n6. List Length")
print(len(fruits))       # Output: 3

# ----------------------------------------
print("\n\n7. Sorting Lists") 
numbers = [5, 2, 9, 1]
numbers.sort()           # Sort ascending
print(numbers)           # Output: [1, 2, 5, 9]

numbers.sort(reverse=True)  # Sort descending
print(numbers)              # Output: [9, 5, 2, 1]

# ----------------------------------------
print("\n\n8.Looping Through a List")
for i in fruits:
    print(i)  # Prints each fruit

# ----------------------------------------
#IN NEXT FILE DETAILED VERSION OF LIST COMPREHENSIONS
print("\n\n9. List Comprehension") 
#List comprehension is a concise way to create lists using a single line of code.
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# ----------------------------------------
print(" \n\n10. Check if Item Exists")
if "grape" in fruits:
    print("Yes, 'grape' is in the list")

# ----------------------------------------
print("🧪 Bonus: String to List")
sentence = "Python is fun"
words = sentence.split()  # Splits by space
print(words)              # Output: ['Python', 'is', 'fun']
