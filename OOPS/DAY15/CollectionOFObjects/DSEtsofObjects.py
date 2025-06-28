# Day 15: Sets of Objects in Python
#important Sets are collection of distinct elements
#so when the objects are same (like there content name,age,class)it does not allow to add them in Sets
#But by default python treat it different and add in SET
#so to remove the same objects we use __eq__() and __hash__() functions 

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
    def __eq__(self,other):
        return (
            self.__name==other.__name and 
            self.__age==other.__age  and
            self.__Class==other.__Class
            
        )
    
    def __hash__(self):
        return hash((self.__name,self.__age,self.__Class))
    
# 2. Create multiple Student objects
print("\n2. Creating multiple Student objects")

s1 = Student("ekam", 13,"9th")
s2 = Student("suraj", 17,'12th')
s3 = Student("ekam", 13,"9th") #same object as above

# 3. Store objects in a list (collection)
print("\n3. Storing all students in a list")

#Set
students = {s1, s2, s3}

# 4. Iterate through the collection and access each object
print("\n4. Iterating through the Set and calling methods")

for student in students:
    print(student)


# 5. Accessing a specific object and its attributes
print("\n5. Accessing a specific object from the Set")
print("We know that in Sets the elements not follow any indexing Rule So we cAnnot Access specific Elements")


# 6. Creating and managing a SET of objects dynamically
print("\n6. taking Inputs from user Creating objects dynamically using a loop")

i=1
myset=set()
while True:
    print("Student ",i)  
    i=i+1
    #Taking data from user
    name=input("Enter the name :")
    age=int(input("Enter the age"))
    Class=input("Enter the CLass")
    #add the Objects to the set
    myset.add(Student(name,age,Class))
    repeat=input("Yes/No")
    if repeat.lower()=='no':
        break

print("Print With Repr")
print(myset)    #it uses the __repr__ function for printing the Set values not the object itself
#print the Myset as developer view which is {<main-- likethis>}
#to print it more better we use the 
print("Print with the str")
for i in myset:
    print(i)

