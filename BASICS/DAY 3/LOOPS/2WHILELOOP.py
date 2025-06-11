#********************************#
#            DAY 3            #
#         WHILE LOOP IN PYTHON #
#********************************#
"""BASIC SYNTAX:
While condition:
if condition true the while body runs and it stops only when condition false
"""
num = int(input("Enter the number (n): "))

# Program 1: Print numbers from 1 to n
print("\n1. Numbers from 1 to n:")
i = 1
while i <= num:
    print(i, end=' ')
    i += 1
print()

# Program 2: Print odd numbers from 1 to n
print("\n2. Odd numbers from 1 to n:")
i = 1
while i <= num:
    print(i, end=' ')
    i += 2
print()

# Program 3: Print even numbers from 1 to n
print("\n3. Even numbers from 1 to n:")
i = 2
while i <= num:
    print(i, end=' ')
    i += 2
print()

# Program 4: Factorial of n
print("\n4. Factorial of the number:")
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} is {fact}")

# Program 5: Sum of numbers from 1 to n
print("\n5. Sum of numbers from 1 to n:")
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print(f"Sum of numbers from 1 to {num} is {total}")

# Program 6: Reverse the number (as string)
print("\n6. Reverse of the number:")
n_str = str(num)
i = 0
rev = ''
while i < len(n_str):
    rev = n_str[i] + rev
    i += 1
print(f"Reverse of {num} is {rev}")

# Program 7: Multiplication table of the number
print(f"\n7. Multiplication table of {num}:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
