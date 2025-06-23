# ----------------------------------
# Day 7: Tuple Practice Using For Loops
# ----------------------------------

# 1. TUPLE OF: Square of numbers from 0 to 10
squares = ()
for i in range(11):
    squares += (i**2,)
print("1. Squares Tuple:", squares)
# Output: (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


# 2. TUPLE OF: Even numbers from 0 to 10
evens = ()
for i in range(11):
    if i % 2 == 0:
        evens += (i,)
print("2. Even Numbers Tuple:", evens)
# Output: (0, 2, 4, 6, 8, 10)


# 3. TUPLE OF: Prime numbers from 0 to 20
primes = ()
for i in range(2, 21):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes += (i,)
print("3. Prime Numbers Tuple:", primes)
# Output: (2, 3, 5, 7, 11, 13, 17, 19)


# 4. TUPLE OF: Convert all strings to uppercase
words = ['data', 'science', 'python', 'rocks']
upper_words = ()
for word in words:
    upper_words += (word.upper(),)
print("4. Uppercase Tuple:", upper_words)
# Output: ('DATA', 'SCIENCE', 'PYTHON', 'ROCKS')


# 5. TUPLE OF: Remove spaces from a list of strings
messy_strings = ['  hello ', ' world', 'python ', ' is ', ' awesome  ']
cleaned = ()
for s in messy_strings:
    cleaned += (s.strip(),)
print("5. Cleaned Tuple:", cleaned)
# Output: ('hello', 'world', 'python', 'is', 'awesome')
