# Problem Statement:
"""
Create a console-based Student Information Management System that allows users
to input and store student details using object-oriented programming principles
in Python. The system should collect student name, age, and roll number, display
the entered data, and store it in a dictionary for further access. This project 
demonstrates the use of classes, object creation, instance variables, methods, and 
dictionaries for data storage.
"""

class Student:
    def __init__(self, name,age, roll_no):
        self.name = name        # initializing instance variable name
        self.age =age   # initializing instance variable roll_no
        self.roll_no = roll_no  # initializing instance variable roll_no
        

    def display_info(self):
        print("\n\n Stored Data ")
        print(f"Student Name:: {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll Number : {self.roll_no}")
    def store_inDIct(self,mydict):
        mydict[self.name]=(self.age,self.roll_no)
        
student_dict={}

print("=========================================")
print("  Student Information Management System  ")
print("=========================================")
while True:
    name=input("Enter Your Name ::")
    age=input("Enter your Age :: ")
    rollnumber=input("Enter your rollno. :: ")
    myobj=Student(name,age,rollnumber)
    myobj.display_info()
    myobj.store_inDIct(student_dict)
    repeat=input("\n\n Enter (yes/no) FOr new Student : ")
    if repeat.lower()=='no':
        print('Thank you')
        break
print("Stored Information in Dictionary FOrmat : ")
print("{")
for i,j in student_dict.items():
        print(i,":",j)
print("}")        
      