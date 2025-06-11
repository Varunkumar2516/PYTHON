# Program 2: Python Operators Example

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print("Addition (a + b):", a + b)          # Addition
print("Subtraction (a - b):", a - b)       # Subtraction
print("Multiplication (a * b):", a * b)    # Multiplication
print("Division (a / b):", a / b)          # Division (float)
print("Floor Division (a // b):", a // b)  # Floor Division
print("Modulus (a % b):", a % b)           # Modulus
print("Exponentiation (a ** b):", a ** b)  # Exponentiation

print("\nComparison Operators:")
# Comparison Operators (Result is Boolean)
print("Equal (a == b):", a == b)           # Equal
print("Not Equal (a != b):", a != b)       # Not Equal
print("Greater Than (a > b):", a > b)      # Greater Than
print("Less Than (a < b):", a < b)         # Less Than
print("Greater Than or Equal (a >= b):", a >= b)  # Greater Than or Equal
print("Less Than or Equal (a <= b):", a <= b)      # Less Than or Equal

print("\nLogical Operators:")
x = True
y = False
print("AND (x and y):", x and y)           # Logical AND
print("OR (x or y):", x or y)              # Logical OR
print("NOT (not x):", not x)               # Logical NOT

print("\nBitwise Operators:")
print("Bitwise AND (a & b):", a & b)       # Bitwise AND
print("Bitwise OR (a | b):", a | b)        # Bitwise OR
print("Bitwise XOR (a ^ b):", a ^ b)       # Bitwise XOR
print("Bitwise NOT (~a):", ~a)             # Bitwise NOT
print("Left Shift (a << 1):", a << 1)      # Left Shift
print("Right Shift (a >> 1):", a >> 1)     # Right Shift

print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c)
c += 2
print("c += 2:", c)  # c = c + 2
c -= 1
print("c -= 1:", c)  # c = c - 1
c *= 3
print("c *= 3:", c)  # c = c * 3
c /= 2
print("c /= 2:", c)  # c = c / 2
c %= 3
print("c %= 3:", c)  # c = c % 3
c **= 2
print("c **= 2:", c)  # c = c ** 2
c //= 2
print("c //= 2:", c)  # c = c // 2

print("\nIdentity Operators:")
print("a is b:", a is b)                   # Identity (is)
print("a is not b:", a is not b)           # Identity (is not)

print("\nMembership Operators:")
list1 = [1, 2, 3, 4, 5]
print("2 in list1:", 2 in list1)           # Membership (in)
print("10 not in list1:", 10 not in list1) # Membership (not in)
