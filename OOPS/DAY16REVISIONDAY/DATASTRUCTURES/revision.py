#================================
#       Revision
#     DAta Structures
#================================

#1
print("\n\n1.Given a list of integers, remove all duplicates and sort the list in descending order.")
nums = [4, 6, 2, 9, 4, 2, 1]
# Expected output: [9, 6, 4, 2, 1]

#SOlUtion
# to REmove the duplicates changeit to set
myset={i for i in nums}
#change it back to the list
UniqueList=[i for i in myset]
#sort the uniqueList using the .sort() or sorted(list) any method In Reverse Order
UniqueList.sort(reverse=True)#sort the orginal List
#or
newsortedlist=sorted(UniqueList,reverse=True)
print("Reverse SOrted Unique List",UniqueList)
print("Reverse SOrted Unique List",newsortedlist)

#2
print("\n\n2.Write a function that returns the sum and product of numbers passed in a tuple.")
nums = (2, 3, 4)
# Expected output: (9, 24)

def Tuplesum_mul(mytuple):
    sum=0
    mul=1
    for i in mytuple:
        sum+=i
        mul*=i
    return (sum,mul)

RequiredTuple=Tuplesum_mul(nums)
print(RequiredTuple)

#3
print("\n\n3. Count the frequency of each character in a string using a dictionary.")
s = "pythonrocks"
# Expected output: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1, 'r': 1, 'c': 1, 'k': 1, 's': 1} 
#solution
required_dict={}
for i in s:
    if required_dict.get(i):
        required_dict[i]+=1
    else:
        required_dict[i]=1
print(required_dict)




#4
print("\n\n4.Find the common elements (intersection) between two sets.")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Expected output: {3, 4}

print("Intersection between a and b is ",a&b) #it Return New Set  we can also do S=a&b
print("Intersection between a and b is ",a.intersection(b))  #it also Return New Set similarly S=a.intersection(b)

print("Intersection between a and b is ",a.intersection_update(b)) #it does not return anything (NONE) it changes the Original Set a
print("Updated a",a)


#5
print("\n\n 5.Given a nested list, access and print the second element of the third sub-list.")
lst = [[1,2], [3,4], [5,6]]
# Expected output: 6

#solution
#for Nested SUblist [item number][sublist item number] both starts from 0
print(lst[2][1])


#6
print("\n\n6.Check if a key exists in a dictionary.")
d = {'a': 1, 'b': 2}
key = 'c'
# Expected output: Key not found
Message=d.get('c',"Key Not Found")

print(Message)


#7
print("\n\n7.: Create a new list of squares of even numbers from a list.")
nums = [1, 2, 3, 4, 5, 6]
# Expected output: [4, 16, 36]
Even_squares=[i**2 for i in nums if i%2==0]
print(Even_squares)


#8
print("\n\n 8.Write a script to compare the time taken to find an element in a list vs a set.(Use time module and explain the difference briefly.)")
import time

large_list = list(range(1, 1000000)) #very large list
large_set = set(range(1,1000000))  #very large set

# Time search in list
start_time = time.time()
999999 in large_list
end_time = time.time()
print("Time taken in list: ", end_time - start_time)

# Time search in set
start_time = time.time()
999999 in large_set
end_time = time.time()
print("Time taken in set: ", end_time - start_time)

#we observe that set has less time to search then list 
#set takesO(1) and list takes O(n)




#9
print("\n\n9.Use a tuple as a key in a dictionary and retrieve its value.")
d = {(1, 2): "point A", (3, 4): "point B"}
# Access value for key (1, 2)

message=d.get((1, 2),"Not FOund")
print(message)



print("\n\n 10.Merge two dictionaries into one. Handle overlapping keys by summing their values.")
d1 = {'a': 5, 'b': 3}
d2 = {'b': 2, 'c': 7}
# Expected output: {'a': 5, 'b': 5, 'c': 7}
newdict={}

for i,j in d2.items():
     if d1.get(i):
         d1[i]=d1[i]+j
     else:
         d1[i]=j

print(d1)