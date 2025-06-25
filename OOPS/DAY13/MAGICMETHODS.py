#==================================
#           DAY 13
#           OOPS PART 2 
#          MAGIC METHODS      
#=+================================

#MAGIC METHOD::magic methods (also called dunder methods, because they start and end with double underscores like __init__) 

#  Example:

class Student:
    #1 def  __init__:
# In Python,   __init__() :constructor of Class
# It is a special method that is automatically called when an object is created.
# The main purpose of __init__ is to initialize the attributes of the object.

#  Syntax of Constructor:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = parameters

    def __init__(self, name,age, roll_no):
        self.name = name        # initializing instance variable name
        self.age =age   # initializing instance variable roll_no
        self.roll_no = roll_no  # initializing instance variable roll_no
        

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll Number : {self.roll_no}")
 
obj=Student("varun",18,2301705)
obj.display_info()

obj=Student("",18,2301705)
obj.display_info()
