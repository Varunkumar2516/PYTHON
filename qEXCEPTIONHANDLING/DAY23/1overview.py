#--------------------------
#        DAY 23
#    EXCEPTION HANDLING
#=-------------------------


"""
exception Handling allows you to deal with runtime errors using 
try, except, else, and finally blocks.
 It ensures your program doesn't crash unexpectedly and provides 
 meaningful error messages.


#Basic Syntax:
try:
    # risky code
except SomeError:
    # handle error

"""

"""  

else:
    # runs if no error occurs
finally:
    # always runs (optional)

"""
# this code can handle all the Errors in try block
# Basic Example of opening a file that does not exist
print('\n1..Basic Code')
try:
    with open("Myfile.txt",'r') as F:
        print(F.read())
    
except :
    print("FIle Not FOund!")


#---------------------------------------------
print("\n2... Specific excpetion :Multiple Except")
#To Catch Specific Error its required to write the name of that Error with except keyword
try:
    with open("Files/newfile.txt","r") as F:
        data=F.read()
        
        print(data)
        print(" file reading done properly")
        print(Undefined_Varible)
#for the file error
except FileNotFoundError as e:
    print("file Not FOund ")
#for name error
except NameError:
 print("Name Error ")
#generic Block that handle all errors
except Exception as e:
    print(e)

#---------------------------------------------
#else Block Usage: if try block not trigger any Exception the else block runs 
#so the try block code is nonException code is placed in else blokc
print("\n\n3......Else block")
try:
    f=open("Files/newfile.txt",'r')       
except Exception as e:
    print(e)
# if try block not trigger any exceptiont than the else block runs
else:
    data=f.read()
    print(data)
    f.close()

#---------------------------------------------
print("\n\n4....Finally block")
#finally block : Block Always runs even Exception triggered or not
try:
    f=open("Files/newfile.txt",'r')       
except Exception as e:
    print(e)
# if try block not trigger any exceptiont than the else block runs
else:
    data=f.read()
    print(data)
    f.close()
finally:
    print('Procedure FInish')


#---------------------------------------------

print("\n\n5... All things in one")
def myfunct():
    num1=int(input("Enter the number 1 :: "))
    num2=int(input("Enter the number 2 :: "))
    div=num1/num2
    return div
try:
    div=myfunct()
except ValueError as e:
    print("Input Should be Integer type")
except ZeroDivisionError as e:
    print("Divison By zero Not Possible ")
except Exception as e:
    print(e)
else:
    print(round(div,2))
finally:
    print("Program Executed")


#---------------------------------------------
print("\n\n 6.Raise custom Error ")
def divide(x,y):
    if y==0:
        raise ValueError("cannot divide by zero")
    return x/y
try:
    result=divide(5,0)
except ValueError as e:
    print(e)


#custom Class FOr that inherit Class Exception 
# so that we can use it as custom Exception
class NegativeAge(Exception):
    pass
#another Example
def setage(x):
    if x<0:
        raise NegativeAge("Age cannot be negative")
    return x

try:
    a=setage(-32)
except NegativeAge as e:
    print(e)