import sqlite3
import re
import cgi

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
         (cdid integer primary key autoincrement,
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

def populateTable(cursor, globalArray):
    for arrayElem in globalArray:
        createNewRow(cursor, arrayElem)

def createNewRow(cursor, arrayElem):
    SQL = "INSERT INTO CDTABLE  (title, artist, country, price, year)"
    SQL += "VALUES ('" + re.escape(str(arrayElem[0])) + "', '" + re.escape(str(arrayElem[1])) + "', '" + re.escape(str(arrayElem[2])) + "', '"
    SQL += re.escape(str(arrayElem[3])) + "', '" + re.escape(str(arrayElem[4])) + "');"
    cursor.execute(SQL)

db_con = sqlite3.connect("cd_db.txt")
cursor = db_con.cursor()

globalDataArray = getDataFromFile()

try:
    createSQLTable(cursor, globalDataArray)
except:
    print("TABLE ALREADY EXISTS")

populateTable(cursor, globalDataArray)

form = cgi.FieldStorage()

didFight = form.getfirst('didFight',True)
searchTerm = form.getfirst('searchTerm',"hello")
searchCategory = form.getfirst('searchCategory',"hello")

if didFight == False:

    html = """
        <h1>{header}</h1>
        <table style="width:100%">
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Country</th>
            <th>Price</th>
            <th>Year</th>
          </tr>
            <tr>
                {table}
            </tr>
        </table>
    """

    construct = "All CDs with "+searchCategory+" matching "+searchTerm
    results = searchForKeyWithCategory(cursor, searchTerm, searchCategory)

    optionsStringHTML = ""
    for row in results:
        optionsStringHTML += "<tr>"
        optionsStringHTML += "<td>"+row[0]+"</td>"
        optionsStringHTML += "<td>"+row[1]+"</td>"
        optionsStringHTML += "<td>"+row[2]+"</td>"
        optionsStringHTML += "<td>"+row[3]+"</td>"
        optionsStringHTML += "<td>"+row[4]+"</td>"
        optionsStringHTML += "</tr>"


    print(html.format(header = optionsStringHTML, table = optionsStringHTML))

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
                    <p>Enter search value: <input type="text" name="search"></p>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """
