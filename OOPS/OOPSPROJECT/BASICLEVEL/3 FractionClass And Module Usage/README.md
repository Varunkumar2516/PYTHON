#  Custom Fraction Class – Python OOP Project

A simple, beginner-friendly project to create your own **Fraction data type** in Python using object-oriented programming.

This project is part of the **"Python from Beginner to Advanced"** guide – .

---

##  Features

- Create fractions (e.g., `Fraction(1, 2)`)
- Auto-simplify on creation (e.g., `4/8 → 1/2`)
- Supports:
  - Addition: `f1 + f2`
  - Subtraction: `f1 - f2`
  - Multiplication: `f1 * f2`
  - Division: `f1 / f2`
  - Equality: `f1 == f2`
  - Comparisons: `f1 < f2`, `f1 >= f2`, etc.
- Clean output with `__str__` and `__repr__`
- Handles negative denominators and zero division errors

---

##  Files

- [CUSTOM_FRACTION_CALCULATOR](./1Custom_Fraction_class.py)– Main class and usage examples
- [Fraction-Module](./Fraction_Module.py)

---

##  Example Usage
[TEST_FRACTION_MODULE](./FractionTest.py)
```python
from Custom_Fraction_class import Fraction

f1 = Fraction(2, 4)
f2 = Fraction(3, 4)

print(f1)              # 1/2
print(f1 + f2)         # 5/4
print(f1 * f2)         # 3/8
print(f1 == Fraction(1, 2))  # True
print(f1 < f2)         # True
SO on...........
for this go to file 
[TEST_FRACTION_MODULE](./Custom_Fraction_class.py)
