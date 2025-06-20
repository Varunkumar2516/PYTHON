# Warm Up : Practice Day 5

#problem 1: Write a Program to get the fibonacci series Upto 10 with for loop.
print("\n1.Fibonacci Series")
a=0
b=1
n=int(input("Enter the terms"))

if n==1:
     print(a)
else:
     print(a,b,end=" ")
     for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c,end=" ")



#problem 2: Write a program to check if the number is prime or not.
print("\n\n2.Prime number or Not")
n=int(input("Enter the number"))
if n>1:
     isprime =True
     for i in range(2,int(n**0.5)+1):
          if n%i==0:
               isprime=False
               break
     if isprime==True:
          print(f"{n} is Prime Number")
     else:
          print(f"{n} is not a PRime Number") 
else:
     print(f"{n} is not a PRime Number")



#problem 3:Print 1 to 20 Prime Numbers
print("\n3. Prime Numbers 1 to 20")
for i in range(1,21):
     if i>1:
          isprime=True
          for j in range(2,int(i**0.5)+1):
               if i%j==0:
                    isprime=False
                    break
          if isprime==True:
               print(i,end=" ")
            
          
#4 Write a Program to check the given Number is Palindrome or Not
# Original == Reverse
print("\n\n4.Palindrome checking")
n=int(input("Enter the Number "))
# rev=""
# for i in str(n):
#      rev=i+rev
newstr=str(n)
rev=newstr[::-1]
print("Reverse of n is",int(rev))

if int(rev)==n:
     print(f"{n} Is Palindrome")
else:
     print(f"{n} Is Not Palindrome")