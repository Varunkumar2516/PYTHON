# ----------------------------------
# Day 7: Tuple Comprehensions and Examples
# ----------------------------------

# 1. TUPLE OF: Square of numbers from 0 to 10
squares = tuple(i**2 for i in range(11))
print("1. Squares Tuple:", squares)
# Output: (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# 2. TUPLE OF: Even numbers from 0 to 10
evens = tuple(i for i in range(0, 11) if i % 2 == 0)
print("2. Even Numbers Tuple:", evens)
# Output: (0, 2, 4, 6, 8, 10)

# 3. TUPLE OF: Prime numbers from 0 to 20
primes = tuple(
    i for i in range(2, 21)
    if all(i % j != 0 for j in range(2, int(i**0.5)+1))
)
print("3. Prime Numbers Tuple:", primes)
# Output: (2, 3, 5, 7, 11, 13, 17, 19)

# 4. TUPLE OF: Convert all strings to uppercase
words = ['data', 'science', 'python', 'rocks']
upper_words = tuple(word.upper() for word in words)
print("4. Uppercase Tuple:", upper_words)
# Output: ('DATA', 'SCIENCE', 'PYTHON', 'ROCKS')

# 5. TUPLE OF: Remove spaces from a list of strings
messy_strings = ['  hello ', ' world', 'python ', ' is ', ' awesome  ']
cleaned = tuple(s.strip() for s in messy_strings)
print("5. Cleaned Tuple:", cleaned)
# Output: ('hello', 'world', 'python', 'is', 'awesome')
