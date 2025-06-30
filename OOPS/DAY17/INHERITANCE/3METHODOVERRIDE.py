#
##==============================
#          DAY 17
#        INHERITANCE     
#          MEthod Overriding   
#==============================

"""

MEthod Overriding ::Method overriding happens when a child class defines a method with
 the same name as a method in its parent class.
 The child class method replaces (overrides) the parent class method when called on a child instance.

 """


class Person:
    def show_role(self):
        print("I am a person")

class Teacher(Person):
    #same name function Overrides
    def show_role(self):
        print("I am a teacher")

class Student(Person):

    #same name function Overrides
    def show_role(self):
        print("I am a student")

p = Person()
t = Teacher()
s = Student()

p.show_role()  # I am a person
t.show_role()  # I am a teacher
s.show_role()  # I am a student



print('\n\nsuper() for parent version')
#to call the Parent Method also we can use the super() keyword
class Person:
    def show_role(self):
        print("I am a person")

class Teacher(Person):
    #same name function Overrides
    def show_role(self):
        print("I am a teacher",end=' ')
        #this calls the Parent method
        super().show_role()

class Student(Person):

    #same name function Overrides
    def show_role(self):
        print("I am a student",end=' ')
        #this calls the Parent method
        super().show_role()

p = Person()
t = Teacher()
s = Student()

p.show_role()  # I am a person
t.show_role()  # I am a teacher
s.show_role()  # I am a student