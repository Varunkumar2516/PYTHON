# = Using join() Method for list to string
# ----------------------------------

# 1. Joining a list of words with space
words = ['Data', 'Science', 'with', 'Python']
result1 = ' '.join(words)
print("1. Space-separated:", result1)  # Output: Data Science with Python

# 2. Joining a list of names with hyphens
names = ['Alice', 'Bob', 'Charlie']
result2 = '-'.join(names)
print("2. Hyphen-separated:", result2)  # Output: Alice-Bob-Charlie

# 3. Joining characters to form a string
chars = ['P', 'y', 't', 'h', 'o', 'n']
result3 = ''.join(chars)
print("3. Joined characters:", result3)  # Output: Python

# 4. Sorting and joining characters of a string
text = "science"
sorted_chars = sorted(text)  # ['c', 'e', 'e', 'i', 'n', 's']
result4 = '-'.join(sorted_chars)
print("4. Sorted and joined:", result4)  # Output: c-e-e-i-n-s

# 5. Joining numbers (convert to strings first)
numbers = [1, 2, 3, 4]
result5 = ' '.join(str(num) for num in numbers)
print("5. Numbers joined:", result5)  # Output: 1 2 3 4

# 6. Joining file paths with slash
folders = ['home', 'user', 'documents', 'project']
path = '/'.join(folders)
print("6. File path:", path)  # Output: home/user/documents/project
