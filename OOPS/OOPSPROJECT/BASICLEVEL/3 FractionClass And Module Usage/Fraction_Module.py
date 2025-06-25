# =============================================
#        DAY 13 - Fraction MODULE
#         SAME AS PREVIOUS FILE CLASS
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
       