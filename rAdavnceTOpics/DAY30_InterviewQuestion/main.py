from Mymodule import SquareClass

obj = SquareClass(5)
print(obj.area())
print("__name__ in main.py is:", __name__)

"""
When you run main.py:
Python executes main.py as the entry point.

So in main.py, __name__ == "__main__".

Python sees the from Mymodule import ... and imports Mymodule.py.

In Mymodule.py, __name__ == "Mymodule" because it is being imported, 
not run directly.

so this concept is used to make sure that the test code
of the mymodule.py not runs by checking the condition

if __name__ == "__main__":
    # run this only when executed directly
    # so if the module is imported this part of code not runs
"""
