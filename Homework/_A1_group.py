#Group 123
#211 Group HW1

import csv
import datetime

def storm_by_event(event): #done
    storms = csv.DictReader(open("Indiana_Storms.csv", "r"))

    for storm in storms:
        if storm["EVENT_TYPE"] == event:
            begin = storm["BEGIN_DATE_TIME"].split(" ")[0]
            print("A", event, "happened on", begin, "in", str(storm["CZ_NAME"]) +".")
    
def storm_by_date(date): #only works for exact same input, does not work for datetime.date() input
    stormData = csv.DictReader(open("Indiana_Storms.csv", 'r'))
    
    for storm in stormData:
        begin = storm["BEGIN_DATE_TIME"].split(" ")[0]
        
        if begin == date:
            print("A", storm["EVENT_TYPE"], 'happened on', date, 'in', storm["CZ_NAME"] +'.')


event_or_date = input("Would you like to search by date or event? ")

while True:
    if event_or_date.lower() == "event" or event_or_date.lower() == "date":
        if event_or_date.lower() == "event":
            weather = input("Enter what weather would you like to search by: ")
            storm_by_event(weather)
            break
    
        else:
            chooseDate = input("Please enter your date (in the format m/d/yy): ")
            storm_by_date(chooseDate)
            break
        
    else:
        print("That is invalid, try again.")
        event_or_date = input("Would you like to search by date or event? ")


