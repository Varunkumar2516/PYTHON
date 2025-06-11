#********************************#
#            DAY 3               #
#         FOR LOOP IN PYTHON     #
#********************************#

"""
Syntax:
- Default step of 1:
    for variable in range(start, end):
- With custom step (e.g., step = 2):
    for variable in range(start, end, step)
"""

# ===============================
# PRACTICE PROGRAMS WITH FOR LOOP
# ===============================

num = int(input("Enter the number (n): "))

# Program 1: Print numbers from 1 to n
print("\n1. Numbers from 1 to n:")
for i in range(1, num + 1):
    print(i, end=' ')
print()

# Program 2: Print odd numbers from 1 to n
print("\n2. Odd numbers from 1 to n:")
for i in range(1, num + 1, 2):
    print(i, end=' ')
print()

# Program 3: Print even numbers from 1 to n
print("\n3. Even numbers from 1 to n:")
for i in range(2, num + 1, 2):
    print(i, end=' ')
print()

# Program 4: Factorial of n
print("\n4. Factorial of the number:")
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")

# Program 5: Sum of numbers from 1 to n
print("\n5. Sum of numbers from 1 to n:")
total = 0
for i in range(1, num + 1):
    total += i
print(f"Sum of numbers from 1 to {num} is {total}")

# Program 6: Reverse the number (using string)
print("\n6. Reverse of the number:")
rev = ''
for digit in str(num):
    rev = digit + rev
print(f"Reverse of {num} is {rev}")

# Program 7: Multiplication table of the number
print(f"\n7. Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
