# ==================================== @
#           ATM CLASS
#=====================================

class Atm:
    #constructor used to insitalizie the class attributes
    def __init__(self):
        #two Variables
        self.pin=''
        self.balance=0
        self.menu()
    #Wait Function
    def wait(self):
        input("Press Enter to Return to Main Menu ")
        self.menu()
    def menu(self):
        print("""
     How Can I Help You?
     1. PRess 1 to Create Pin
     2. Press 2 to Change Pin
     3. Press 3 to Check Balance
     4. press 4 to withdraw
     5.Anything else to exit
              """)
        userinput=input("Enter the Input :")
        if userinput=='1':
            #Create Pin Code
            self.create_pin()
            
        elif userinput=='2':
            #change Pin
             self.change_pin()
             
        elif userinput=='3':
            #check Balance
            self.check_Balance()
        elif userinput=='4':
            #withdraw 
            self.withdraw()
        else:
            print("Thanks To visit !")
            


    def create_pin(self):
        if self.pin=='':
            inpin=input("Enter Your 4-Digit Pin :")
            if inpin.isdigit() and len(inpin)==4:
                self.pin=inpin
                
                startingbalance=input("Enter the First Amount To Deposit :")
                if startingbalance.isdigit():
                    self.balance=int(startingbalance)
                    print("Pin Created Succesfully ")
                else:
                    print("Invalid Balance Input ,Try Again")
            else:
                print("Pin Must Be of 4 digit Number!")
        else :
            print("Pin Already Created")
        self.wait()
            

    def change_pin(self):
         if self.pin=='':
             print("First Create THe Pin !")
             self.wait()
         else:
             oldpin=input("Enter your Old Pin :")
             if str(oldpin)==str(self.pin ):
                  inpin=input("Enter 4-digit New Pin :")
                  if inpin.isdigit() and len(inpin)==4:
            
                     self.pin=inpin
                     print("new Pin Set Successfully !")
                     self.wait()
                  else:
                     print("Pin must be of 4-digit !Try Again")
                     self.wait()

                 
             else :
                 print("Pin Entered is Incorrect !! Try Again")
                 self.wait()
        
         
    def check_Balance(self):
        oldpin=input(" TO Check Your Balance : Enter your Old Pin")
        if str(oldpin)==str(self.pin ):
             print("Balance :: ₹"  ,self.balance)
             self.wait()
            
        else:
            print("Pin Incorrect ! Try Again")
            self.wait()

    def withdraw(self):
        oldpin=input(" TO Withdraw : Enter your Old Pin :")
        if str(oldpin)==str(self.pin ):
             print("Balance :: ₹"  ,self.balance)
             amount=input("Enter Amount to Withdraw :")
             if amount.isdigit():
                 self.balance=int(self.balance)
                 amount=int(amount)
                 if amount<=self.balance:
                     
                     self.balance-=amount
                     print("Withdraw succesfully : ₹",amount)
                     print(" Balance : ₹",self.balance)
                     self.wait()
                 else:
                     print("Insufficient Balance !")
                     self.wait()
                    
            
        else:
            print("Pin Incorrect ! Try Again")
            self.wait()
    
     
        

 


User1=Atm()

        