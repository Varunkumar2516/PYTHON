# ===================================================
# 1. Single Inheritance
#  One child class inherits from one parent class
# ===================================================

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

print("\n#1 Single Inheritance")
d = Dog()
d.speak()
d.bark()

# ===================================================
# 2. Multiple Inheritance
#  A class inherits from more than one parent class
# more than one parent class gets inherited by single child
# Not works in Java 
# ===================================================

class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

print("\n#2 Multiple Inheritance")
duck = Duck()
duck.fly()
duck.swim()
duck.quack()

# ===================================================
#  3. Multilevel Inheritance
# Inheritance in a chain: A → B → C
# ===================================================

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class ElectricCar(Car):
    def battery(self):
        print("Electric car uses battery")

print("\n#3 Multilevel Inheritance")
car = ElectricCar()
car.battery() #child class method
car.wheels()  #parent class method
car.move()    #grand parent class method

# ===================================================
# 4. Hierarchical Inheritance
#  Multiple child classes inherit from one parent
# ===================================================

class Parent:
    def show(self):
        print("This is the parent class")

class ChildA(Parent):
    def feature_a(self):
        print("Feature A")

class ChildB(Parent):
    def feature_b(self):
        print("Feature B")

print("\n#4 Hierarchical Inheritance")
a = ChildA()
b = ChildB()
a.show()
a.feature_a()
b.show()
b.feature_b()

# ===================================================
# 5. Hybrid Inheritance
#  Combination of multiple types of inheritance
# ===================================================

class Human:
    def speak(self):
        print("Human speaks")

class Male(Human):
    def gender(self):
        print("Gender: Male")

class Employee:
    def work(self):
        print("Employee works")

class Engineer(Male, Employee):
    def field(self):
        print("Field: Engineering")

print("\n#5 Hybrid Inheritance")
eng = Engineer()
eng.speak()
eng.gender()
eng.work()
eng.field()
