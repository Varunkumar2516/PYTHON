# Day 15: Access Specifiers in Python

# 1. What are Access Specifiers?
print("1. Access Specifiers define how the members (variables and methods) of a class can be accessed,from outisde or inside of class.")
print("   Python supports three types: Public, Protected (_), and Private (__).\n")

# 2. Defining a class with all types of variables
print("2. Creating a class with public, protected, and private members")

class Demo:
    def __init__(self):
        self.publicvar = "I am Public"          # Public variable
        self._protectedvar = "I am Protected"   # Protected variable (by convention)
        self.__privatevar = "I am Private"      # Private variable (name mangled)

    def show_vars(self):
        print("Inside class:")
        print("Public:", self.publicvar)
        print("Protected:", self._protectedvar)
        print("Private:", self.__privatevar)

# 3. Creating an object
print("\n3. Creating an object of Demo class")
obj = Demo()
obj.show_vars()

# 4. Accessing public member
print("\n4. Accessing public member from outside class")
print("Public:", obj.publicvar)  # Allowed

# 5. Accessing protected member
print("\n5. Accessing protected member from outside class")
print("Protected:", obj._protectedvar)  # Technically allowed but discouraged

# 6. Trying to access private member directly
print("\n6. Trying to access private member directly")
obj.__privatevar="Hello im accessed from outside"
try:
    print("Not Private its the different memory location ", obj.__privatevar)
except AttributeError:
    print("Cannot access __private_var directly (AttributeError)")

# 7. Accessing private variable via name mangling (not recommended)
print("\n7. Accessing private variable using name mangling (not recommended)")
print("Private (via name mangling):", obj._Demo__privatevar)

"""
- Public (no underscore): Accessible from anywhere
- Protected (_var): Accessible but should be used within class and subclass only (convention)
- Private (__var): Not directly accessible, intended to be used only within the class
- Python does not enforce strict access control, it relies on naming conventions and developer discipline
- It can be also accessed form outside by _classname__Variablename 
- 

Python is not the fully private language 
But it is made for only adults ,so If we want that the private members can be accessed from ouside it can be....
but with fully protected way 
"""
