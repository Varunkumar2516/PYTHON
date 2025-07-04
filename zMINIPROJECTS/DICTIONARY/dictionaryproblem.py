
#Problem : Take Inputs from user Name,age,COurse,Grade
#Create the dictionary of the data such that (key:value) pair should be as follows
#key should be same as the name of user
#value should be the tupple of rest data (age,course,grade)

#dict={"name1":("age","course","Grade"),
#      "name2":("age","course","Grade") 
#     }


mydict={}
while True:
    
    name=input("Enter the name :")
    age=input("Enter the age :")
    course=input("Enter the course :")
    grade=input("Enter the Grade :")
    mydict[name]=(age,course,grade)

    repeat=input("\n\nEnter (yes/NO) for next user").lower()
    if repeat=='no':
        break
print(mydict)

    
#Problem  :Four Lists of 10 Students  Name,age,COurse,Grade  are given with some blank spaces 
#Create the dictionary of the data such that (key:value) pair should be as follows
#key should be same as the name of user
#value should be the tupple of rest data (age,course,grade)
#if blank spaces comes wrtie it as N/A

#dict={"name1":("age","course","Grade"),
#      "name2":("age","course","Grade") 
#     }

names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "", "Hannah", "Ian", "Judy"]
ages = ["20", "21", "", "19", "22", "23", "20", "", "21", ""]  # some blanks
courses = ["BSc", "", "BA", "BCom", "", "BCA", "BBA", "BSc", "", "BA"]
grades = ["A", "B+", "", "A-", "B", "", "A+", "B", "C", ""]    # some blanks

mydict={}
for i in range(len(names)):    #10 students
    if names[i]=="":
        names[i]=f'Student{i+1}'
    if ages[i]=="":
        ages[i]='N/A'
    if courses[i]=="":
        courses[i]='N/A'
    if grades[i]=="":
        grades[i]='N/A'
    mydict[names[i]]=(ages[i],courses[i],grades[i])
print("{")
for i,j in mydict.items():
    print(i,":",j)
print("}")


