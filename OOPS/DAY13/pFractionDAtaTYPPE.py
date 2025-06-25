# =============================================
#        DAY 13 - Fraction Data Types
#         Creation using class magicfunctions
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
    
    #not a magic method simple method for reduce the fraction 
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
       


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print("\n1. Print")
print("f1 =", f1)                       # 1/2
print("f2 =", f2)                       # 3/4


print("\n2. ADD :")
print("f1 + f2 =", f1 + f2)             # 5/4

print("\n3. Substract :")
print("f1 - f2 =", f1 - f2)             # -1/4

print("\n4. Multiply :")
print("f1 * f2 =", f1 * f2)             # 3/8

print("\n5. DIVIDE :")
print("f1 / f2 =", f1 / f2)             # 2/3

print("6. Compare :")
print("Are f1 and f2 equal?", f1 == f2) # False

print("\n7. Less Than :")
print("Is f1 < f2 ?", f1 < f2)     # True

print("\n8. Greater than : ")
print("Is f1 > f2 ?", f1 > f2)     # False

print("\n9. Less Than Equal to :")
print("Is f1 <= f2 ?", f1 <= f2)   # True


print("\n10. Greater Than Equal To: ")
print("Is f1 >= f2 ?", f1 >= f2)   # False


print("\n 11. Developer Printing :")
print("Number 1",repr(f1))
print("Number 2",repr(f2))



# Testing reduction
print("\n12. Checking the Reductions ::")
f3 = Fraction(4, 8)
print("Reduced 4/8 =", f3)              # 1/2


    
