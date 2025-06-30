# Day 17: Static Variables
#Static variable is variable of class that is shared with all the objects and itsvalue is not the object dependent 
#it is totally object independent , it has same copy for all the objects of the class
#it is declared inside the class but outside the methods of the class

print("1. Creating a class with a static (class) variable")

class Student:

    # Static/class variable As Private
    __school_name = "ABC Public School" #private static member
    counter=1

    # only method that cannot havethe self For Static variables 
    #it does not require any object to call but it need the (class name) classname.getschool() etc.
    #utility Functions
    @staticmethod
    def get_schoolname():
        return Student.__school_name
    @staticmethod
    def set__schoolname(name):
        Student.__school_name=name
        return Student.__school_name
    


    def __init__(self, name):
        self.name = name
        #instance variable
        self.school=Student.__school_name
        self.count=Student.counter
        Student.counter+=1
    def show(self):
        print(f"Name: {self.name}, School: {self.__school_name} \n Total Objects:{self.count}")

print("\n2. Creating multiple objects sharing the same class variable")

s1 = Student("Arjun")
s2 = Student("Kiran")

s1.show()
s2.show()

print("\n3. Changing the static variable")
Student.__school_name = "XYZ International"
#here we generally create the new variable not change that one
s1.show()
s2.show()

print("\n Student._Student__school_name TO access the real static member")
#same as we have intialized
print(Student._Student__school_name)

print("\n4. Adding an instance variable with the same name (overrides class var for that object)")
s1.__school_name = "Private School"
print(f"s1's __school_name: {s1.__school_name}")     # instance variable
print(f"s2's __school_name: {s2.__school_name}")     # class variable
print(f"Student.__school_name: {Student.__school_name}")
print(f"Student._Student__school_name:",Student._Student__school_name)


print("\n5. Calling set and get function for the StaticPrivate members")
print("Student.get_schoolname() :",Student.get_schoolname())
print("Student.set__schoolname(DAVIET) :",Student.set__schoolname("DAVIET"))
print("Student.get_schoolname() :",Student.get_schoolname())
