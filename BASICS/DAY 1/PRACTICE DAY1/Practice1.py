#PRACTIC_SECTION1
# 01_basic_io.
# 02_swap_numbers.
# 03_float_to_int.
# 04_student_info.
# 05_eval_expression.


# ============================
# Program 1: Basic Input/Output take 
# input from user and display it to user
# ============================
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

print(f"""NAME: {name}
AGE: {age}
ADDRESS: {address}
""")

# ============================
# Program 2: Swap Two Numbers 
#take input from user and then swap them
# ============================
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Before Swap: a = {a}, b = {b}")

# Swapping
a, b = b, a
print(f"After Swap: a = {a}, b = {b}")

# ============================
# Program 3: Float to Integer Conversion
# ============================
num = float(input("Enter a floating-point number: "))
num = int(num)  # Typecasting float to int (truncates decimals)
print("Integer part:", num)

# ============================
# Program 4: Student Info Formatter
# ============================
name = input("Enter the student's name: ")
grade = input("Enter the student's grade: ")
age = int(input("Enter the student's age: "))
email = input("Enter the student's email: ")
phoneno = int(input("Enter the student's phone number: "))

#using f-string to print variables and """ """(triple codes) for multiple lines
print(f"""
Name     : {name}
Grade    : {grade}
Age      : {age}
Email    : {email}
Phone No.: {phoneno}
""")

# ============================
# Program 5: Evaluate an Expression (eval)
# ============================
# WARNING: eval() executes user input as code.
# Use only in trusted environments or for safe expressions.
var = eval(input("Enter a Python expression (e.g., 2+3*5): "))
print("Result:", var)
