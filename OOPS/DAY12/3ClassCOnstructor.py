#  Day 12: Constructor of Class in Python

#  What is a Constructor?
# In Python, the constructor method is called Magic Method __init__()
# It is a special method that is automatically called when an object is created.
# The main purpose of __init__ is to initialize the attributes of the object.

#  Syntax of Constructor:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = parameters

#  Example:

class Student:
    def __init__(self, name, roll_no):
        self.name = name        # initializing instance variable name
        self.roll_no = roll_no  # initializing instance variable roll_no

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number : {self.roll_no}")


# 🎯 Creating an object (which automatically calls __init__)
student1 = Student("Alice", 101)
student1.display_info()

# Output:
# Student Name: Alice
# Roll Number : 101


# ------------------------------------------------------------
# 🧠 Problem-Solving Example: Circle Area Calculator

# 🎯 Problem:
# Create a class `Circle` with a constructor that takes radius as input.
# Include a method `area()` that returns the area of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius  # initialize radius

    def area(self):
        return 3.14159 * self.radius * self.radius


# 🔍 Testing the Circle class
circle1 = Circle(5)
print(f"\nArea of Circle with radius 5: {circle1.area()}")

# Output:
# Area of Circle with radius 5: 78.53975

