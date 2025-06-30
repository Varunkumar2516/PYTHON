#=====================
#     Revision
#-=======================

#1
print("\n1.Write a Function That Takes Input of THree NUmbers And Return Maximum Number")

def Maximum(a,b,c):
    if a>b:
        if a>c:
            return a
        else :
            return c
    else :
        if b>c:
            return b
        else:
            return c
    
#Checking the FUnction
print(Maximum(6,3,1))   #6
print(Maximum(8,10,11))   #11
print(Maximum(11,61,0))   #61


#2
print("\n2.Write a Function to create And Print A List Where the values are square of Numbers that are given as argument ")

def SquareList(start,end):
    mylist=[i**2 for i in range(start,end+1)]
    return mylist

Square_List=SquareList(1,10)
print(Square_List)


#3
print("\n3.Write a Function to That Takes Number as parmeter and check if the number is prime or not ")

def Is_prime(num):
    if num>1:
        for j in range (2,int(num**0.5)+1):
            if num%j==0:
                return False
        return True
    return False

print(Is_prime(2))  #true 
print(Is_prime(5))   #true
print(Is_prime(11))  #true
print(Is_prime(9))   #false



#4
print("\n4.Write a Function to find the sum of the List Elements")

def sum(List):
    sum=0
    for i in List:
        sum=sum+i 
    return sum
List=[1,2,3,4]
print(sum(List))

print("#using Recursion")
def sum(List):
    if len(List)==1:
      return (List[0])
    else:
      return (List[0]+sum(List[1:]))
List=[1,2,3,4]
print(sum(List))



print("\n\n5. USing Functions Write Fibonacci Series")
#with Simple Logic
# def Fibonacci_Series(num):
#     a=0; print(a,end=' ')
#     b=1;print(b,end=' ')
#     for i in range(num-2):
#         c=a+b
#         print(c,end=' ')
#         a=b
#         b=c
    
# Fibonacci_Series(5)
    
#with Recursion
def Fibonacci_series(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return Fibonacci_series(num-1)+Fibonacci_series(num-2)

n=int(input("Enter terms"))
for i in range (n):
    print(Fibonacci_series(i) ,end=' ')

               