#Functions Of Dictionary

# Sample dictionary we'll use 
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. dict.get(key, default)
# Safely get the value of a key. If the key doesn't exist, return the default value instead of an error.
print("1. get():", person.get("name"))         # Output: Alice
print("get() with default:", person.get("country", "USA"))  # Output: USA


# 2. dict.keys()
# Returns all the keys in the dictionary
print("\n\n2. keys():", person.keys())             # Output: dict_keys(['name', 'age', 'city'])


# 3. dict.values()
# Returns all the values in the dictionary
print("\n\n3. values():", person.values())         # Output: dict_values(['Alice', 25, 'New York'])


# 4. dict.items()
# Returns key-value pairs as tuples in a view object
print("\n\n4. items():", person.items())           # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])


# 5. dict.update(other_dict)
# Adds or updates multiple key-value pairs from another dictionary
newdict={"age": 26, "country": "USA"}
person.update(newdict)
print("\n\n5. update():", person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}


# 6. dict.pop(key)
#    dict.pop(key, default_value)
#if element is not found in dictionary it will pop valueError
#to prevent this error we use default value
# Removes the specified key and returns its value
age = person.pop("age")
print("\n\n6. pop():", age)                        # Output: 26
print("Dictionary after pop():", person)    # 'age' is removed
print(person.pop("Myname","Not found"))

# 7. dict.clear()
# Removes all items from the dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("\n\n7. clear():", temp)                     # Output: {}


# 8. dict.copy()
# Returns a shallow copy of the dictionary (not linked to original)
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print("\n\n8. copy() Original:", original)         # Output: {'x': 10, 'y': 20}
print("copy() Copied:", copy_dict)          # Output: {'x': 99, 'y': 20}


# 9. key in dict
# Checks if a key exists in the dictionary (returns True or False)
print("\n\n9. 'name' in person:", 'name' in person)      # Output: True
print("'age' in person:", 'age' in person)        # Output: False (we popped it earlier)









