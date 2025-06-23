"""
1Write a python program to sort a Dictionary by value
"""
print("\n1. ")
A={"a":43,"b":55,"c":12,"d":81,"e":3}
# valuelist=[]
# for i in A.values():
#     valuelist.append(i)
# valuelist.sort()'


#step1: create the keylist

keylist=[]
for i in A.keys():
     keylist.append(i)
print(keylist)

#step2:find sorted valuelist
valuelist=sorted(A.values())
print(valuelist)

#step 3: again Update the dictionary with the sorted elements
for i in range(len(valuelist)):
    A[keylist[i]]=valuelist[i]
print("Sorted Dictionary",A)


print("\n\n2.")
"""
2.Write A python script a print dictionary such that keys are from 1 to 15
and the values should be the square of them
"""
square_dict={}
for i in range(1,16):
     square_dict[i]=i**2
print("Square_dict",square_dict)





print("\n\n3. ")
"""
3.Write a program to Multiply all the in dictionary
"""
A={"a":1,"b":3,"c":5,"d":7,"e":1}
multi=1
for i in A.values():
     multi*=i
print("Multiplication of All values of dict",multi)


print("\n\n4. ")
"""
3.Write a program to sort  dictionary with keys
"""
A={"u":1,"e":3,"z":5,"i":7,"a":9}
keylist=list(A.keys())
valuelist=list(A.values())
print(keylist,"\n",valuelist)
keylist.sort()
print("Sorted keylist",keylist)

A.clear()
for i in range(len(keylist)):
     A[keylist[i]]=valuelist[i]
print("sorted dictionary with keys",A)


