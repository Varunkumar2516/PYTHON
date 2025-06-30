#==============================
#          DAY 18
#       POLY-MORPHISM          
#==============================

"""
Polymorphism::
Polymorphism means "many forms".
when a single Thing exist in more than one forms it becomes the Polymorphism
Polymorphism is ability to take make than one form.
it allows Operator,Functions,and objects to behave in Multiple Ways
It helps write flexible and reusable code by using a common interface for different data types or classes.
"""

"""
Two Types of Polymorphism
1.Compile TIme Polymorphism (static)
      a. Method overloading 
      b. Operator Overloading

2.Run TIme Polymorphism (Dynamic)
      a. Method Overriding
      """



#1.Compile TIme Polymorphism (static)
 #     a. Method overloading 
 #     b. Operator Overloading

 #a.Method Overloading means having multiple methods with the same name but different parameters (number or type) within the same class.
#In many languages like Java or C++, this is allowed directly.
#But in Python...
#Python does NOT support method overloading directly.
#If you define multiple methods with the same name, only the last one is kept.

class Greet:
    def hello(self):
        print("Hello")

    def hello(self, name):  # Overrides previous hello()
        print(f"Hello, {name}")

g = Greet()
g.hello("Alice")  # Works
# g.hello()         #  Error: missing 1 required argument


 #b .Operator Overloading :Same  operator, different behavior depending on the type
print("\n# Polymorphism with '+' operator")
print(2 + 3)         # 5 (integers)
print("Hello " + "World")  # Hello World (strings)
print([1, 2] + [3, 4])     # [1, 2, 3, 4] (lists)

#Same + operator, different behavior depending on the type — this is also polymorphism




#2.Run TIme Polymorphism (Dynamic)
 #     a. Method Overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism in action
def animal_sound(animal):
    animal.speak()

a = Animal()
d = Dog()
c = Cat()

print("\n# Polymorphism with method overriding")
animal_sound(a)  # Animal makes a sound
animal_sound(d)  # Dog barks
animal_sound(c)  # Cat meows
