#===========================
#      DAY !10
#     FUNCTION OUTPUT 
#============================



print("\n\n#1 ")
def g(y):
    print(x) #we can use the global variable but not change it
    print(x+1)
x=5
g(x)
print(x)

#output ::: 5 6 5 

 
print("\n\n#2")
def d(y):
    x=1
    x=x+1
    print(x)
x=5
d(x)
print(x)

#output 2 5
   



"""
print("#3")
#wrong function
def h(y):
    x+=1
    #most important we can
    #use the global variables 
    #inside function but cannot change them
x=5
h(x)
print(x)
"""



print("\n\n#3")
 #most important we can
    #use the global variables 
    #inside function but cannot change them

#to change global variable we use 
# global variable_name   
#in our function
def h(y):
    global x
    x+=1
   
x=5
h(x)
print(x)



print("\n\n4.")
def k(x):
    x=x+1
    print("in k(x) : x=",x)
    return x
x=3
z=k(x)
print("in main program scope z=",z)
print("in main program scope x=",x)