#==============================
#          DAY 21
#       FILE HANDLING 
#         IN PYTHON       
#==============================


"""
File handling: it allows us to read from and write to the files
Python provides built-in functions to handle files, using functions
 like open(), read(), write(), and close().

  File Modes in Python
'r'	Read mode (default). File must exist.
'w'	Write mode. Creates file if it doesnt exist. Overwrites if it does.
'a'	Append mode. Adds data to the end of file.
'x'	Create mode. Fails if file exists.
'b'	Binary mode (useful for images, PDFs).
't'	Text mode (default).

We can also combine modes, like 'rb', 'wt', etc.
"""


# READ   Operations
#'r'	Read mode (default). File must exist.
print("\n\n1 'r'  Reading from a File")
#sample text file :"Sample.txt" must exist ,if it is not already exist the code will throw error
myfile= open("Sample.txt","r")
content=myfile.read()
print(content)
myfile.close() #manually required to CLose

print("\n2.using with statement (best Practice)")
#using with ensures that the file is automatically closed
#  after the block of code is executed — even if an error occurs.
with open ("sample.txt",'r') as File:
    content=File.read()
    print(content)
    #No need to Close file
  

print("\n3.Read Line By Line")
myfile=open("Sample.txt",'r')
for i in myfile:
    print(i.strip())

print("\n "*2)
with open("Sample.txt") as Myvar:
    j=1
    for i in Myvar:
        print(i,end=f"  {j}  Line \n")
        j+=1



