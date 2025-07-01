#------------------------------
#      Coding Exercises
#=-----------------------------

"""

1. Inheritance Practice
# Create a class 'Person' with name and age and profession.
# Inherit it in 'Student' class with an extra field: roll number. Store data in Dictionary with name as key
# Add methods to display both student and person info.
# """

class Person:
    mydict={}
    def __init__(self,name,age,Profession="N/A"):
        self.__name=name
        self.__age=age
        self.profession=Profession
        self.StoreData()

    def getname(self):
        return self.__name
    
    def getage(self):
        return self.__age
    
    def StoreData(self):
        Person.mydict[self.__name]=(self.__age,self.profession)

    def __str__(self):
        return f"""Name : {self.getname()}
                   AGE  : {self.getage()}
                   Profession : {self.profession}"""
    
    def ShowData(self):
        print("\n\nData :: \n")
        for i,j in Person.mydict.items():
             print(f"""Name       :{i}
                       Info       :{j}""")
    

class Student(Person):
    Studentdict={}
    def __init__(self,name,age,RollNumber):
        super().__init__(name,age,"Student")
        self.__RollNumber=RollNumber
        self.StoreData_ofStudents()
    
    def StoreData_ofStudents(self):
        Student.Studentdict[self.getname()]=(self.getage(),"Student",self.__RollNumber)
    
    def __str__(self):
       return f"""Name :{self.getname()}
                  AGE        :{self.getage()}
                  Profession :{self.profession}
                  RollNumber :{self.__RollNumber}"""
    def ShowData(self):
        Input=input("""Enter 
                    1. For Student Data
                    2. For Full Data` """)
        if Input=='1':
             for i,j in Student.Studentdict.items():
                 print(f"""Name       :{i}
                           Info       :{j}""")
        else:
            super().ShowData()

            
P1=Person("varun",18)
print(P1)

P2=Person("prince",18)
print(P2)
P3=Person("john",18)
print(P3)
S1=Student("Imran",28,120175)
print(S1)

P1.ShowData()

S1.ShowData()


    