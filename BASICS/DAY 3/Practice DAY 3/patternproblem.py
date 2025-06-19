"""PATTERN PROBLEM
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
n= int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
n= int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4
5
"""
n= int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end=' ')
    print()


"""      
        *
      * *
    * * *
  * * * *
* * * * *
"""
n= int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for k in range(i):
        print("*",end=' ')
    print()


"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""
*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * *
* *
*"""
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end=" ")
    print()



"""
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64"""
for i in range(1,9):
    for j in range(1,i+1):
        print(j*i,end=" ")
    print()