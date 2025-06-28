# Day 15: OOP Concepts - Practice Questions and Solutions

# Question 1: Reference Variable vs Object
print("\n1. Reference Variable vs Object")
class Demo:
    def __init__(self):
        self.value = 100

obj1 = Demo()
obj2 = obj1  # obj2 is a reference to obj1
obj2.value = 200
print("obj1.value:", obj1.value)  # 200, because obj1 and obj2 refer to the same object


# Question 2: How many objects are created?
print("\n2. Single object, multiple references")
p1 = Demo()
p2 = p1
print("Memory IDs:", id(p1), id(p2))  # Same IDs and single object


# Question 3: del keyword
print("\n3. Using del on one reference")
p3 = Demo()
p4 = p3
del p3
print("p4.value:", p4.value)  # Still accessible delonly delete the p3 reference to the object


# Question 4: Access specifier
print("\n4. Accessing private variable directly")
class Student:
    def __init__(self):
        self.__name = "John"

    def get_name(self):
        return self.__name

s = Student()
# print(s.__name)  # Error
print("Access via getter:", s.get_name())


# Question 5: Employee class with getter and setter
print("\n5. Employee with getter and setter")
class Employee:
    def __init__(self, id, salary):
        self.__id = id
        self.__salary = salary

    def get_id(self): return self.__id
    def get_salary(self): return self.__salary
    def set_salary(self, salary): self.__salary = salary

e = Employee(1, 50000)
print("Before Update:", e.get_salary())
e.set_salary(55000)
print("After Update:", e.get_salary())


# : Why we use private?
# - To protect internal data, enforce validation, encapsulate logic.


#  _var vs __var
# _var = protected, __var = private (name mangling)


# Question 6: __str__ vs __repr__
print("\n6. str vs repr")
class A:
    def __str__(self): return "STR A"
    def __repr__(self): return "REPR A"
a = A()
print(a)  # STR A
print([a])  # [REPR A]


# Question 7: __eq__ override
print("\n7. __eq__ always returns True")
class A:
    def __eq__(self, other): return True

a1 = A()
a2 = A()
print(a1 == a2)  # True


#  __hash__ with __eq__
# To use objects in set/dict, __hash__ must align with __eq__ when the hash index is sane for more objects it python checks from the eq 



# Question 8: Book class
print("\n8. Book class with eq and hash")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author)) #this takes the single inputto hash (self.title, self.author) and provide the integer 
    #if this integer is same for two objects ,then python checks to the __eq__ method if the return True :: itmeans that the objects are same 
    #hence it does not add to the data structure

    def __str__(self):
        return f"{self.title} by {self.author}"

b1 = Book("Python", "X")
b2 = Book("Python", "X")
b3 = Book("Java", "Y")
books = {b1, b2, b3}   #this is called the Set of Objects 
for b in books:
    print(b)  # Only 2 unique books
#  Set stores unique objects only if __eq__ and __hash__ match



# Differences
# list = dynamic, allows duplicates, mutable
# tuple = immutable, fixed size
# set = unordered, no duplicates, requires hash


# Question 9: Input and tuple
print("\n9. Input and convert list to tuple")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

students_list = []
for i in range(2):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    students_list.append(Student(name, age))

tuple_students = tuple(students_list)
for s in tuple_students:
    print(s)





#  True/False
# .append() on tuple: NOOOO
# Objects passed by reference: YESSS
# Tuples can hold mutable objects: YESSSSS 


# Question 10: Account class
print("\n10. Account class")
class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def deposit(self, amt): self.__balance += amt
    def withdraw(self, amt): self.__balance -= amt
    def __str__(self): return f"{self.__name}: Rs. {self.__balance}"

accs = [Account("Ram", 1000), Account("Shyam", 500)]
accs[0].deposit(500)
accs[1].withdraw(200)
for acc in accs:
    print(acc)


# Question 11: Car class and set
print("\n11. Car class with set")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __eq__(self, other):
        return (self.make, self.model, self.year) == (other.make, other.model, other.year)

    def __hash__(self):
        return hash((self.make, self.model, self.year))

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

cars = set()
cars.add(Car("Toyota", "Camry", 2020))
cars.add(Car("Toyota", "Camry", 2020))  # Duplicate
cars.add(Car("Honda", "Civic", 2022))
for c in cars:
    print(c)


# Question 12: School simulation
print("\n12. School simulation")
class Subject:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, subject, teacher):
        self.name = name
        self.subject = subject  # reference to Subject
        self.teacher = teacher  # reference to Teacher

    def __str__(self):
        return f"{self.name} studies {self.subject.name} with {self.teacher.name}"

math = Subject("Math")
mr_kumar = Teacher("Mr. Kumar")
raj = Student("Raj", math, mr_kumar)
print(raj)
