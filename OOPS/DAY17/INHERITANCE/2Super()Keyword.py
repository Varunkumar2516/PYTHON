#==============================
#          DAY 17
#        INHERITANCE     
#        Super()     
#==============================

"""
1. WHen THE CHild CLass dont have the constructor( __Init__())
then on that case the Parent class constructor RUns Automatically 

2. but when the Child class have its own constructor (__init__())
then in this case the Child class constructor Overrides the Parent COnstructor and child Constructor runs 
"But main point":: The parent class Does not Constructor not runs 
THis does not creates the varaibles that are initilaized in Parent Constuctor
"""

class Parent:
    def __init__(self):
        self.myvar=0
        print("Parent init")

class Child(Parent):
    def __init__(self):
        print("Child init")

c = Child() #ONly Child CLass COnstructor will runs 
# print(c.myvar) #this code gives error because myvar is never created
#parent Init Not Printed


# SO here Problem OCcurs what if we Intialized (created), instance variables (attributes )of parent class in parent constructor 
# ,so it never be created ,we cannot access them from the child class
# To overcome this situation:: we USe inside the child constuctor extra line given below
# To Call Both Constructors we use  super().__init__()


print("\n\n super() ")
class BASE:
    def __init__(self):
        print("Parent init")

class CHILD(Parent):
    def __init__(self):
        super().__init__() #calls the parent CLass Method
        print("Child init")

C=CHILD()
