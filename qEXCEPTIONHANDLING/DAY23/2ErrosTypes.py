#--------------------------
#        DAY 23
#    EXCEPTION HANDLING
#=-------------------------

"""
Built in errors
BaseException
 |-- SystemExit
 |-- KeyboardInterrupt
 |-- GeneratorExit
 |- Exception (most user-defined and runtime errors are here)
 """


#  1. SyntaxError
# This can't be demonstrated in a running cell since it's a parsing error
# Uncomment the below line to see it in action
# if True print("Syntax Error") 

# 2. IndentationError / TabError
# Also can't be caught while running — occurs during parsing
# Uncomment to test in script
# def my_func():
# print("Missing Indentation")  # IndentationError

#  3. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

#  4. OverflowError
import math
try:
    x=math.exp(1000)
    print(x)
except OverflowError as e:
    print("OverflowError:", e)

#  5. FloatingPointError (very rare unless manually triggered)
try:
    if 0.1+0.2==0.3:
     print("True")
except FloatingPointError as e:
    print("FLoating Point Error ",e)
#  6. IndexError:When trying to access the  out of range index
try:
    arr = [1, 2, 3]
    print(arr[10])
except IndexError as e:
    print("IndexError:", e)

#  7. KeyError:occurs when the key not found in dictionary
try:
    d = {"name": "Alice"}
    print(d["age"])
except KeyError as e:
    print("KeyError:", e)

#  8. ValueError:occurs when a function is called with the proper argument type but with the wrong value.
try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)

#  9. TypeError: Operation is perfromed on differnet objects or datatypes
try:
    print(5 + "five")
except TypeError as e:
    print("TypeError:", e)

#  10. AssertionError
#In Python, an assertion is a statement that checks if a given condition is true.
#Syntax: The basic syntax for an assertion is:
#    assert condition, message 
#condition if true the assertion passes and program runs
# but if condition fails AssertionError exception raised and stop execution

try:
    assert 95-90==0, "Math is broken!"
except AssertionError as e:
    print("AssertionError:", e)

#  11. NameError:occured when we try to access the undefined name
try:
    print(variable)
except NameError as e:
    print("NameError:", e)

#  12. UnboundLocalError:occurs when a local variable is used before it's assigned a value in functions
def example():
    try:
        print(x)
        x = 10
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)
example()

#  13. AttributeError:when we try to access the attribute which is not defined in class 
try:
    x = 10
    x.append(5)
except AttributeError as e:
    print("AttributeError:", e)



#FILE ERRORS
#  14. FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as file:
        file.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

#  15. MemoryError
try:
    x = [1] * (10 ** 10)
except MemoryError as e:
    print("MemoryError:", e)

#  16. RecursionError
def recurse():
    return recurse()
try:
    recurse()
except RecursionError as e:
    print("RecursionError:", e)

# 17. BufferError (manually constructed)
try:
    b = bytearray(1)
    mv = memoryview(b)
    b.append(1)  # Modifying buffer during export
except BufferError as e:
    print("BufferError:", e)


#  18. RuntimeError
try:
    raise RuntimeError("Something went wrong")
except RuntimeError as e:
    print("RuntimeError:", e)


#  19. SystemExit
import sys
try:
    sys.exit()
except SystemExit as e:
    print("SystemExit:", e)

#  20. KeyboardInterrupt 
try:
    while True:
        pass  # Infinite loop
except KeyboardInterrupt:
    print("Program interrupted by user (Ctrl+C)")


#  21. GeneratorExit 

# 22.SystemExit
import sys

try:
    sys.exit("Exiting the program...")
except SystemExit as e:
    print("Caught SystemExit:", e)

# #  End of all exceptions demonstration
print("\nAll common Python exceptions DONE.")


