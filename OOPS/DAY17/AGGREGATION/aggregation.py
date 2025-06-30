# ===============================
#        DAY 13 - AGGREGATION
# ===============================
"""
Aggregation is a form of association that represents a "has-a" relationship between two classes.
Its a way to use one class inside another without strong coupling — the contained object can exist independently of the container object.
Example: A Student has a Address, but an Address can exist without the Student.
"""
#using object of one class as the argument to the object of another class 
#as in this code we are using the Address() object as argument to the Student() object 

class Student:
    def __init__(self,name,Rollno,Address):
        self.name=name
        self.Rollno=Rollno
        self.address=Address

    def __str__(self):
        return f"""
                Name      :  {self.name}
                RollNumber:  {self.Rollno}
                  Address   
                    HouseNo.  :  {self.address.get_HouseNo()}  
                    Area      :  {self.address.Area}
                    Pin       :  {self.address.pin}
                    City      :  {self.address.City}
                    State     :  {self.address.State  }"""
    
    def EditProfile(self,name,RollNo,HouseNO,Area,Pin,City,State):
        self.name=name
        self.Rollno=RollNo
        self.address.Edit_address(HouseNO,Area,Pin,City,State)
    
class Address:
    def __init__(self,HouseNo,Area,Pin,City,State):
        self.__HouseNo=HouseNo #taking this as Private 
        #the aggreagated class cannot use it directly we have to use the getter method or the obj._classname__variablename
        self.Area=Area
        self.pin=Pin
        self.City=City
        self.State=State
    def get_HouseNo(self):
        return self.__HouseNo
    
    def Edit_address(self,HouseNO,Area,Pin,City,State):
        self.__HouseNo=HouseNO 
        self.Area=Area
        self.pin=Pin
        self.City=City
        self.State=State

A1=Address("34/3","New DEOL Nagar",144001,"Jalandar","Punjab")
S1=Student("Suraj",2301705,A1)

print(S1)

# so here we are using the address object as the argument to Student class Object


S1.EditProfile("Varun",2301705,"52","Green Avenue",144002,"jalandhar","Punjab")
print(S1)