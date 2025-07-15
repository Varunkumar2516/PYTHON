"""
 __Task: File and Directory Analyzer__

Create a Python script that takes a directory path as input, analyzes all the files within it (non-recursively), and outputs the following information for each file:


1.Check if the given path exists and is a directory.

Use: os.path.exists(), os.path.isdir()

2.List all entries in the directory.

Use: os.listdir()

- For each entry:
Check if it is a file.
Use: os.path.isfile()

- Print the following details:

1.Absolute path → os.path.abspath()

2.File size in bytes → os.path.getsize()

3.File name and extension → os.path.splitext()

4.Relative path from the current directory → os.path.relpath()

5.Use os.path.join() to construct full paths.

"""

import os
import time

Path=input("Enter the Directory Path :")
def checkdirectory(path):
    try:
        mylist=os.listdir(path)
    except PermissionError:
        print("Permission Denied")
        return
    print("\tNested Content:",mylist)
    for i in mylist:
        full_path=os.path.join(path,i)
        if os.path.isfile(full_path):
         print("\n\tFile :",i)
            
         print("\t1.Absolute Path",os.path.abspath(full_path))
         print("\t2.Size of file ",os.path.getsize(full_path))
         print(f"\t3. Filename {os.path.splitext(i)[0]}\n\t  FileExtension {os.path.splitext(i)[1]}")
         print("\t4.Relative Path ",os.path.relpath(full_path))
         x=os.path.getmtime(full_path)
         print("\t5. Last Modified Time",time.ctime(x))
        else:
            print("\n\tDirectory :",i)  
            checkdirectory(full_path)


if os.path.exists(Path):
    print("\tValid Path\n")
    # Check if the Path COntains the FIles or not
    if os.path.isdir(Path):
       print("Directory Path")
       checkdirectory(Path)
    else:
        print("File Path")

else:
    print("Not A Valid Path")