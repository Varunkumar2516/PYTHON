import os
# WRITE Operations

#1 "w"
"""# 'w'	Write mode.Automatically  Creates file if it doesnot exist. Overwrites if it does.
# If You Run a Write ("w") Operation Multiple Times
# Each time you open a file in write mode ("w"), it will overwrite the entire file.
#  So even if your write code runs 100 times with the same content,
#it will add only one time in file(overwrite everytime not adding)"""

#opening the file with With statement
with open("writefile.txt",'w') as File:
    File.write("""
Name:  John
Class:  10th
Roll no.:56               """)
print("\n Write Succesfully")




    
#2 "a"
"""
append mode automatically creates the file if it does not exist
and if the file already exist it doesnot erase the old content
just open the file to write the things at the end of the file
"""
with open("append.txt","a") as Myfilevar:
    
    for i in range (0,2):
        Myfilevar.write("""
Name:  John
Class:  10th
Roll no.:56           \n\n    """)
print("\n Append Succesfully")


#3 "x" (Exclusive Creation Mode)
"""
When you try to open a file in exclusive creation mode ("x"), it:
 Creates the file if it doesnt exist.
 Raises a FileExistsError if the file already exists.
"""

#so we can delete the file so it runs smoothly 
if os.path.exists("Mypython.py"):
    os.remove("Mypython.py")


with open("Mypython.py",'x') as File:
    pass
#it just create the file , if it is not exisit 
#if the file already present it pop error




