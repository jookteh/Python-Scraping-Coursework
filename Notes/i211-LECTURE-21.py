! /usr/bin/env python

#! /usr/bin/env python

import cgi
import random

print('Content-type: text/html\n')

import MySQLdb

def createPersonTable(cursor):
    SQL = """CREATE TABLE Faculty
            (FacultyID Int (11) UNIQUE primary key autoincrement,
            Name varchar (30),
            Title varchar (100),
            Email varchar (25) NOT NULL,
            Areas varchar (200) NOT NULL);"""
    cursor.execute(SQL)

# INSERTING
def insertPerson(cursor, id_num, name, title, email, areas):
    SQL = "INSERT INTO Faculty (FacultyID, Name, Title, Email, Areas)"
    SQL += "VALUES ('" + str(id_num) + "', '" + name + "', '" + title + "', '"
    SQL += email + "', '" + areas + "');"
    cursor.execute(SQL)

string = "i211s16_ljbollin" 		#change username to yours!!!
password = "my+sql=i211s16_ljbollin" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

#createPersonTable(cursor)

for i in range(5):
    insertPerson(cursor, 'Jack_'+str(i), 'TEACHER_'+str(i), 'something_'+str(i)+"@hello.com", "someArea_"+str(i))

# SELECTING
cursor.execute("SELECT * FROM Faculty;")
results = cursor.fetchall()


tableViewOutput = "<table border='1'>"
tableViewOutput += "<tr>"
tableViewOutput += "  <th>ID</th>"
tableViewOutput += "  <th>Name</th>"
tableViewOutput += "  <th>Title</th>"
tableViewOutput += "  <th>Email</th>"
tableViewOutput += "  <th>Areas</th>"
tableViewOutput += "</tr>"

for row in results:
    tableViewOutput += "<tr>"
    tableViewOutput += "  <td>"+str(row[0])+"</td>"
    tableViewOutput += "  <td>"+str(row[1])+"</td>"
    tableViewOutput += "  <td>"+str(row[2])+"</td>"
    tableViewOutput += "  <td>"+str(row[3])+"</td>"
    tableViewOutput += "  <td>"+str(row[4])+"</td>"
    tableViewOutput += "</tr>"

tableViewOutput += "</table>"

html = """
<!doctype html>
    <html>
     <head><meta charset = "utf-8">
      <title>Table</title>
     </head>
      <body>

       <h2> Table: </h2>
       <div>{tableView}</div>

    </body>
</html>"""

print(html.format(tableView = tableViewOutput))
