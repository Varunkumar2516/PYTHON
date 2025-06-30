#-=============================
#        DIAMOND PROBLEM
#------------------------------

"""
The Diamond Problem occurs when a class inherits from two 
classes that both inherit from a common parent class.
The inheritance structure looks like a diamond:
      A
     / \
    B   C
     \ /
      D
Class B and Class C both inherit from Class A.
Class D inherits from both B and C.
      
  The Problem:
If D calls a method defined in A, which path should Python follow?
D → B → A?
Or D → C → A?
This is called ambiguity in method resolution.MRO """


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.__mro__)  ##TO CHECK THE MRO ORDER
"""MRO ORDER IS D -> B -> C -> A"""
#this gives ouptut as B 
#because Python uses MRO (Method Resolution Order) — 
# it follows left-to-right order in the class declaration of D(B, C).
#so it go to first B class THat is why B class Version of the self runs



#We already know that Python prints B in D(B, C).
#So why do we need super() if Python already knows what to call?
"""
Without super():
Only the immediate class method is called.
It only calls B.show() — it ignores C and A completely.
So if C also had important logic, it gets skipped. Thats risky."""

"""With super():
You let Python follow the Method Resolution Order (MRO) and call 
ALL relevant methods, in the correct order."""

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(B,C):
    def show(self):
        print("D")
        super().show()
obj = D()
obj.show()
#Now each class's method is called! That’s the power of super().
#Calls all methods in MRO (Method resoultion order)
#MRO ==  D -> B -> C -> A
# It helps to DO classes : I’ll do my part, then pass the work up the chain.
#important in large projects