#==========================
#  INSTANCE VARIABLE
#==========================
#This variable isbasically whose value is different for different Objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello {self.name} ,Your Age {self.age}")


A=Person("varun",18)
A.greet()     #self.name=varun and self.age=18

B=Person("sharma",27)  
B.greet()     #self.name=sharma and self.age=27


#hence variable are same self.name but it have different values for different objects
#they are called the Instance variable