#*******************************#
#       Part 2                  #
#       9 STRING FUNCTIONS      #
#*******************************#
# DAY 4: STRING METHODS PRACTICE

"""
 Python String Methods 
"""

# 1. startswith(substring, start=0, end=len(string))
#  Checks if a string starts with a substring
text = "Learning Python is fun"
print(text.startswith("Learning"))        # True
print(text.startswith("Python", 9))       # True (starts at index 9)
print(text.startswith("fun", 18, 21))     # True (from index 18 to 21)

# 2. endswith(substring, start=0, end=len(string))
#  Checks if a string ends with a substring
print(text.endswith("fun"))               # True
print(text.endswith("Python", 0, 17))     # True (up to index 17)
print(text.endswith("is", 13, 15))        # True

# 3. swapcase()
#  Swaps uppercase to lowercase and vice versa
mixed = "PyThOn RuLes!"
print(mixed.swapcase())                   # pYtHoN rUlES!

# 4. strip(), lstrip(), rstrip()
#  Removes whitespace or specified characters
s = "  Hello World  "
print(s.strip())                          # 'Hello World'
print(s.lstrip())                         # 'Hello World  '
print(s.rstrip())                         # '  Hello World'

# With characters
url = "///docs///"
print(url.strip("/"))                     # 'docs'

# 5. split(separator, maxsplit=-1)
#  Splits the string into a list
data = "one,two,three,four"
print(data.split(","))                    # ['one', 'two', 'three', 'four']
print(data.split(",", 2))                 # ['one', 'two', 'three,four']

# 6. ljust(width, fillchar=' ')
#  Left-aligns string with optional fill character
txt = "dog"
print(txt.ljust(10, "."))                 # 'dog.......'

# 7. rjust(width, fillchar=' ')
#  Right-aligns string with optional fill character
print(txt.rjust(10, "-"))                 # '-------dog'

# 8. replace(old, new, count=-1)
#  Replaces occurrences of a substring
msg = "apple banana apple grape"
print(msg.replace("apple", "orange"))     # 'orange banana orange grape'
print(msg.replace("apple", "orange", 1))  # 'orange banana apple grape'

# 9. rindex(substring, start=0, end=len(string))
#  Finds last occurrence index (raises ValueError if not found)
text = "a quick brown fox jumps over a lazy dog"
print(text.rindex("o"))                   # 36
print(text.rindex("o", 10, 30))           # 17

# Uncommenting this will raise ValueError
# print(text.rindex("zebra"))             # ValueError

# 10. rfind(substring, start=0, end=len(string))
#  Same as rindex but returns -1 instead of error
print(text.rfind("o"))                    # 36
print(text.rfind("o", 10, 30))            # 17
print(text.rfind("zebra"))                # -1

#  BONUS: find() vs index() – What's the difference?
sample = "hello world"

# .find() returns -1 if not found
print(sample.find("z"))                   # -1

# .index() raises an error if not found
try:
    print(sample.index("z"))
except ValueError as e:
    print("Error with index():", e)

# Optional start and end in find()
print(sample.find("o", 5))                # 7
print(sample.find("o", 5, 8))             # 7

# Optional start and end in index()
try:
    print(sample.index("o", 5, 8))        # 7
except ValueError:
    print("Not found in range.")

