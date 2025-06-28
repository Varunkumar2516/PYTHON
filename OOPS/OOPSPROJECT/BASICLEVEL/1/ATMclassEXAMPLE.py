# ==================================== @
#           ATM CLASS
#=====================================

class Atm:
    #constructor used to insitalizie the class attributes
    def __init__(self):
        #two Variables
        self.__pin=''   #Private Members
        self.__balance=0  #private members
        self.menu()
    #Wait Function
    def wait(self):
        input("Press Enter to Return to Main Menu ")
        self.menu()
    def menu(self):
        print("""
     How Can I Help You?
     1. PRess 1 to Create __pin
     2. Press 2 to Change __pin
     3. Press 3 to Check __balance
     4. press 4 to withdraw
     5.Anything else to exit
              """)
        userinput=input("Enter the Input :")
        if userinput=='1':
            #Create __pin Code
            self.create___pin()
            
        elif userinput=='2':
            #change __pin
             self.change___pin()
             
        elif userinput=='3':
            #check __balance
            self.check___balance()
        elif userinput=='4':
            #withdraw 
            self.withdraw()
        else:
            print("Thanks To visit !")
            


    def create___pin(self):
        if self.__pin=='':
            in__pin=input("Enter Your 4-Digit __pin :")
            if in__pin.isdigit() and len(in__pin)==4:
                self.__pin=in__pin
                
                starting__balance=input("Enter the First Amount To Deposit :")
                if starting__balance.isdigit():
                    self.__balance=int(starting__balance)
                    print("__pin Created Succesfully ")
                else:
                    print("Invalid __balance Input ,Try Again")
            else:
                print("__pin Must Be of 4 digit Number!")
        else :
            print("__pin Already Created")
        self.wait()
            

    def change___pin(self):
         if self.__pin=='':
             print("First Create THe __pin !")
             self.wait()
         else:
             old__pin=input("Enter your Old __pin :")
             if str(old__pin)==str(self.__pin ):
                  in__pin=input("Enter 4-digit New __pin :")
                  if in__pin.isdigit() and len(in__pin)==4:
            
                     self.__pin=in__pin
                     print("new __pin Set Successfully !")
                     self.wait()
                  else:
                     print("__pin must be of 4-digit !Try Again")
                     self.wait()

                 
             else :
                 print("__pin Entered is Incorrect !! Try Again")
                 self.wait()
        
         
    def check___balance(self):
        old__pin=input(" TO Check Your __balance : Enter your Old __pin")
        if str(old__pin)==str(self.__pin ):
             print("__balance :: ₹"  ,self.__balance)
             self.wait()
            
        else:
            print("__pin Incorrect ! Try Again")
            self.wait()

    def withdraw(self):
        old__pin=input(" TO Withdraw : Enter your Old __pin :")
        if str(old__pin)==str(self.__pin ):
             print("__balance :: ₹"  ,self.__balance)
             amount=input("Enter Amount to Withdraw :")
             if amount.isdigit():
                 self.__balance=int(self.__balance)
                 amount=int(amount)
                 if amount<=self.__balance:
                     
                     self.__balance-=amount
                     print("Withdraw succesfully : ₹",amount)
                     print(" __balance : ₹",self.__balance)
                     self.wait()
                 else:
                     print("Insufficient __balance !")
                     self.wait()
                    
            
        else:
            print("__pin Incorrect ! Try Again")
            self.wait()
    
     
        

 


User1=Atm()

        