# Liam Bolling
# Group 123

#! /usr/bin/env python

import MySQLdb
import re
import cgi

print('Content-type: text/html\n')

def getDataFromFile():
    currentFile = open("cd_catalog.csv", 'r+')
    content = currentFile.readlines()
    finalArrayReturn = []
    for line in content:
        finalArrayReturn.append(line.strip().split(","))
    return finalArrayReturn

def searchForKeyWithCategory(cursor, searchTerm, searchCategory):
    SQL = """
        SELECT * FROM CDTABLE
        WHERE """+str(searchCategory.lower())+""" = '"""+str(searchTerm)+"""';
    """
    cursor.execute(SQL)
    return cursor.fetchall()

def createSQLTable(cursor, globalArray):
    SQL = """CREATE TABLE CDTABLE
         (cdid Int (11) UNIQUE primary key auto_increment,
         title varchar (100),
         artist varchar (100),
         country varchar (100),
         price varchar (100),
         year varchar (100)
         );"""
    cursor.execute(SQL)

def printCurrentTable(cursor):
    cursor.execute("SELECT * FROM CDTABLE;")
    results = cursor.fetchall()
    return results

def populateTable(cursor, globalArray):
    for arrayElem in globalArray:
        createNewRow(cursor, arrayElem)

def createNewRow(cursor, arrayElem):
    SQL = "INSERT INTO CDTABLE (title, artist, country, price, year)"
    SQL += "VALUES ('" + re.escape(str(arrayElem[0])) + "', '" + re.escape(str(arrayElem[1])) + "', '" + re.escape(str(arrayElem[2])) + "', '"
    SQL += re.escape(str(arrayElem[3])) + "', '" + re.escape(str(arrayElem[4])) + "');"
    cursor.execute(SQL)

string = "i211s16_ljbollin"
password = "my+sql=i211s16_ljbollin"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

globalDataArray = getDataFromFile()

try:
    createSQLTable(cursor, globalDataArray)
except Exception as e:
    print("")

populateTable(cursor, globalDataArray)

form = cgi.FieldStorage()

didSubmit = form.getfirst('didSubmit',"False")
searchTerm = form.getfirst('search',"hello")
searchCategory = form.getfirst('field',"hello")

if didSubmit == "True":

    html = """
        <h1>{header}</h1>
        <table border="1">
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Country</th>
            <th>Price</th>
            <th>Year</th>
          </tr>
            {table}
        </table>
    """

    construct = "All CDs with "+searchCategory+" matching "+searchTerm
    results = searchForKeyWithCategory(cursor, searchTerm, searchCategory)

    optionsStringHTML = ""
    for row in results:
        optionsStringHTML += "<tr>"
        optionsStringHTML += "<td>"+str(row[0])+"</td>"
        optionsStringHTML += "<td>"+str(row[1])+"</td>"
        optionsStringHTML += "<td>"+str(row[2])+"</td>"
        optionsStringHTML += "<td>"+str(row[3])+"</td>"
        optionsStringHTML += "<td>"+str(row[4])+"</td>"
        optionsStringHTML += "</tr>"

    print(html.format(header = construct, table = optionsStringHTML))

else:
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <head><meta charset="utf-8">
            <title>Album Lookup</title>
        </head>
        <body>
            <h1>Album Finder</h1>
            <form method="post" action="Group3.cgi">
                <p>Select search criteria:
                    <select name="field">
                        <option>Title</option>
                        <option>Artist</option>
                        <option>Country</option>
                        <option>Company</option>
                        <option>Price</option>
                        <option>Year</option>
                    </select>
                    </p>
                    <input type="hidden" value="True" name="didSubmit" />
                    <p>Enter search value: <input type="text" name="search"></p>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """
    print(html)
