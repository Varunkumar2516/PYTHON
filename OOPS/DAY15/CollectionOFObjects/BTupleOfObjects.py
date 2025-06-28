# Day 15: Collection of Objects in Python
#tuple of Objects


print("1. Creating the Student CLass")
#Student CLass 
class Student:
    def __init__(self,name,age,Class):
        self.__name=name
        self.__age=age
        self.__Class=Class
    
    #creating the Str function to  print (object)
    def __str__(self):
       return f"""Student : 
              Name  : {self.__name}
              Age   : {self.__age} 
              Class : {self.__Class}"""
    
# 2. Create multiple Student objects
print("\n2. Creating multiple Student objects")

s1 = Student("ekam", 13,"9th")
s2 = Student("suraj", 17,'12th')
s3 = Student("rishab", 19,"UG")

# 3. Store objects in a list (collection)
print("\n3. Storing all students in a TUple")

students = (s1,s2,s3)

# 4. Iterate through the collection and access each object
print("\n4. Iterating through the Tuple and calling methods")

for student in students:
    print(student)


# 5. Accessing a specific object and its attributes
print("\n5. Accessing a specific object from the TUple")
print("Second Student:", students[1])


# 6. Creating and managing a list of objects dynamically
print("\n6. taking Inputs from user Creating objects dynamically using a loop")

i=1
mytuple=()
while True:
    print("Student ",i)  
    i=i+1
    #Taking data from user
    name=input("Enter the name :")
    age=int(input("Enter the age"))
    Class=input("Enter the CLass")
    p=Student(name,age,Class)
    mytuple=mytuple+(p,)
    repeat=input("Yes/No")
    if repeat.lower()=='no':
        break

print("Print With Repr")
print(mytuple)    #it uses the __repr__ function for printing the Tuple values not the object itself
#print the Tuple
#to print it more better we use the 
print("Print with the str")
for i in mytuple:
    print(i)

