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

"""
So How to Do It in Python?
We simulate method overloading using:
1.Default arguments
2.Variable-length arguments (*args, **kwargs)
3.Type checking 
"""

print("1. Default Arguments")
class Shape:
    def Area(self,a=0,b=0):
        if b==0:
            return f'Square Area :{a*a} Units'
        else:
            return f'Rectangle Area :{a*b} Units'

A=Shape()
print(A.Area())  #0
print(A.Area(5))  #25
print(A.Area(5,6))  #30


print("2. Using *args and *kwargs")

class Shape:
    def Area(self,*args):
        if len(args)==0:
            return 0
        elif len(args)==1:
            return f"Square Area:{args[0]*args[0]}"
        if len(args)==2:
            return f"Rectangle Area :{args[0] *args[1]}"
        if len(args)==3:
            a,b,c=map(int,args)
            return f"Cuboid Area:{2 * (a* b + b * c+ a * c)}"
        else:
            return "try again broo sorryy~~~"
A=Shape()
print(A.Area())  #0
print(A.Area(5))  #25
print(A.Area(5,6))  #30
print(A.Area(5,6,7))  


print("\n3.Type Checking")
class Shape:
    def area(self, a=None, b=None):
        if a is not None and b is not None:
            return a * b  # rectangle
        elif a is not None:
            return a*a
        else:
            return 0

s = Shape()
print(s.area())        # 0
print(s.area(5))       # 25 (Square)
print(s.area(4, 6))    # 24 (rectangle)
