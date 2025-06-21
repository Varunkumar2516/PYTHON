students = {
    "A": {"name": "John", "grade": "B"},
    "B": {"name": "Emma"},
    "C": {"grade": "A"},
}
print("\n\n method 1")
#Fetch data from the nested dictinary without error
for key, data in students.items():
    name = data.get("name", "Not Provided")
    grade = data.get("grade", "Not Available")
    print(f"{key} => Name: {name}, Grade: {grade}")

print("\n\n method 2")
for student,info in students.items():
    print(student)
    for i,j in info.items():
        print(f"{i}:{j}")