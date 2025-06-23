# ================================================
#  Creating Sets -    Practical Examples
# ================================================
# NOTE: Sets do NOT maintain order and only store UNIQUE values.
# Syntax: myset = set()
#same as the list use the .add() function instead of .append()

# -----------------------------------------------
print("\n1. SET OF: Squares of numbers from 0 to 10 ")
Squares = set()
for i in range(0, 11):
    Squares.add(i ** 2)
print(Squares)

# -----------------------------------------------
print("\n2. SET OF: Even numbers from 0 to 10 ")
Even = set()
for i in range(0, 11):
    if i % 2 == 0:
        Even.add(i)
print(Even)

# -----------------------------------------------
print("\n3. SET OF: Prime numbers from 0 to 20 ")
Primes = set()
for i in range(2, 21):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        Primes.add(i)
print(Primes)

# -----------------------------------------------
print("\n4. SET OF: Uppercase strings from another list ")
OldSet = {"apple", "banana", "cherry", "mango"}
print("Original Set:", OldSet)
UpperSet = set()
for item in OldSet:
    UpperSet.add(item.upper())
print("Uppercase Set:", UpperSet)

# -----------------------------------------------
print("\n5. SET OF: Remove spaces from strings in a set ")
RawSet = {"  1  ", "  2  ", "  3  "}
print("Raw Set with spaces:", RawSet)
CleanSet = set()
for item in RawSet:
    CleanSet.add(item.strip())
print("Cleaned Set:", CleanSet)
