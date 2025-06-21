#NESTED DICTIONARY#

#A nested dictionary means a dictionary inside another dictionary.

#Example
Data={
    "student1":{"Name":"varun","age":18},
    'student2':{"Name":"faiz","Age":42}
}

#Access Data 
print(Data["student1"]["Name"])
print(Data.get("student1",{}).get("Name","H"))



 #Modifying Nested Dictionary Values
Data["student1"]["grade"] = "A+"
print(Data["student1"])  # Updated value



#Adding New Nested Dictionary Entries
Data["student3"] = {"name": "Charlie", "age": 22, "grade": "C"}
print(Data)


#Deleting Entries from Nested Dictionary
Data.pop("student3") # Removes entire student2 record
print("\n\nAfter Delete\n",Data)
#to delete specific nested key
Data["student2"].pop("Age")



#Looping Through a Nested Dictionary

for student, info in Data.items():
    print(student)
    for key, value in info.items():
        print(f"  {key}: {value}")
