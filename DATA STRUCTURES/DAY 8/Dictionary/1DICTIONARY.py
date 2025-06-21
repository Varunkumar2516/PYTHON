# ----------------------------------
# Day 8: Dictionary 
# ----------------------------------
# A dictionary is a collection of key-value pairs.
# It's like a real dictionary where you look up a word (the key)
# and find its meaning (the value).
# Dictionaries are written in curly braces: {key: value}
# Keys must be unique, and values can be of any data type and can be duplicate

"""
Syntax:
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
"""
#Example
Student={
    "name":"Varun Kumar",
    "age":18,
    "Roll no.":2301705,
    "Class":"Cse B"
    }

#1Accessing values in Dictionary
#If the Key is Not available In Dictionary it Gives Error
print("1.\nName",Student["name"])
print("class",Student["Class"])
print("RollNO.",Student["Roll no."])
print("Age",Student["age"])

#get()::To Avoid Error We use .get(key,default) Function
print("\n2.\n.get(key,default) Function")
print(Student.get("Name"))
print(Student.get("Name","N/A"))
print(Student.get("name","Key Found"))



#2Updating Values In Dictionary[Mutable]
Student["Grade"]="A+"    #This will Add the New Key-value Pair or Update it
print("Grade ",Student["Grade"])
#To check
print(Student.items())



#3To Remove A key-Value pair from dictionary
print("\n3.")
Student.pop("Grade") #it removes the grade key from the Dictionary
print("After Removing Grade")
print(Student.items())


#To View the Dictionary
print("\n\n4.")
#only keys
print(Student.keys())
#only values
print(Student.values())
#Full Dictionary
print(Student.items())