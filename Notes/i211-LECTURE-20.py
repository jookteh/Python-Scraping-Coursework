import sqlite3

def createPersonTable(cursor):
    SQL = """CREATE TABLE Faculty
            (FacultyID Int (11) UNIQUE,
            Name varchar (30),
            Title varchar (100),
            Email varchar (25) NOT NULL,
            Areas varchar (200) NOT NULL);"""
    cursor.execute(SQL)

def insertPerson(cursor, id_num, name, title, email, areas):
    SQL = "INSERT INTO Faculty (FacultyID, Name, Title, Email, Areas)"
    SQL += "VALUES ('" + str(id_num) + "', '" + name + "', '" + title + "', '"
    SQL += email + "', '" + areas + "');"
    cursor.execute(SQL)

def updatePerson(cursor, updatePerson, updateTitle, updateEmail, updateArea):
    SQL = "UPDATE Faculty "
    SQL += "SET Name='"+updatePerson+"', Title='"+updateTitle+"', Email='"+updateEmail+"', Areas='"+updateArea+"' "
    SQL += "WHERE Name='"+updatePerson+"';"
    print(SQL)
    cursor.execute(SQL)
    db_con.commit()


db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

#createPersonTable(cursor)

for i in range(5):
    insertPerson(cursor, i, 'Jack_'+str(i), 'TEACHER_'+str(i), 'something_'+str(i)+"@hello.com", "someArea_"+str(i))


cursor.execute("SELECT * FROM Faculty;")
results = cursor.fetchall()

def updatePersonAskQuestions():
    name = str(input("Who do you want to change? (by name)"))
    title = str(input("New title?"))
    email = str(input("New email?"))
    areas = str(input("New areas?"))

    updatePerson(cursor, name, title, email, areas)

print()
print("Pretty Table")
print("-"*45)
print("ID\tName\tTitle\t\tEmail\t\t\t\t\tAreas\t")

for row in results:
    print(str(row[0])+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4])


updatePersonAskQuestions()
db_con.commit()

cursor.execute("SELECT * FROM Faculty;")
results = cursor.fetchall()

print()
print("Pretty Table")
print("-"*45)
print("ID\tName\tTitle\t\tEmail\t\t\t\t\tAreas\t")

for row in results:
    print(str(row[0])+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4])
