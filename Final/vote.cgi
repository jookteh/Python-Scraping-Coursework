#! /usr/bin/env python

import MySQLdb
import re
import cgi

print('Content-type: text/html\n')

def printCurrentTable(cursor):
    cursor.execute("SELECT * FROM candidates;")
    results = cursor.fetchall()
    return results


string = "i211s16_ljbollin"
password = "my+sql=i211s16_ljbollin"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """
    <h1>Vote Here!</h1>
    <form action="election.cgi" method="get">
    <table border="1" width="800px">
      <tr>
        <th>Vote</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Party</th>
        <th>Promises</th>
      </tr>
        {table}
    </table>
    <input type="submit" value="Vote">
    </form>
"""

results = printCurrentTable(cursor)

optionsStringHTML = ""
for row in results:
    optionsStringHTML += "<tr>"
    optionsStringHTML += "<td><input type='radio' name='vote' value='"+str(row[0])+"'></td>"
    optionsStringHTML += "<td> "+str(row[1])+"</td>"
    optionsStringHTML += "<td> "+str(row[2])+"</td>"
    optionsStringHTML += "<td> "+str(row[3])+"</td>"
    optionsStringHTML += "<td> "+str(row[4])+"</td>"
    optionsStringHTML += "</tr>"

print(html.format(table = optionsStringHTML))
