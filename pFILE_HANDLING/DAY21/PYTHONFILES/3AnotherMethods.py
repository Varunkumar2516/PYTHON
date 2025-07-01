#----------------------------
#     DAY 21 
#   More Important Methods
#----------------------------


"""
write(str)	Writes a single string
1.writelines()	Writes a list of strings
2.read(size)	Reads specific number of characters
3.readline()	Reads one line at a time
4.readlines()	Reads all lines into a list
5.seek(offset)	Moves the cursor to the given byte position
6.tell()	Returns the current cursor position
"""

print("1.")
#1. writelines(iterable)
# Writes multiple strings (lines) to a file. 
# It does NOT add newline characters automatically — you must include \n yourself if needed.

myList=["hello\n","Today\n","im\n","Doing\n ","The \n","python\n","File-Handling\n"]
with open("Method.txt",'w') as Myfile:
    Myfile.writelines(myList)

#output FIle:::

#hello
#Today
#im
#oing
# The 
#python
#File-Handling 

print("\n2.")
#2. read(size)
#Reads a specific number of characters from the file.

with open("Method.txt",'r') as f:
   content=f.read(5)  #it only reads the first 5 characters
print(content)
#output hello


print("\n3.")
#3 readline()
#it only read the single line at a time

with open("Method.txt",'r') as f:
    line1=f.readline()
    line2=f.readline()
    print(line1,line2)
#output:
#  hello 
#  today


print("\n4.")
#4 readlines()
#it read all the lines and retunr the list of that lines

with open("Method.txt",'r') as f:
    linesList=f.readlines()
    print(linesList)
#output: ['hello\n', 'Today\n', 'im\n', 'Doing\n', ' The \n', 'python\n', 'File-Handling\n']

print("\n5.")
#5 seek(offset,whance)
# it is useful to move the cursor (file pointerr) to any specific byte
# offset is the number of bytes to move
# whance is integer it can be 0,1,2
# by default whance =0 means move from start of file
# if whance =1 means move poiner from the current position
#if whance =2 means move cursor from end
with open("Method.txt",'r') as f:
    f.seek(4)
    content=f.read()
    print("hello",content)
    #important here : seek uses the Bytes 
    #in most English files the 1 byte == 1 character
    #but in files whihc have emojies or another non english content 1byte != 1 character

print("\n6.")
#6 tell()
# it returns the current position of the File Pointer

with open("Sample.txt",'r') as f:
    cursor_loc=f.tell()
    print(cursor_loc)

    f.seek(5)
    print("after Seek(5)")
    cursor_loc=f.tell()
    print(cursor_loc)

    data=f.read(5)
    print(f"After read(5) : Reading: {data}")
    cursor_loc=f.tell()
    print(cursor_loc)

    f.seek(f.tell()+5)
    print("after Seek(f.tell()+5)")
    cursor_loc=f.tell()
    print(cursor_loc)

    data=f.read(5)
    print(f"After read(5) : Reading: {data}")
    cursor_loc=f.tell()
    print(cursor_loc)
    

