students = {
    "A": {"name": "John", "grade": "B"},
    "B": {"name": "Emma"},
    "C": {"grade": "A"},
}
#Fetch data from the nested dictinary without error
for key, data in students.items():
    name = data.get("name", "Not Provided")
    grade = data.get("grade", "Not Available")
    print(f"{key} => Name: {name}, Grade: {grade}")
