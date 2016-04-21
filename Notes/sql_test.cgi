#! /usr/bin/env python

print('Content-type: text/html\n')

import MySQLdb

string = "i211s16_username" 		#change username to yours!!!
password = "my+sql=i211s16_username" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()
print('Connection Successful!')