import mysql.connector as c

con=c.connect(
    host='localhost',
    user='root',
    password='varun@123',
    database='school'
)

if con.is_connected():
    print("SUccessfully connected")
else :
    print("Some Problems WIth COnnections")


while True:
# CReating CUrsor 
    try:
        cur=con.cursor()
        query1="""CREATE TABLE IF NOT EXISTS student
                    (Id INT primary key,
                    name VARCHAR(20),
                    marks INT);    """
        cur.execute(query1)

        id= int (input("Enter Your ID "))
        name = input("Enter you name ")
        marks= int (input("Enter Student marks "))

        query2="INSERT INTO  student VALUES (%s,%s,%s)"
        data=(id,name,marks)
        cur.execute(query2,data)
        con.commit()



        query3="SELECT * FROM Student"
        cur.execute(query3)
        rows=cur.fetchall()

        for i in rows:
            print(i)
    except Exception as e:
        print(e)

















