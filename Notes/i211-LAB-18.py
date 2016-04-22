#! /usr/bin/env python

import cgi
import random

print('Content-type: text/html\n')

import MySQLdb

def createRobotTable(cursor):
    SQL = """CREATE TABLE Robot
            (RobotID varchar (10) UNIQUE primary key ,
            Name varchar (20) NOT NULL,
            Weapon varchar (20) NOT NULL,
            HitPoints int (11) default 5);"""
    cursor.execute(SQL)

def insertRobot(cursor, robotID, name, weapon, hitpoints):
    SQL = "INSERT INTO Robot (RobotID, Name, Weapon, HitPoints)"
    SQL += "VALUES ('" + str(robotID) + "', '" + name + "', '" + weapon + "', '"
    SQL += "'" + hitpoints + "');"
    cursor.execute(SQL)

robotExampleList = [
    ["ah6d8", "Megaton", "Gun", 100],
    ["kjqhw","BB-8", "Gun", 100],
    ["hdj78","Commander Data", "Gun", 100],
    ["jdhh78","Terminator", "Gun", 100],
    ["256hs","Roomba", "Gun", 100]
]

string = "i211s16_ljbollin"
password = "my+sql=i211s16_ljbollin"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

for robot in robotExampleList:
    insertRobot(cursor, robot[0], robot[1], robot[2], robot[3])


form = cgi.FieldStorage()
didFight = form.getfirst('didFight',True)

if didFight == True:
    print("did fight")
else:
    html = """
    <html>
        <head>
        <title>Robot Fight!</title>
        </head>
         <body>
                <H1>Choose two robots to face off!</H1><hr />
                <FORM method="post" action="robot_fight.cgi">
                <H3>Please select robots:</H3>
                <p> Robot Name:
                    <select name="robot1">
                        {options}
                    </select>
                    <select name="robot2">
                        {optionsSecond}
                    </select>
                </p>
        <input type="submit" value="Fight!" />
        </FORM>
        <hr /></body>
    </html>"""

    cursor.execute("SELECT * FROM Addresses;")
    results = cursor.fetchall()

    optionsStringHTML = ""
    for row in results:
        optionsStringHTML+="<option value='"+row[1]+"'>"+row[1]+"</option>"

    print(html.format(options = optionsStringHTML, optionsSecond = optionsStringHTML))


