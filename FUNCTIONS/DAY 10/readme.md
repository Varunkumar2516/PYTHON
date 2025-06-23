#  Day 10: Python Functions

---

## 🔹 What is a Function?

A **function** is a reusable block of code that performs a specific task. Functions help organize programs into smaller, modular, and manageable parts.

---

##  Benefits of Using Functions

-  **Avoid Code Repetition**: Write once, use multiple times.
-  **Modularity**: Breaks the program into smaller parts.
-  **Readability**: Makes code easier to understand.
-  **Maintainability**: Easier to debug and test.

---


# Back To Main Session
[Back to Main README](../../README.md)
##  Types of Functions in Python

| Type                  | Description                                      |
|-----------------------|--------------------------------------------------|
| **Built-in Functions** | Pre-defined functions like `len()`, `sum()`       |
| **User-defined Functions** | Functions created using the `def` keyword         |
| **Lambda Functions**   | Small anonymous functions written in one line   |

---

##  Syntax of a User-Defined Function

```python
def function_name(parameters):
    # code block
    return value


def greet(name):
    return "Hello " + name

print(greet("Alice"))  # Output: Hello Alice

