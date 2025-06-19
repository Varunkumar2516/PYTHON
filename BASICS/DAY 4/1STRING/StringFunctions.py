#*******************************#
#       9 STRING FUNCTIONS      #
#*******************************#
# DAY 4: STRING METHODS PRACTICE

# Sample strings
s1 = "Python3"
s2 = "Python"
s3 = "12345"
s4 = "12.34"
s5 = "   "
s6 = "HELLO"
s7 = "hello"
s8 = "Hello World"

# 1. isalnum() - Checks if all characters are alphanumeric (A-Z, a-z, 0-9)
print(s1.isalnum())     # True
print(s4.isalnum())     # False (contains a dot)

# 2. isalpha() - Checks if all characters are alphabetic (A-Z, a-z)
print(s2.isalpha())     # True
print(s1.isalpha())     # False (contains number)

# 3. isdecimal() - Checks if all characters are decimal digits (0-9)
print(s3.isdecimal())   # True
print(s4.isdecimal())   # False (contains a dot)

# 4. isdigit() - Checks if all characters are digits (similar to isdecimal, but includes superscripts/subscripts in Unicode)
print(s3.isdigit())     # True

# 5. isnumeric() - Checks if all characters are numeric (includes Roman numerals, Unicode numbers, etc.)
print(s3.isnumeric())   # True

# 6. islower() - Checks if all letters are lowercase
print(s7.islower())     # True
print(s2.islower())     # False

# 7. isupper() - Checks if all letters are uppercase
print(s6.isupper())     # True
print(s2.isupper())     # False

# 8. isspace() - Checks if the string only contains whitespace
print(s5.isspace())     # True
print(s2.isspace())     # False

# 9. istitle() - Checks if the string is in title case (each word starts with an uppercase letter)
print(s8.istitle())     # True
print(s2.istitle())     # False

# BONUS: casefold() vs lower()
print("Straße".lower())     # 'straße'
print("Straße".casefold())  # 'strasse'  (more aggressive)

