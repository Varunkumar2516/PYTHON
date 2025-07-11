
# Project 3: To-Do List App (Console Version) 

# Goal : Let users add, view, and delete tasks from a to-do list.

import json 
Myfile="Files/Mynewfile.json"

todo_list = []
# to check my file is empty or not , if it is empty we add a empty list to it 
def checkFileEmpty():
    try:
        with open(Myfile,'r+') as F:
            todo_list=json.load(F)
    except Exception as e:
        todo_list=[]
        with open (Myfile,'w') as F:
            json.dump(todo_list,F)


def Load_from_file():
    global todo_list
    try:
        with open(Myfile,'r') as F:
            todo_list=json.load(F)
            if not todo_list:
                print("Empty File !")
    except FileNotFoundError as e:
        print("FIle Is Not found ! ")
    

def Add_to_file(task):
    global todo_list
    Load_from_file()
   
    todo_list.append(task)
    try:
        with open(Myfile,'w') as F:
            json.dump(todo_list,F)
    except FileNotFoundError as e:
        print(e)


def UpdateFile():
    global todo_list
    with open(Myfile,'w') as F:
        json.dump(todo_list,F)

def Delete_from_file(task):
    Load_from_file()
    global todo_list
    todo_list.pop(task-1)
    UpdateFile()

def wait():
    input("\nPress Enter for Main Menu ")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


checkFileEmpty()
while True:

    show_menu()
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        Load_from_file()
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\n\n\t To-DO List: ")
            for i, task in enumerate(todo_list, 1):
                print("\n\t",f"{i}. {task}")
        wait()
    elif choice == '2':
        task = input("Enter new task: ")
        Add_to_file(task)
        print("Task added!")
        wait()
    elif choice == '3':
        task_no = int(input("Enter task number to delete: "))
        
        Load_from_file()
        if 0 < task_no <= len(todo_list):
            Delete_from_file(task_no)
            
        else:
            print("Invalid task number!")
        wait()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        wait()

# Concepts used:
# - File HAndling
# - try Except practice
# - List operations (append, pop)

# - Loops and conditionals

# - Creating menus with functions

# - User interaction via input



