# name = ""
# DoB =
# hairColor =
# eyeColor =
# feature =
# petName =
# petType =
# house =



# numberCollector = 0
# loopChecker = input("Enter a number or STOP?")
#
# while loopChecker != "STOP":
#     numberCollector = numberCollector + int(loopChecker)
#     loopChecker = input("Enter a number or STOP?")
#
# print(numberCollector)



# evenList = []
# oddList = []
# otherList = []
# listCounter = 0
# loopChecker = eval(input("Please enter a number"))
#
# while loopChecker != "STOP":
#     if listCounter <= 9:
#         if loopChecker % 2 == 0:
#             evenList.append(loopChecker)
#         elif loopChecker % 1 == 0:
#             oddList.append(loopChecker)
#         else:
#             otherList.append(loopChecker)
#     else:
#         print("You're Done...")
#         break
#
#     listCounter+=1
#     loopChecker = eval(input("Please enter a number?"))
#
# print("Evens: ",evenList)
# print("Odds: ",oddList)
# print("Others: ",otherList)




scores = {"Dave": 125,"Abby": 100, "Carrie": 275, "Ben": 150}

whatAreWeFinding = input("Find?")

for name in scores.keys():
    if name == whatAreWeFinding:
        print(name)













