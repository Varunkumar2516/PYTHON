#=====================================
#     DAY 12 Classes and Objects
#=====================================

#CLass Syntax
"""
class class_name:
    Class Varibles` or Class Attributes
    class methods `or class methods

    """

#Object synax
"""
Object_name=classname()
"""

#example::
# Defining a class (blueprint)
class Person:

    name ="default"
    age =18

    # Method (function) inside the class
    #self ,It is used to access variables and methods that belong to the object.or we can say declared in class
    def introduce(self,myname,myage):
        self.name=myname
        self.age=myage
    def print(self):
        print(f"Name :{self.name} Age: {self.age}")

# Creating an object (instance of the class)
person1 = Person()

# Calling the method using the object
person1.introduce("varun",18)
person1.print()


