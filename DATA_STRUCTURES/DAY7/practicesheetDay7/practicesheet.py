# ------------------------------------------------------------
# Day 7 Practice Extension – Tuple-Based Python Questions
# ------------------------------------------------------------
# 
# 1 Reverse a tuple using a for loop.
# 2 Create a tuple of numbers divisible by 3 from 1 to 30.
# 3 Form a tuple of characters from a string (manual method).
# 4 Create a tuple of string lengths from a list of words.
# 5 Filter and store numbers > 50 into a tuple from a list.and sort them.
#
 

#1
mytupple=(10,20,30,40,50)
print("\n1. Reverse a tuple using a for loop.")
rev=()
for i in range(len(mytupple)-1,-1,-1):
        rev=rev+(mytupple[i],)
print("original Tupple",mytupple)
print("Reverse Tupple",rev)


#2
print("\n2. Divisible by 3 upto 30")
div3=()
for i in range(0,31):
        if i%3==0:
          div3=div3+(i,)
#Tupple comprehension
# div3=tuple(i for i in range(0,31) if i%3==0)
print("Tupple of numbers Divisible By 3 upto 30 ",div3)


#3
print("\n 3.Form a tuple of characters from a string (manual method).")
string1="python"
mytupple=()
for i in string1:
      mytupple=mytupple+(i,)
print("Tuple Of characters",mytupple)


#4
print("\n 4. Create a tuple of string lengths from a list of words.")
Avengers=["HULK","ironman","Thor","BlackWidow"]
print("List of Avengers",Avengers)
length=tuple(len(i) for i in Avengers)
print("Tuple OF length ",length,type(length))



#5
print("\n5 Filter and store numbers > 50 into a tuple from a list.And Sort them")
list2=[10,100, 55, 23, 89, 2, 67]
print("List of Numbers ",list2)
num_greater_50=tuple(i for i in list2 if i>50)
print("Tuple of Numbers Greater than 50",num_greater_50)
list3=list(num_greater_50)
list3.sort()
sortedTuple=()
for i in list3:
      sortedTuple+=(i,)
print(" SOrted Tuple of Numbers Greater than 50",sortedTuple)