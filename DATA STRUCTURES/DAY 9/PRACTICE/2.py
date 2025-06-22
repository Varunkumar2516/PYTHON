#REGRADING DICTIONARY



#merge Two Dictionary
print("\n1.")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)

print("\n\n2.")
#revrese the key and values in dictionary
Input={'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
valuelist=list(Input.values())
Keyslist=list(Input.keys())
print(Keyslist,valuelist)
newdict={}
for i in range(len(valuelist)):
    newdict[valuelist[i]]=Keyslist[i]
print(newdict)



#Create a Dictionary from a String with Word Frequency
print("\n\n3.")
text = "python is easy and python is powerful"
mylist=list(text.split())
print(mylist)
chardic={}
for i in range(len(mylist)):
    chardic[mylist[i]]=mylist.count(mylist[i])
print(chardic)


# Group Names by First Letter Using Dictionary
print("\n\n4.")
names = ['Alice', 'Arun', 'Bob', 'Bobby', 'Charlie']

mydict={}

for i in names:
    firstchar=i[0]
    if mydict.get(firstchar,False):
        mydict[firstchar].append(i)
    else:
        mydict[firstchar]=[]
        mydict[firstchar].append(i)
print(mydict)

#OUTPUT
# {'A': ['Alice', 'Arun'], 'B': ['Bob', 'Bobby'], 'C': ['Charlie']}


#Create Nested Dictionary from Two Lists
students = ['Alice', 'Bob']
grades = [ {'math': 85, 'science': 90}, {'math': 75, 'science': 80} ]

mydict1={}
for i in range(len(students)):
    mydict1[students[i]]=grades[i]
print(mydict1)
# Output:
# {'Alice': {'math': 85, 'science': 90}, 'Bob': {'math': 75, 'science': 80}}


# Find Key with Maximum Value
marks = {'Alice': 88, 'Bob': 72, 'Charlie': 90}
maximum=max(marks.values())
for i,j in marks.items():
    if maximum==j:
        print(f"key => {i} with maxmimum value =>{j}")
        break
    
