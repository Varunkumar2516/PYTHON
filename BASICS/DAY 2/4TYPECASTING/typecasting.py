# Program 4: Type Casting in Python : Conversion of one data type to another
# This program provides two types of type casting in Python:
# 1. Implicit Type Casting 
# 2. Explicit Type Casting

# 1. Implicit Type Casting
# Python automatically converts one data type to another when needed

print("Implicit Type Casting:")
a = 5       # int
b = 2.5     # float

result = a + b  # int is automatically converted to float
print("a (int) + b (float) =", result)  # Output will be float
print("Type of result:", type(result))  # <class 'float'>

# 2. Explicit Type Casting
# Manually converting one data type to another using functions like int(), float(), str(), etc.

print("\nExplicit Type Casting:")

x = 10      # int
y = "25"    # str

# Convert string to integer
y_int = int(y) # using the explicit typecasting
sum_result = x + y_int
print("x (int) + y (str converted to int) =", sum_result)
print("Type of y_int:", type(y_int))  # <class 'int'>

# Convert integer to string
x_str = str(x)
combined_str = x_str + y
print("x (int converted to str) + y (str) =", combined_str)
print("Type of x_str:", type(x_str))  # <class 'str'>
  