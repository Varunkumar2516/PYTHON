# Day 10 – Part 4: Built-in Higher-Order Functions in Python

"""
Python provides several built-in higher-order functions.
Here, we willll cover:
     map()
     filter()
     reduce() (from functools)
Each takes a function and applies it to elements of a sequence.
"""

from functools import reduce  # required for reduce()

#  1. map() – transform each item in a sequence
print("\n1. map(): Transforming items in a list")

nums = [1, 2, 3, 4, 5]
print("simple Number",nums)
# Square each number using map
squares = list(map(lambda x: x**2, nums))
print("squares",squares)  # Output: [1, 4, 9, 16, 25]

#odd/even Lablelling Of list items
List=[1,2,3,4,5,6,7,8,9]
print("simple list",List)
labellist=list(map(lambda x:'even' if x%2==0 else 'odd',List))
print("even/odd List",labellist)



#  2. filter() – select items based on a condition
print("\n2. filter(): Filtering items based on a condition")
nums = [1, 2, 3, 4, 5]
print('Simple Nums',nums)
# Get even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Evennums ",even_nums)  # Output: [2, 4]

#fetch only fruits start from a
fruits=['apple','banana',"cherry"]
print("fruits",fruits)
Astart=list(filter(lambda fruits: fruits.startswith('a'),fruits))
print("Fruits from A",Astart)



#  3. reduce() – apply a function cumulatively and provide the single value answer
print("\n3. reduce(): Reducing a sequence to a single value")

# Multiply all numbers together
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120

#minimum among all list
min=reduce(lambda x,y: x if x<y else y,list)
#  4. Custom versions for learning purposes

print("\n4. Custom map(), filter(), and reduce()")

# Custom map
def my_map(func, seq):
    return [func(x) for x in seq]

# Custom filter
def my_filter(func, seq):
    return [x for x in seq if func(x)]

# Custom reduce
def my_reduce(func, seq):
    result = seq[0]
    for x in seq[1:]:
        result = func(result, x)
    return result

print(my_map(lambda x: x + 10, nums))        # [11, 12, 13, 14, 15]
print(my_filter(lambda x: x > 2, nums))      # [3, 4, 5]
print(my_reduce(lambda x, y: x + y, nums))   # 15


# ✅ Summary:
"""
map(func, iterable)     → Transforms items (1-to-1)
filter(func, iterable)  → Filters items (keep/discard)
reduce(func, iterable)  → Combines to a single result

All are higher-order functions because they take a function as input.
Great for functional-style programming and clean data pipelines.
"""
