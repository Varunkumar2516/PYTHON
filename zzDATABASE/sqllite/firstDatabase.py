import sqlite3

# 1. Create and connect to database
con = sqlite3.connect('student.db')

#2. Create cursor
cur = con.cursor()

# 3. Create table (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
            id INT,
            name VARCHAR(20),
            marks INT);""")


# 4. Insert data
id= int (input("Enter Your ID "))
name = input("Enter you name")
marks= int (input("Enter Student marks"))


# Insert into the Table
cur.execute("INSERT INTO students VALUES(?,?,?)",(id,name,marks))

# 5. Save changes
con.commit()

# 6. Fetch and display data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

for i in rows:
    print(i)


# 7. Close connection
con.close()