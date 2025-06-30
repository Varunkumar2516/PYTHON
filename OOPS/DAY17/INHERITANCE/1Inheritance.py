#==============================
#          DAY 17
#        INHERITANCE          
#==============================
"""
Inheritance allows a class (child class) to inherit the properties and methods
 of another class (parent class). It helps with code reusability.
 Inheritance allows us to 
   Inherit the constructor 
   Inherit the Non Private attributes
   Inherit the Non Private Methods
 """

#Example
class Base:
    def __init__(self):
        self.name="varun"
    def Basespeak(self):
        print("Im Base Class")


#to Inherit 
#Class ChildCLass(ParentCLassName):

class Child(Base):
    
    def childspeak(self):
        print("Im Child Class")


# With the CHild Class Object we can also Call the Parent class Methods
obj = Child()
obj.Basespeak()  # Inherited method
obj.childspeak()   # Child class method

print(obj.name)

