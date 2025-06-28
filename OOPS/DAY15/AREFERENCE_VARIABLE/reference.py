#===============================================================
# Day 15: Reference Variables in Python & Introduction to OOP
#======================================================================
# 1. Creating a class
print("1. Creating the Person class")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

# 2. Creating an object and understanding reference variable
print("\n2. Creating an object and assigning to reference variable 'p'")
p = Person("Alice")  # 'p' is NOT the object, it's a reference to the object Created by person() in memory
#suppose we dont assign the p= then we dont get the acccess to our object for further use 
#so to use our object againn we use the Refernce Variable


p.greet()  # Output: Hello, I am Alice

# 3. Using id() to show that 'p' refers to the memory address of the object
print("\n3. Checking the memory address of the object referenced by 'p'")
print("Memory address of object:", id(p))

# 4. Multiple reference variables pointing to the same object
print("\n4. Creating multiple reference variables: q = p, r = p")
q = p  # q now refers to the same object as p
r = p  # r also refers to the same object

print("Memory address of q:", id(q))
print("Memory address of r:", id(r))

# 5. Modifying object using one reference variable
print("\n5. Modifying the object through 'q'")
q.name = "Bob"

# All references reflect the change, since they point to the same object
print("p.greet(): ", end=''); p.greet()  # Output: Hello, I am Bob
print("r.greet(): ", end=''); r.greet()  # Output: Hello, I am Bob

# 6.  pass-by-reference behavior with functions
print("\n6. Passing object to a function (pass by reference)")

def change_name(personobj):
    personobj.name = "Charlie"
    p2=Person("varun")
    return p2

l=change_name(p)

# All references see the updated name
print("p.greet(): ", end='')
p.greet()  # Output: Hello, I am Charlie
print("q.greet(): ", end='')
q.greet()  # Output: Hello, I am Charlie
print("r.greet(): ", end='')
r.greet()  # Output: Hello, I am Charlie
print("l.greet(): ",end='')
l.greet()
# 7. Summary comment
print("\n7. Summary:")
print("""
- In Python, variables like 'p', 'q', and 'r' are reference variables.
- They do not *contain* the object, but point to the memory location where the object is stored.
- Assigning one variable to another does NOT create a new object — it just copies the reference.
- When passed into functions, objects are passed by reference, so changes inside the function affect the original object.
""")
