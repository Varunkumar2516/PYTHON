#================================
# Day 15: Encapsulation in Python
#================================

# 1. What is Encapsulation?
# Encapsulation means wrapping data and methods into a single unit (class).
# It restricts direct access to some components to protect the integrity of the data.
# Encapsulation is the concept of hiding the internal attributes of an object
# and exposing only controlled access using methods like getters and setters.


# 2. Creating a Person class with different access levels
print("2. Creating Person class with public, protected, and private variables")

class Person:
    def __init__(self, name, age):
        self.name = name           # Public
        self._age = age            # Protected (by convention)
        self.__salary = 50000      # Private (name mangled)

    def show_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")

# 3. Creating an object
print("\n3. Creating an object of Person class")
p = Person("Alice", 30)

# Accessing public variable
print("\n4. Accessing public variable")
print("Name:", p.name)  # Works fine

# Accessing protected variable
print("\n5. Accessing protected variable")
print("Age (protected):", p._age)  # Works, but should be accessed carefully

# Accessing private variable directly
print("\n6. Trying to access private variable directly")
p.__salary=35000
print(p.__salary)  # This will print the just setted value because it creates the new 
#varible of name __salary inside the class but not change the private member 


# To access it outside  we require the _classname__privatevariable
print(p._Person__salary) #this will print the actual value of private Members



# Accessing private variable using getter
print("\n7. Accessing private variable using getter")
print("Salary:", p.get_salary())

# Modifying private variable using setter
print("\n8. Modifying private variable using setter")
p.set_salary(60000)
print("Updated Salary:", p.get_salary())

# Trying to set invalid salary
print("\n9. Trying to set invalid salary")
p.set_salary(-1000)  # Should not allow

# 10. Name mangling trick (not recommended in practice)
print("\n10. Accessing private variable using name mangling (not recommended)")
print("Salary using name mangling:", p._Person__salary)

"""
- Public: Accessible from anywhere (e.g., self.name)
- Protected (_var): Accessible but meant to be used within class/subclass
- Private (__var): Not accessible directly from outside class
- Use getters and setters to safely access and modify private data
- Encapsulation helps hide internal state and protect object integrity
"""
