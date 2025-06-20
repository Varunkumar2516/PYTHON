#Creating Lists 


#1.LIST OF: Square of numbers from 0 to 10.
#2 LIST OF: Create a list of even numbers from 0 to 10.
#2 LIST OF: Create a list of PRIME numbers from 0 to 20.
#4 LIST OF: Convert all strings to uppercase from another strings
#5 LIST OF: Remove spaces from a list of strings


print("\n1. LIST OF: Square of numbers from 0 to 10 ")
Square=[]
for i in range (0,11):
    Square.append(i**2)
print(Square)


print("\n2. LIST OF: Create a list of even numbers from 0 to 10. ")
EVEN=[]
for i in range(0,11):
    if i%2==0:
        EVEN.append(i)
print(EVEN)


print("\n3. LIST OF: Create a list of PRIME numbers from 0 to 20. ")
Prime_numbers=[]
for i in range(1,21):
    isprime=True
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                isprime=False
                break
        if isprime==True:
            Prime_numbers.append(i)
       
print(Prime_numbers)



print("\n4. Convert all strings to uppercase from another strings ")
OldList=["Apple","Banana","Cherry","Mango"]
print("Old List",OldList)
NewList=[]
for i in OldList:
    NewList.append(i.upper())
print("New List :",NewList)


print("\n5. LIST OF: Remove spaces from a list of strings")
Num=["  1  ","  2  ","  3  "]
print("Num List With Unnessary spaces",Num)
NewNum=[]
for i in Num:
    NewNum.append(i.strip())
print("New List ::",NewNum)