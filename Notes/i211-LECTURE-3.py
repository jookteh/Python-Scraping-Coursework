# groceries = ["50 apples\n", "25 pears\n", "10 oranges\n"]
# groceriesDict = {}
# for item in groceries:
#     num, fruit = item.strip().split(" ")
#     groceriesDict[fruit] = num
# print(groceriesDict)

# def playGame():
#     print("Apples")
#     firstResponse = input("Type in 'Yes' or 'No'!")
#     if firstResponse.lower() == "yes":
#         print("Organges")
#         secondResponse = input("Type in 'Yes' or 'No'!")
#         if secondResponse.lower() == "yes":
#             print("Bannanas")
#         elif secondResponse.lower() == "no":
#             print("Kiwi")
#         else:
#             print("You lose!")
#     elif firstResponse.lower() == "no":
#         print("Lime")
#         secondResponse = input("Type in 'Yes' or 'No'!")
#         if secondResponse.lower() == "yes":
#             print("Watermelon")
#         elif secondResponse.lower() == "no":
#             print("Strawberry")
#         else:
#             print("You lose!")
#     else:
#         print("You lose!")
#     print("You win")
# playGame()

# theWord = "duck"
#
# def getGuess():
#         tempGuess = input("guess something")
#         if(len(tempGuess) < 5):
#             score = 0
#             for index,letter in enumerate(theWord):
#                 if index < len(tempGuess) and tempGuess[index] == letter:
#                     score += 1
#             print("Your score: "+str(score))
#             if score == 4:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#
# def getGuess_main():
#     while True:
#         if getGuess():
#             print("Ur right!!!!!")
#             return True
#
# getGuess_main()















import math

radius = 5
height = 8
print(2 * math.pi * radius * height + (2 * math.pi * (radius ** 2)))















