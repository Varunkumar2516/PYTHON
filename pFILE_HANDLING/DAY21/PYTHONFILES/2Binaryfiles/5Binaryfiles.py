#---------------------------
#      BINARY fiLES
#--------------------------

#Problems with Working with text modes
#1. Cant work with binary fileslike images
#2.not good for other data types like int/float/list/tuples
"""
A binary file stores data in 0s and 1s (machine code) — 
not human-readable . You can read and write binary data
 using binary modes in Python.

 File Modes for Binary Files
"rb"	Read binary
"wb"	Write binary (overwrites)
"ab"	Append binary
"xb"	Exclusive creation in binary
"""

#WE CAN CREATE THE BINARY FORMAT OF DATA USING bytes() fucntion
#example
data=bytes([10,20,30,40])
print(data) #binary format of data 
#1  now writing to the binary files
with open("Binaryfile1.bin",'wb') as B:
    B.write(data)

#2 read from same file
with open("Binaryfile1.bin","rb") as B:
    content=B.read()
    print((content)) #Binary format 
    print(list(content))   # list format

#let us try with copy a Image from one file to another
with open("definition.jpg","rb") as original:
    with open("Copy_img.jpg",'wb') as copy:
        copy.write(original.read()) 
        #create the new file as copy of another jpg file
    

#Using "wb"/"rb" lets you write or read raw binary data, but…
#You still need to convert complex Python objects (like dictionaries, lists, classes)
#  into binary — and that’s what serialization does.