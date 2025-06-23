list1=["Hello","How","are","You"]
tuple1=("I","am","Fine")


# 1:  List to Tuple:
print("1:  List to Tuple:")
newtuple=tuple(list1)
print(type(newtuple),newtuple)


#Alternative Method : Creating tuple from list with concatenation

new=()  #Empty Tuple
for i in list1:
    new=new+(i,)   #Concatenation 
print(type(new),new)



#2: Tuple to List
print("2: Tuple to List")
newlist=list(tuple1)
print(type(newlist),newlist)


#Alternative Method:With Append()function
newlist1=[] #Empty List
for i in tuple1:
    newlist1.append(i)
print(type(newlist1),newlist1)


print("\n\n\nQuestion")
#Problem 
"""
YOu have List of numbers but in string format
create tupple from it such that the elements should
be in integer format
"""
list1=["1","3","5","7"]
print(type(list1),list1,type(list1[0]))
mytupple=()
# for i in list1:
#     mytupple=mytupple+(int(i),)
mytupple=tuple(int(i) for i in list1) #Using tupple Comprehensions
print(type(mytupple),mytupple,type(mytupple[0]))

tuple1=("I","am","Fine")



#THANK YOU