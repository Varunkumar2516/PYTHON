#===================================================================================
#Program 1:Exception handling:TAKE INPUT FROM USER IF IT IS NOT VALID PRINT VALUE=0
#===================================================================================

name=input("Enter student name : ") #in string
grade=input("Enter student grade : ") #in string

try:
    age=int(input("Enter the student age : "))
except ValueError:
    print("Invaliid input for age ,setting age=00 by default")
    age=0
   
email=input("Enter the student Email : ")

try:
    phno=int(input("Enter the student phone number: "))
except ValueError:
    print("Invalid phone number.setting phone number =x by deafault")
    phno="x"
print("Student information :: ")
print(f"""
Name     : {name}
Grade    : {grade}
Age      : {age}
Email    : {email}
Phone No.: {phno}
""")
    
