"""PROGRAM :5 Conditional statements:conditional statements allows computer
 to execute a certain block only if the condition is true.
 TYPES OF CONDITIONAL STATEMENTS
 1.if statement
 2.if-else statement
 3.if-elif-else statement
 4.Nested statement 
 5.shorthand  if statement
"""
# 1. Simple if Statement
# Executes the block only if the condition is True
num = 10
if num > 0:
    print("1. Positive number")

# 2. if-else Statement
# Executes one block if condition is True, another if False
num = -5
if num >= 0:
    print("2. Non-negative number")
else:
    print("2. Negative number") #this block runs because condition false

# 3. if-elif-else Statement
# Checks multiple conditions in sequence
marks = 85

if marks >= 90:
    print("3. Grade: A")
elif marks >= 75:
    print("3. Grade: B") #this condition mets with given data hence this runs
elif marks >= 60:
    print("3. Grade: C")
else:
    print("3. Grade: F")

# 4. Nested if Statement
# An if inside another if
age = 20
if age >= 18:
    if age < 60:
        print("4. You are an adult.")
    else:
        print("4. You are a senior citizen.")
else:
    print("4. You are a minor.")

#5. Short hand if statement
#this statement is used when there is only one 
#statement within the if statement , we can write the statement in same line
marks=78
if marks>40 and marks <80 : print("5. Grade : A")

#6.short hand if-else statement
#this statement is used when there is only one condition to execute and if it false then else block'

marks=78
print("6. GRADE : A+") if marks>=90 else print("6. Grade : B")

#another example
num=5
print("6. NUmber is even") if num%2==0 else print("6. Number is odd")