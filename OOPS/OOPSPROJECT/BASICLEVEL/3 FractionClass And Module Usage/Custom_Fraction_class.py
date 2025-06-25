# =============================================
#        DAY 13 - Fraction Data Types
#         Creation using class magicfunctions
#            FRACTION CALCULATOR
# =============================================
"""
Fraction numbers
numertor/denominator
"""
from math import gcd
class Fraction:
    #using COnstructor 
    def __init__(self,n,m) :
       if m==0:
           raise ValueError("Denominator 0!!")
       self.numerator=n
       self.denominator=m
       self.reduce()
      
    #using the __str__ for print
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    #using for + Addition: a/b + c/d = (ad + bc)/bd
    def __add__(self,other):
        new_numerator=(self.numerator * other.denominator)+(self.denominator * other.numerator)
        new_denominator=self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
    #usign for - Substaction :a/b - c/d = (ad - bc)/bd
    def __sub__(self,other):
        new_numerator=(self.numerator * other.denominator)-(self.denominator * other.numerator)
        new_denominator=self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
     #using for the * Multiplication:a/b*c/d=a*c/b*d
    def __mul__(self,other):
        new_numerator=self.numerator * other.numerator 
        new_denominator=self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
    #using for the / division :(a/b) / (c/d) = a*d/b*c
    def __truediv__(self,other):
        new_numerator=self.numerator*other.denominator
        new_denominator=self.denominator*other.numerator
        return Fraction(new_numerator,new_denominator)
    
    #using for the == comparsion
    def __eq__(self,other):
        return (self.numerator==other.numerator) and (self.denominator == other.denominator)
      
    #using for < comparsion in a/b < c/d  =>  (ad<bc)  we just want to check this condition
    def __lt__(self,other):
        return self.numerator *other.denominator <other.numerator *self.denominator
     #using for > comparsion in a/b > c/d  =>  (ad>bc)  we just want to check this condition
    def __gt__(self,other):
        return self.numerator *other.denominator >other.numerator *self.denominator
    #using for <= comparsion in a/b <= c/d  =>  (ad<=bc)  we just want to check this condition
    def __le__(self,other):
        return self.numerator *other.denominator <=other.numerator *self.denominator
    #using for >= comparsion in a/b >= c/d  =>  (ad>=bc)  we just want to check this condition
    def __ge__(self,other):
        return self.numerator *other.denominator >=other.numerator *self.denominator
    

    #Developer Friendly Representation
    def __repr__(self):
        return f"Fraction({self.numerator},{self.denominator})"
    
    #not a magic method just, simple method for reduce the fraction 
    #if 10/5 == 2/1 like that
    def reduce(self):
        common=gcd(self.denominator,self.numerator)
        self.numerator=self.numerator//common
        self.denominator=self.denominator//common


        # Ensure denominator is always positive
        # we know a/(-b) == -a/b so check if b is -ve then multiply a with -1 and b with -1 to change sign
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
       
def wait():
    input("Press Enter to Next :")

def main():
    print("\n Welcome to the Fraction Calculator\n")

    a,b = map(int,input("Enter first fraction (a/b): ").strip().split('/'))
    c,d = map(int,input("Enter Second fraction (c/d): ").strip().split('/'))
    
    f1=Fraction(a,b)
    f2=Fraction(c,d)

    while True:
        print("""
===== MENU =====
1. Print Fractions
2. Add
3. Subtract
4. Multiply
5. Divide
6. Compare
7. Exit
""")
        choice = input("Choose an option: ")

        if choice == '1':
            print("Fraction 1:", f1)
            print("Fraction 2:", f2)
            wait()

        elif choice == '2':
            print("Addition Result:", f1 + f2)
            wait()
        elif choice == '3':
            print("Subtraction Result:", f1 - f2)
            wait()
        elif choice == '4':
            print("Multiplication Result:", f1 * f2)
            wait()
        elif choice == '5':
            try:
                print("Division Result:", f1 / f2)
            except ZeroDivisionError:
                print(" Cannot divide by zero!")
            wait()
        elif choice == '6':
            print("Equality: ", f1 == f2)
            print("Less Than: ", f1 < f2)
            print("Greater Than: ", f1 > f2)
            print("Less or Equal: ", f1 <= f2)
            print("Greater or Equal: ", f1 >= f2)
            wait()
        elif choice == '7':
            print(" Thank you for using the Fraction Calculator!")
            break
         
        else:
            print(" Invalid choice. Please try again.")


# Module-safe block
if __name__ == "__main__":
    main()
    #usefull when our file is import to another file it prevent to run the another code
    #if we not write this __name__ ="main"
    #when we import this file 
    # in anpther file to use the Fraction Class
    #then automatically the main function run
    #that will leads to inconsistency


    
