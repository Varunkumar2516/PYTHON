###############################
#   ITERATION IN DICTIONARY   #
###############################

Student={
    "name":"Varun Kumar",
    "age":18,
    "Roll no.":2301705,
    "Class":"Cse B"
    }

print("1.printing All the keys by one by one")
for i in Student:
    print (i)
print("\nWith .keys() function")
for i in Student.keys():
    print(i)


print("\n\n\n2.printing All the values by one by one")
for i in Student:
    print(Student[i])
print("\nWith .values function")
for i in Student.values():
    print(i)

print("\n\n\n3.printing All the values by one by one")
for i in Student:
    print(i,"\t",Student[i])
print("\nWith .values function")
for i,j in Student.items():
    print(i,j)

