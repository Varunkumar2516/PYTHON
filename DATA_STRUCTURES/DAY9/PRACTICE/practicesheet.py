#=============================+
##    DAY9 Set Practice     
#==============================


print("\n1.Write a progam to find the max and min in a set")
myset={12,56,34,8,90,1,57}
maximum=max(myset)
minimum=min(myset)
print(f"Maximum Element {maximum} \nMinimum Element {minimum}")


#Without max() and min() function
mylist=list(myset)
mylist.sort()
maximum=mylist[-1]
minimum=mylist[1]
print(f"Maximum Element {maximum} \nMinimum Element {minimum}")



print("\n2.Write A program to find common elements in three lists using sets")
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]

set1=set(a)
set2=set(b)
set3=set(c)

print("Common Elements ",set1 & set2 & set3)



