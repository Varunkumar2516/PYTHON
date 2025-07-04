#-------------------
#     Day 23
#+==================

"""
Standard Attributes:
type()              gives the type of that object -class
__str__()	        Returns the string representation of the exception print(e)
args            	It's a tuple that stores all the arguments you passed when raising the exception
with_traceback(tb)	Adds a traceback to the exception object

"""

try:
    1 / 0
except ZeroDivisionError as e:
    print("Exception type:", type(e))
    print("Exception print:", e)
    print("Exception args:", e.args)
    print("Exception string format:", str(e))
    print("Exception traceback:", e.with_traceback)
    print("Exception developer view:", repr(e))


"""
Output
Exception type: <class 'ZeroDivisionError'>
Exception print: division by zero
Exception args: ('division by zero',)
Exception string format: division by zero
Exception traceback: <built-in method with_traceback of ZeroDivisionError object at 0x00000183917C7A00>
Exception developer view: ZeroDivisionError('division by zero')
"""