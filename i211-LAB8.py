# import os
#
# correctPath = os.path.join(os.getcwd(), "i211-assets", "lab4_files")
#
# # it changes the file names.
#
# def removeShorts():
#     for fileName in os.listdir(correctPath):
#         if os.path.getsize(os.path.join(correctPath, fileName)) < 100 and os.path.isfile(os.path.join(correctPath, fileName)):
#             os.rename(os.path.join(correctPath, fileName), os.path.join(correctPath, fileName.replace("(SHORT)", "")))
#
# def addShorts():
#     for fileName in os.listdir(correctPath):
#         if os.path.getsize(os.path.join(correctPath, fileName)) < 100 and os.path.isfile(os.path.join(correctPath, fileName)):
#             print(fileName)
#             print(os.path.getsize(os.path.join(correctPath, fileName)))
#             os.rename(os.path.join(correctPath, fileName), os.path.join(correctPath, fileName.split(".")[0]+"(SHORT)."+fileName.split(".")[1]))
#
# while True:
#     inputCommand = str(input("add or remove?"))
#     if inputCommand == "add":
#         print("Running add...")
#         addShorts()
#     elif inputCommand == "remove":
#         print("Running remove...")
#         removeShorts()
#     else:
#        break

# nowDate = datetime.date.today()
# birthday = datetime.date(1994, 7, 17)
# print(nowDate)
# print(nowDate.strftime("%m-%d-%y. %b %A %d day of %B"))
# print((nowDate - birthday).days)
#
# start = time.clock()
# for i in range(300):
#     print(i)
# end = time.clock()
# print(end - start)











import datetime
import time
import random

start = time.clock()
while True:

    try:
        testDate = datetime.date(random.randrange(1900, 2000), random.randrange(1, 12), random.randrange(0, 31))
        print(testDate.strftime("%m-%d-%y. %b %A %d day of %B"))
        correctDate = True
    except ValueError:
        correctDate = False

    if correctDate:
        if testDate.weekday() == 3 and testDate.month == 2 and testDate.year % 7 == 0:
            print("Weekday:",testDate.weekday())
            print("Month:",testDate.month)
            print("Year:",testDate.year)

            end = time.clock()
            print("Took this long:",end - start)
            break