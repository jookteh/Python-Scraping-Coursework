#! /usr/bin/env python

import MySQLdb
import re
import cgi

print('Content-type: text/html\n')

def printCurrentTable(cursor):
    cursor.execute("SELECT * FROM candidates;")
    results = cursor.fetchall()
    return results

def searchForCandidateInfo(cursor, candidateID):
    SQL = """
        SELECT * FROM candidates
        WHERE CandidateID = """+str(candidateID)+""";
    """
    cursor.execute(SQL)
    return cursor.fetchall()

def updateVotes(db_con, cursor, candidateID, newVoteCount):
    SQL = "UPDATE candidates "
    SQL += "SET Votes = "+str(newVoteCount)
    SQL += " WHERE CandidateID = "+str(candidateID)+";"
    cursor.execute(SQL)
    db_con.commit()


string = "i211s16_ljbollin"
password = "my+sql=i211s16_ljbollin"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()
candidateID = form.getfirst('vote',"")

currentCanidateInfoArray = searchForCandidateInfo(cursor, int(candidateID))

try:
    updateVotes(db_con, cursor, int(candidateID), (int(currentCanidateInfoArray[0][5]) + 1))
except Exception as e:
    print("")



html = """
    <h1>Results</h1>
    <table border="1" width="800px">
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Votes</th>
      </tr>
        {table}
    </table>
"""

results = printCurrentTable(cursor)

results = sorted(results, key=lambda x: x[5], reverse=True)

optionsStringHTML = ""
for row in results:
    optionsStringHTML += "<tr>"
    optionsStringHTML += "<td> "+str(row[1])+" </td>"
    optionsStringHTML += "<td> "+str(row[2])+" </td>"
    optionsStringHTML += "<td> "+str(row[5])+" </td>"
    optionsStringHTML += "</tr>"

print(html.format(table = optionsStringHTML))
