# Day 15: Collection of Objects in Python


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
print("\n3. Storing all students in a list")

students = [s1, s2, s3]

# 4. Iterate through the collection and access each object
print("\n4. Iterating through the list and calling methods")

for student in students:
    print(student)


# 5. Accessing a specific object and its attributes
print("\n5. Accessing a specific object from the list")
print("Second Student:", students[1])


# 6. Creating and managing a list of objects dynamically
print("\n6. taking Inputs from user Creating objects dynamically using a loop")

i=1
list=[]
while True:
    print("Student ",i)  
    i=i+1
    #Taking data from user
    name=input("Enter the name :")
    age=int(input("Enter the age"))
    Class=input("Enter the CLass")
    #append the object to list
    list.append(Student(name,age,Class))
    repeat=input("Yes/No")
    if repeat.lower()=='no':
        break

print("Print With Repr")
print(list)    #it uses the __repr__ function for printing the list values not the object itself
#print the list
#to print it more better we use the 
print("Print with the str")
for i in list:
    print(i)

