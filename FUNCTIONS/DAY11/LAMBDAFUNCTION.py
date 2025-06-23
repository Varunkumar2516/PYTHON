#=======================================================
#  Day 11: LAMBDA FUNCTIONS
#========================================================

"""
A lambda function is an anonymous, one-line function defined using the lambda keyword instead of def.
It's  used when:
The function is short/simple
You only need it temporarily (e.g., in sorting, mapping, filtering)


SYNTAX
lambda arguments: expression

"""
print("\n1.lambda function :: lambda x, y: x + y")

def add(x, y):
    return x + y

# same as:
squrre=lambda x, y: x + y
print(squrre(5,6))


print("\n2.lambda function :: lambda x: x **2")

def square(x, y):
    return x **2 

# same as:
squrre=lambda x:x**2
print(squrre(5))


string=input("Enter the string")
a=lambda s:"a" in s
print(a(string))



print("\n3.Lambda fucntion to change the listitems to uppercase")
list=["hello","john","issac","newton"]
a=lambda s:s.upper()
mylist=[]
for i in range(len(list)):
    mylist.append(a(list[i]))
print(mylist)
