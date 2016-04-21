# (20 pts) Create a table called Addresses that has the fields AddressID, Name, Address1, Address2, City, State, Zip
# (40 pts) Ask the user to enter a Name, Address line one, Address line two (optional), City, State and Zip. Add their responses as an entry in your Addresses table.
# (10 pts) Ask the user if they would like to input a new address. Repeat step two until they say they don’t want to enter a new address.
# (30 pts) Once they are done entering ask the user for the name of the person they would like to look up. Show them the address(s) for everyone with that name.
import sqlite3

def createAddressTable(cursor):
    SQL = """CREATE TABLE Addresses
            (AddressID integer primary key autoincrement,
            Name varchar (20),
            AddressOne varchar (100),
            AddressTwo varchar (100),
            City varchar ()
            );
            """
    cursor.execute(SQL)

def insertPerson(cursor, name, address1, city, state, zip, address2=None):
    SQL = "INSERT INTO Addresses (AddressID, Name, Address1, Address2, City, State, Zip)"
    SQL += "VALUES ('" + name + "', '" + address1 + "', '"
    SQL += address2 + "', '" + city + "', '" + state + "', '" + zip + "');"
    cursor.execute(SQL)


db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

createAddressTable(cursor)


while True:
    if str(input("Want to add an address? Y/N")) == "Y":
        insertPerson(cursor, str(input("Enter Name:")), str(input("Address 1:")), str(input("Address 2:")), str(input("City:")), str(input("State:")), str(input("Zip:")))
    else:
        break

