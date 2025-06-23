# 📘 Day 11: Higher Order Functions in Python

## 🔹 Topics Covered:

- Functions as First-Class Citizens
- Higher Order Functions (HOFs)
- Common HOFs: `map()`, `filter()`, `reduce()`
- Lambda Functions
- Custom Implementations of HOFs

---
## 📄 Files:
[Function](../../FUNCTIONS)
- [Function AS 1stclassCitizens](./Functions1stclassCitizens.py)
- [THEORY HIGH ORDER FUNCTIONS](./HIGHERORDERFUNCTIONS.py)
- [3 HIGH ORDER FUNCTIONS ](./HOF3Functions.py)
- [LAMBDAFUNCTION.py](./LAMBDAFUNCTION.py)

---

## 🔄 Navigation:
- ⬅️ [Day 10 – Functions Part 1](../DAY10/README.md)
- ➡️ [Day 12 – Next Topic](../DAY11/README.md) 

# Back To Main Session
[Back to Main README](../../README.md)



## 🧠 Concepts Explained:

### 🔸 Functions as First-Class Citizens

In Python, functions are treated like any other object. This means:
- They can be passed as arguments.
- They can be returned from other functions.
- They can be assigned to variables.

```python
def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice
