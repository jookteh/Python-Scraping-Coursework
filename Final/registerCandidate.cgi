#! /usr/bin/env python

import MySQLdb
import re
import cgi

print('Content-type: text/html\n')

def createSQLTable(cursor):
    SQL = """CREATE TABLE candidates
         (CandidateID Int (11) NOT NULL primary key auto_increment,
         NameFirst varchar (25) NOT NULL,
         NameLast varchar (25) NOT NULL,
         Party varchar (30),
         Promises varchar (200),
         Votes Int (11)
         );"""
    cursor.execute(SQL)

def insertPerson(cd_con, cursor, NameFirst, NameLast, Party, Promises, Votes):
    SQL = "INSERT INTO candidates (NameFirst, NameLast, Party, Promises, Votes)"
    SQL += "VALUES ('" + str(NameFirst) + "', '" + str(NameLast) + "', '" + str(Party) + "', '"
    SQL += str(Promises) + "', " + str(Votes) + ");"
    cursor.execute(SQL)
    db_con.commit()

string = "i211s16_ljbollin"
password = "my+sql=i211s16_ljbollin"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()

try:
    createSQLTable(cursor)
except Exception as e:
    print("")

FirstName = form.getfirst('fname',"")
LastName = form.getfirst('lname',"")
Party = form.getfirst('party',"None")
Promises = form.getfirst('prom',"None")

try:
    insertPerson(db_con, cursor, FirstName, LastName, Party, Promises, 0)
    print("<h1>Candidate Registered</h1>")
    print("<a href='vote.cgi'>Go Vote!</a>")
except Exception as e:
    print(e)
