#==============================
#          DAY 18
#       ABSTRACTION        
#==============================


"""
Abstraction means:
Hiding the internal details and showing only the necessary features to the user.
Abstraction is all about creating a class which is only inherited if constraints are followed…
It helps in:
Making your code simpler to use

"""
"""
How to Achieve Abstraction in Python?
Python supports abstraction using:

ABC → Abstract Base Class
@abstractmethod decorator
You must import from the abc module:

from abc import ABC, abstractmethod
"""

from abc import ABC,abstractmethod

#abstract CLass : Class which has atleast one abstract method
class BankApp(ABC):
    def Database(self):
        print("COnnected TO Data base")
     
     #abstract method 
    @abstractmethod 
    def Security(self):
        pass

class MobileApp(BankApp):
    def Mobile(self):
        print("Mobile App")
    
    #Here we are overriding the abstract method of the abstract class
    #If You Don't Implement Security()
    #Error: Can't instantiate abstract class
    #Python prevents you from creating a class that doesn't fulfill the abstract contract.
    def Security(self):
        print('Security Implimentation of mobileapp')


Mobile=MobileApp()
Mobile.Database()
Mobile.Security()
#obj=BankApp()  #object of abstract classcannot be created


# when create the Security () in child class
#user does not need to know about 
#how secuity works 
#how signals are sent 
#what are theback things happening 
#so these things are getting hide from user
#that is by abstraction is useful to hide the unneccessary things from user