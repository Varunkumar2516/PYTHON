# ===============================
#        DAY 13 - Magic Methods
# ===============================

# A sample class to use common magic (dunder) methods

class Book:
    # 1.__init__ is a constructor: used to initialize object attributes
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # 2.__str__ is called when we print the object
    def __str__(self):
        return f"📘 Book Title: {self.title}, Pages: {self.pages}"

    # 3.__len__ is called when we use len() on the object
    def __len__(self):
        return self.pages

    # 4.__add__ allows using + between two objects
    def __add__(self, other):
        return self.pages + other.pages

    # 5.__eq__ allows comparison using ==
    def __eq__(self, other):

        return self.pages == other.pages

    # 6.__lt__ allows comparison using <
    def __lt__(self, other):
        return self.pages < other.pages

    # 7.__gt__ allows comparison using >
    def __gt__(self, other):
        return self.pages > other.pages

    # 8.__repr__ gives an official string representation (for developers)
    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    # 9. __del__ is a destructor: called when object is deleted
    def __del__(self):
        print(f"🗑️ Book '{self.title}' is deleted from memory")


# Creating objects
#__init__ using it for intialization
book1 = Book("Python Basics", 300)
book2 = Book("OOP Mastery", 250)

# __str__
print("\n __str__")
print(book1)  #  Book Title: Python Basics, Pages: 300
print(book2)  #  Book Title: OOP Mastery, Pages: 250

# __len__
print("\n\n __len__")
print("Total pages in book1:", len(book1))  # 300
print("Total pages in book1:", len(book2))  # 300

# __add__
print("\n\n __add__")
total_pages = book1 + book2
print("Combined pages of both books:", total_pages)  # 550

# __eq__
print("\n\n__eq__  ==")
print("Are both books of equal length?", book1 == book2)  # False
 # False

# __lt__ and __gt__
print("\n\n  __lt__ (<) and __gt__ (>)")
print("Is book1 shorter than book2?", book1 < book2)  # False
print("Is book1 longer than book2?", book1 > book2)  # True

# __repr__
print("\n\n __repr__")
print("Developer view:", repr(book1))  # Book('Python Basics', 300)

# __del__
print("\n\n __del__")
del book2  # Calls __del__ and prints a message
print("\n")
del book1

##Even we write del or not it is a destructor it will automatically called when the program ends