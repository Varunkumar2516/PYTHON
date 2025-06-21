# ----------------------------------
# Day 8: Dictionary Practice Using For Loops
# ----------------------------------



# 1. DICT OF: Squares of numbers from 0 to 10
squares_dict = {}
for i in range(11):
    squares_dict[i] = i**2
print("1. Squares Dictionary:", squares_dict)
# Output: {0: 0, 1: 1, 2: 4, ..., 10: 100}


# 2. DICT OF: Count of each character in a string
text = "hello world"
char_count = {}
for char in text:
    if char != " ":  # ignoring spaces
        char_count[char] = char_count.get(char, 0) + 1
print("2. Character Count Dictionary:", char_count)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


# 3. DICT OF: Word lengths from a list
words = ['python', 'is', 'awesome']
lengths = {}
for word in words:
    lengths[word] = len(word)
print("3. Word Lengths Dictionary:", lengths)
# Output: {'python': 6, 'is': 2, 'awesome': 7}


# 4. DICT OF: Mapping index to word
word_list = ['apple', 'banana', 'cherry']
index_map = {}
for i in range(len(word_list)):
    index_map[i] = word_list[i]
print("4. Index to Word Dictionary:", index_map)
# Output: {0: 'apple', 1: 'banana', 2: 'cherry'}


# 5. DICT OF: Counting even and odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7]
count = {"even": 0, "odd": 0}
for num in numbers:
    if num % 2 == 0:
        count["even"] += 1
    else:
        count["odd"] += 1
print("5. Even/Odd Count Dictionary:", count)
# Output: {'even': 3, 'odd': 4}
