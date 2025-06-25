# Day 12: Understanding `self` Keyword in Python

# What is `self`?
# In Python, `self` represents the current instance of the class.
# It is used to access variables and methods that belong to the object.
# `self` must be the first parameter of instance methods in a class.
# It is automatically passed when you call a method on an object.

#  Example:

class Car:
    def __init__(self, brand, model):
        self.brand = brand      # 'self.brand' refers to the object's brand attribute
        self.model = model      # 'self.model' refers to the object's model attribute

    def show_info(self):
        # Accessing attributes using self
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating an object
car1 = Car("Toyota", "Camry")
car1.show_info()

# Output:
# Brand: Toyota, Model: Camry


# ------------------------------------------------------------
#  Problem-Solving Example: Book Info Class

#  Problem:
# Create a class `Book` with attributes: title and author.
# Use `self` to initialize and display these attributes using a method.

class Book:
    def __init__(self, title, author):
        self.title = title      # initialize title
        self.author = author    # initialize author

    def display(self):
        print(f" Title : {self.title}")
        print(f" Author: {self.author}")

#  Testing the Book class
book1 = Book("PHYSICS ", "SL.arora")
book1.display()

# Output:
#  Title : The Alchemist
#  Author: Paulo Coelho



#Functions : functions that are defined outside the class
#methods :  functions that are inside the class

# L=[1,2,3] List
# len(L)        Function
# L.append(4)   Method
# L.pop()       Method

