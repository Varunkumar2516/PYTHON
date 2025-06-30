 #b .Operator Overloading :Same  operator, different behavior depending on the type
print("\n# Polymorphism with '+' operator")
print(2 + 3)         # 5 (integers)
print("Hello " + "World")  # Hello World (strings)
print([1, 2] + [3, 4])     # [1, 2, 3, 4] (lists)

#Same + operator, different behavior depending on the type — this is also polymorphism





print("\n\nusing function")
class OperatorOverloading:
    def Funct(self,a=0,b=0):
        if type(a)==type(b) :
            return a + b
        else:
            return "Enter Both Arguments of same Type"
    
A=OperatorOverloading()
print(A.Funct(5,6))
print(A.Funct("hello its ","My Job!"))
print(A.Funct([5,6,7],[1,2,3]))
print(A.Funct([5,6,7]))
print(A.Funct())