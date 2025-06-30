##==============================
#          DAY 17
#        INHERITANCE     
#        Practice   
#==============================


#1 GUess the Output

class Parent:
    def __init__(self,a):
        #private attribute
        self.__var=a
    

    def get_var(self):
        return self.__var

class Child(Parent):
    def __init__(self,a,b): 
        #calling the Parent COnstuctor
        super().__init__(a)
        self.__var2=b  #privateAttributr

        #overrides the parent method
    def get_var(self):
        Parentvar=super().get_var()
        return Parentvar,self.__var2
    
c=Child(1000,2000)
print(c.get_var())



#2 GUess the Output
class Parent:
    def __init__(self):
        self.num=1000

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var=2000
    def show(self):
        return (self.num,self.var)

son=Child()
print(son.show())


#3 Guess the Output
class Parent:
    def __init__(self):
        self.__num=1000
    def show(self):
        return self.__num
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=2000
    def show(self):
        return self.__var

c=Child()
print(c.show())



#4 Guess the Output
class Parent:
    def __init__(self):
        self.__num=1000
    def show(self):
        return self.__num
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=2000
    def show(self):
        
        return super().show(),self.__var

c=Child()
print(c.show())


#5 
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1=A()
obj2=B()
obj3=C()
print(obj1.m1() +obj3.m1() +obj3.m2())
#       20      + 30       +  20 =70



#6
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val=super().m1()+30
        return val
class C(B):
    def m1(self):
        val=super().m1()+20
        return val


obj3=C()
print(obj3.m1())