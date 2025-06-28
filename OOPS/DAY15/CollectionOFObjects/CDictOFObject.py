# Day 15: Collection of Objects in Python
#Dictionary of Objects


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
    
    def getname(self):
        return self.__name
    
# 2. Create multiple Student objects
print("\n2. Creating multiple Student objects")

s1 = Student("ekam", 13,"9th")
s2 = Student("suraj", 17,'12th')
s3 = Student("rishab", 19,"UG")

# 3. Store objects in a list (collection)
print("\n3. Storing all students in a DIctionary")

#we use here getname function as we cannot access the private members outsidethe class
# that method of _classname__varibalename is very long and not more beneficial
students={s1.getname():s1,
          s2.getname():s2,
          s3.getname():s3}

# 4. Iterate through the DIctionary and access each object
print("\n4. Iterating through the DIctionary and calling methods")

for i,j in students.items():
    print(i,":",j)


# 5. Accessing a specific object and its attributes
print("\n5. Accessing a specific object from the TUple")
print("Second Student:", students[s2.getname()])


# 6. Creating and managing a list of objects dynamically
print("\n6. taking Inputs from user Creating objects dynamically using a loop")

i=1
mydict={}
while True:
    print("Student ",i)  
    i=i+1
    #Taking data from user
    name=input("Enter the name :")
    age=int(input("Enter the age"))
    Class=input("Enter the CLass")
    p=Student(name,age,Class)
    mydict[name]=Student(name,age,Class)
    repeat=input("Yes/No")
    if repeat.lower()=='no':
        break

print("Print With Repr")
print(mydict)  #it uses the __repr__ function for printing the Tuple values not the object itself
#print the Tuple
#to print it more better we use the 
print("Print with the str")
for i,j in mydict.items():
    print(i,":",j)

