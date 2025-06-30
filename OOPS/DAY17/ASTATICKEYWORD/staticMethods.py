# Day 17: Static Variables (Private) and Static Methods in Python

print("1. Creating Student Class with Private Static Variable")

class Student:

    # Private static (class) variable
    __school_name = "ABC Public School"  # This is private: __school_name
    counter = 1  # Public static variable to track student count

    def __init__(self, name):
        self.name = name
        self.roll = Student.counter
        Student.counter += 1

    def show(self):
        print(f"Roll No: {self.roll}, Name: {self.name}, School: {Student.__school_name}")

    # Static Getter Method (no self or cls)
    @staticmethod
    def get_schoolname():
        return Student.__school_name

    # Static Setter Method
    @staticmethod
    def set_schoolname(name):
        Student.__school_name = name
        return Student.__school_name

# ---------------------------
print("\n2. Using static methods for utility tasks")

# Accessing private static variable via static method
print("School Name (via static method):", Student.get_schoolname())

# Creating objects
s1 = Student("Arjun")
s2 = Student("Kiran")

s1.show()
s2.show()

# Modifying private static variable via static setter
print("\n3. Modifying private static variable using static setter")
Student.set_schoolname("XYZ Global School")

s1.show()
s2.show()

# Verifying that school name is updated for all instances
print("\n4. Getting school name after update:")
print(Student.get_schoolname())
