# ================================================
#  Creating Sets -  SETCOMPREHENSION
# ================================================
#SYNTAX
# my_set = {expression for item in iterable if condition}


# -----------------------------------------------
print("\n1. SET OF: Squares of numbers from 0 to 10 ")
Squares = {i**2 for i in range(0,11)}
print(Squares)

# -----------------------------------------------
print("\n2. SET OF: Even numbers from 0 to 10 ")
Even = {i for i in range(0,11) if i%2==0}
print(Even)

# -----------------------------------------------
print("\n3. SET OF: Prime numbers from 0 to 20 ")
Primes = {
    i for i in range(2,21)
    if all(i%j!=0 for j in range(2,int(i**0.5)+1))
}
print(Primes)

# -----------------------------------------------
print("\n4. SET OF: Uppercase strings from another list ")
OldSet = {"apple", "banana", "cherry", "mango"}
print("Original Set:", OldSet)
UpperSet = {i.upper() for i in OldSet}
print("Uppercase Set:", UpperSet)

# -----------------------------------------------
print("\n5. SET OF: Remove spaces from strings in a set ")
RawSet = {"  1  ", "  2  ", "  3  "}
print("Raw Set with spaces:", RawSet)
CleanSet = {i.strip() for i in RawSet}
print("Cleaned Set:", CleanSet)
