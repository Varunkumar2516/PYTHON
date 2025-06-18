# ============================================
# DAY 4 - STRINGS IN PYTHON (Basics & Practice)
# ============================================

# 1 String Declaration
# Strings can be defined using single, double, or triple quotes.

single_quote_str = 'Hello'
double_quote_str = "World"
multi_line_str = """This is 
a multi-line
string"""
print(single_quote_str)
print(double_quote_str)
print(multi_line_str)

# ------------------------------------------------

# 2 String Indexing
# Characters in a string are indexed starting from 0.
# Negative indexing starts from the end (-1 is last character).

text = "Python"
print("First character:", text[0])   # P
print("Last character:", text[-1])   # n

# ------------------------------------------------

# 3 String Slicing
# You can extract a substring using slicing: [start:end]

print("Slicing text[0:3]:", text[0:3])   # Pyt
print("Slicing text[2:]:", text[2:])     # thon

# ------------------------------------------------

# 4 String Length
# To get the number of characters in a string.

print("Length of string:", len(text))  # 6

# ------------------------------------------------

# 5 Loop Through a String
# Strings are iterable, so we can loop through them.

print("Characters in the word:")
for ch in text:
    print(ch)

# ------------------------------------------------

# 6 String Methods
# Python provides many built-in string functions.

sample = "hello world"
print(sample.upper())          # HELLO WORLD
print(sample.lower())          # hello world
print(sample.title())          # Hello World
print(sample.capitalize())     # Hello world
print(sample.count('l'))       # 3
print(sample.replace('world', 'Python'))  # hello Python
print("Size of string",len(sample))
# ------------------------------------------------

# 7 String Concatenation
# Combine strings using + operator.

greeting = "Hello"
name = "Alice"
print(greeting + " " + name)  # Hello Alice

# ------------------------------------------------

# 8 String Formatting
# Using f-strings or format() to insert variables.

age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# ------------------------------------------------

# 9 Checking Substring
# Use 'in' keyword to check if substring exists.

if "Py" in "Python":
    print("Yes, 'Py' is in Python")

# ------------------------------------------------

# 10 Comparing Strings
# Lexicographical (dictionary order) comparison.

a = "apple"
b = "banana"
print(a == b)    # False
print(a < b)     # True

# ------------------------------------------------

# 11 String Reversal using slicing
original = "Python"
reversed_str = original[::-1]
"""Other methods:
reverse=original(start,stop,step)
reverse=original(len(original)-1,-1,-1)
start=len(original)-1
stop=-1
it means stop before last character
step is -1 everytime"""
print("Reversed string:", reversed_str)

# ------------------------------------------------

# 12 Get Last Character (Even if length is unknown)
user_input = input("Enter a word: ")
print("Last character is:", user_input[-1])  # works regardless of length

# ============================================
# END OF STRING BASICS (DAY 4)
# ============================================
