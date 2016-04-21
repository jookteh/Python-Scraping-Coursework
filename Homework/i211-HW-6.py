# Liam Bolling
# Group 123

import sqlite3

# (20 pts) Create a table called Addresses that has the fields AddressID, Name, Address1, Address2, City, State, Zip
def createAddressTable(cursor):
    SQL = """CREATE TABLE Addresses
            (AddressID integer primary key autoincrement,
            Name varchar (20),
            AddressOne varchar (100),
            AddressTwo varchar (100),
            City varchar (30),
            State varchar (50),
            Zip varchar (5)
            );
            """
    cursor.execute(SQL)

# (40 pts) Ask the user to enter a Name, Address line one, Address line two (optional), City, State and Zip.
# Add their responses as an entry in your Addresses table.
def insertPerson(cursor, name, address1, city, state, zip, address2=None):
    SQL = "INSERT INTO Addresses (Name, AddressOne, AddressTwo, City, State, Zip)"
    SQL += "VALUES ('" + name + "', '" + address1 + "', '"
    SQL += address2 + "', '" + city + "', '" + state + "', '" + zip + "');"
    cursor.execute(SQL)


db_con = sqlite3.connect("sampleDB.txt")
cursor = db_con.cursor()

createAddressTable(cursor)

while True:
    # (10 pts) Ask the user if they would like to input a new address. Repeat step two until
    # they say they don’t want to enter a new address.
    if str(input("Would you like to enter another address? Y/N")) == "Y":
        insertPerson(cursor, str(input("Please enter Name:")), str(input("Please enter Name Address 1:")), str(input("Please enter Address 2:")), str(input("Please enter City:")), str(input("Please enter State:")), str(input("Please enter Zip (5 chars):")))
    else:
        break

cursor.execute("SELECT * FROM Addresses;")
results = cursor.fetchall()

print("-"*30)
print("---------CURRENT DB---------")
for row in results:
    print(row)
print("-"*30)


# (30 pts) Once they are done entering ask the user for the name of the person they would like to look up.
# Show them the address(s) for everyone with that name.
cursor.execute("SELECT * FROM Addresses WHERE Name = '"+str(input("Who would you like to search for?"))+"';")
results = cursor.fetchall()

print("-"*30)
print("---------SEARCH RESULTS--------")
for row in results:
    print(row)
print("-"*30)