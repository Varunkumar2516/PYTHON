##############################
#         DAY 3              #
#     NESTED LOOPS           #
##############################

""" Nested loops : Loops inside the another loops  :: Used for the pattern problems
syntax :

for i in range(start,end):
       for j in range(start,end):
       
"""
n=int(input("Enter the number "))


#Program 1:Print rectangle of Stars
print("\n 1. PRINT SQUARE OF STAR *")
for i in range (1,n+1):
    for j in range (1 ,n+1):
        print("*",end=' ')
    print()

#Program 2:Print Right andgled traingle of Stars
print("\n 1. Print Right angled traingle  OF STAR *")
for i in range (1,n+1):
    for j in range (0,i):
        print("*",end=' ')
    print()


#Program 3:Print a number traingle
print("\n 3. Print a number traingle ")
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end=' ')
    print()


#program 4:Multiplication table GRID(1-n)
print("\n 4.Multiplication table GRID(1-n)")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end='\t')
    print()

#program 5:HOllow Square pattern
print("\n 5. Hollow square pattern")
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#program 6: REVERSE STAR TRAINGLE
print("\n 6.REVERSE STAR TRAINGLE")
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=' ')
    print()

#PROGRAM 7:FULL PYRAMID OF STAR
print("\n 7.FULL PYRAMID")
for i in range (n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()