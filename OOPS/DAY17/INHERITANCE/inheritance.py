#==============================
#          DAY 17
#        INHERITANCE          
#==============================

# write a code to create the SCHOOL,Teacher,Student, Person CLass 
# Person Class SHould have the access of all the Students ,teachers and other persons of the sociey as dictionary 
# Whenever New Teacher OR student COmes Add them In school Class and Store them IN dictionarys (teachers,students) ,and
# School have the access of All Students ANd THe Teachers 


class Person:
    person_id=1
    persons={}
    def __init__(self,Name,Age,Profession):
        self.Name=Name
        self.Age=Age
        self.Profession=Profession
        self.add_Person()
    def add_Person(self):
        Person.persons[Person.person_id]=(self.Name,self.Age,self.Profession)
        Person.person_id+=1

    def get_details(self):
        return f"{self.Name}, Age: {self.Age}, Profession: {self.Profession}"
    
    def ShowALLPersons(self):
        for i,j in Person.persons.items():
            print(i," : \n"," "*10,j)
            


class School:
    student_id=1
    Teacher_id=1
    def __init__(self,School_name):
        self.name=School_name
        self.Teacher={}
        self.Students={}


 #giving the Student CLass Object here 
 #aggregation
    def add_student(self,Student_name):
        self.Students[School.student_id]=Student_name
        School.student_id+=1


#giving the Teacher CLass Object here 
 #aggregation
    def add_Teacher(self,Teacher_name):
        self.Teacher[School.Teacher_id]=Teacher_name
        School.Teacher_id+=1
    
    def ShowInfo(self):
        print(f"Welcome To {self.name} ")

        print("\nStudents :")
        for i,j in self.Students.items():
            print(f"""Student ID :{i} 
                  Student Info:{j.get_details()}""")
        print("\nTeachers :")
        for i,j in self.Teacher.items():
            print(f"""Teacher ID :{i} 
                  Teacher Info:{j.get_details()}""")
        
        

class Student(Person):
    def __init__(self,name,age,Student_id,Course):
        #we can pass the argument also using the super() to our parent constructor
        super().__init__(name,age,'Student')
        self.Student_id=Student_id
        self.Course=Course
    def get_details(self):
        return f"{super().get_details()}, ID: {self.Student_id}, Course: {self.Course}"



class Teacher(Person):
    def __init__(self,name,age,Teacher_id,Subject):
        super().__init__(name,age,"Teacher")
        self.Teacher=Teacher_id
        self.Subject=Subject
    def get_details(self):
        return f"{super().get_details()}, ID: {self.Teacher}, Subject: {self.Subject}"

# ======= Example Usage =======

school = School("S.S.M Senior Secondary School")

# Add teachers
teacher1 = Teacher("Mr. Sharma", 45, "T001", "Mathematics")
teacher2 = Teacher("Ms. Roy", 38, "T002", "English")
school.add_Teacher(teacher1)
school.add_Teacher(teacher2)

# Add students
student1 = Student("Amit", 16, "S1001", "Science")
student2 = Student("Sara", 17, "S1002", "Commerce")
school.add_student(student1)
school.add_student(student2)


Person1=Person("Simran",19,"Data Scientist")

# Show all info Inside the School
school.ShowInfo()

#Show all Info As persons
print("\n\n All PERSONS")
Person1.ShowALLPersons()

