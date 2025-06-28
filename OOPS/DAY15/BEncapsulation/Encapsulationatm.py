# Day 15: Encapsulation in Python

# 1. What is Encapsulation?
print("1. Encapsulation is the concept of hiding the internal state (attributes) of an object")
print("   and exposing only controlled access using methods like getters and setters.\n")

# 2. Defining a class with private attribute and public methods (getter and setter)
print("2. Creating a class with private variable and using getter/setter methods")

class ATM:
    def __init__(self, owner, balance):
        self.owner = owner          # Public variable
        self.__balance = balance    # Private variable using double underscore

    # Getter method (to view private data)
    def get_balance(self):
        return self.__balance

    # Setter method (to safely update private data)
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount! Cannot set negative balance.")

    # Method to display account info
    def display_account(self):
        print(f"Owner: {self.owner}, Balance: {self.__balance}")

# 3. Creating an object of ATM
print("\n3. Creating a ATM object")
acc = ATM("Alice", 1000)

# 4. Accessing public attribute
print("\n4. Accessing public attribute (owner)")
print("Owner:", acc.owner)

# 5. Accessing private attribute directly (should fail)
print("\n5. Trying to access private attribute directly")
try:
    print("Balance:", acc.__balance)
except AttributeError:
    print("Cannot access __balance directly (AttributeError)")

# 6. Accessing private attribute via getter method
print("\n6. Accessing private attribute using getter")
print("Balance:", acc.get_balance())

# 7. Modifying private attribute via setter method
print("\n7. Modifying private attribute using setter")
acc.set_balance(1500)
print("Updated Balance:", acc.get_balance())

# 8. Trying to set an invalid value
print("\n8. Trying to set negative balance (invalid)")
acc.set_balance(-500)  # Should not update
"""
- Encapsulation = attributes (data) + methods (functions) bundled in a class
- Keep sensitive data private using __double_underscore
- Provide access through public methods: getter (to read), setter (to update)
- Protects the internal state of the object from accidental or unauthorized changes
"""
