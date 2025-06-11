# Program 3: Python Data Types
# This program provides the basic built-in data types in Python with examples.

# Numeric Types
print("Numeric Types:")
int_var = 10               # Integer data type
float_var = 3.14           # Float data type
complex_var = 2 + 3j       # Complex Number data type

print("Integer:", int_var)
print("Float:", float_var)
print("Complex:", complex_var)

# string Type :: for string we just need to put the characters in double codes ""
print("\nText Type:")
str_var = "Hello, Python!"  # String
print("String:", str_var)

# Sequence Types
print("\nSequence Types:")
list_var = [1, 2, 3, "apple"]            # List
tuple_var = (10, 20, 30, "banana")       # Tuple
range_var = range(5)                     # Range

print("List:", list_var)
print("Tuple:", tuple_var)
print("Range:", list(range_var))  # Convert range to list for display

# Set Types
print("\nSet Types:")
set_var = {1, 2, 3, 4}                  # Set
frozenset_var = frozenset([1, 2, 3])    # Frozenset

print("Set:", set_var)
print("Frozenset:", frozenset_var)

# Mapping Type
print("\nMapping Type:")
dict_var = {"name": "Alice", "age": 25}  # Dictionary
print("Dictionary:", dict_var)

# Boolean Type
print("\nBoolean Type:")
bool_var1 = True
bool_var2 = False

print("Boolean True:", bool_var1)
print("Boolean False:", bool_var2)

# None Type
print("\nNone Type:")
none_var = None
print("None value:", none_var)

# Binary Types
print("\nBinary Types:")
bytes_var = b"Hello"                  # Bytes
bytearray_var = bytearray([65, 66, 67])  # Bytearray
memoryview_var = memoryview(bytes_var)  # Memoryview

print("Bytes:", bytes_var)
print("Bytearray:", bytearray_var)
print("Memoryview:", memoryview_var[0])  # Accessing first byte

