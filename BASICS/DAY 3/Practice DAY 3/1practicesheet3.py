#Practice Sheet DAY 3

"""PROBLEMS::
1.Write a program to find a sum of all the even numbers up to 50
2.Write a program to print first 20 numbers and their squared numbers
3.Write a program to find sum of first 10 odd numbers using while loop
4.Write a program to Check if a number is divisible by 8 and 12 upto 100
5.Write a program to create a billing system at supermarket"""


#Problem 1:
print("\n1. Sum of all even numbers upto 50")
sum=0
for i in range(0,51,2):
    sum=sum+i
print("Sum of even numbers upto 50 is ",sum)

#Problem 2:
print("\n2. first 20 numbers with their square")
print("Number(n)\tSquare(n^2)")
for i in range (1,21):
    print(i,"\t\t",i*i)


#Problem 3:
print("\n3.Sum of 10 odd numbers")
n=1
sum=0
i=1
while(n<=10):
    sum=sum+i
    i=i+2
    n=n+1
print("Sum of first 10 odd numbers",sum)

#problem 4:
print("\n 4.print numbers divisible by 8 and 12")
for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i,end=" ")

#problem 5:
"""  On nextprogram """