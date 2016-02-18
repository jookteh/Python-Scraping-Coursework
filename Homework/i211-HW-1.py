# Liam Bolling
# ljbollin
# Team: (no clue)
# Monday (MLK DAY) Jan 18th 2016

# ------------ #

# 1. Write an algorithm for a Rock Paper Scissors game. The user should enter either rock, or paper, or scissors while the
# computer makes its choice randomly. The two choices are then compared with the user being told whether they won, lost,
# or tied. For this game Rock beats Scissors, which beats Paper, which beats Rock.

import random
def rockPaperSciessors():
    userChoice = input("Rock, paper or scissor?")
    computerChoices = ['rock', 'paper', 'scissor']
    computerChoice = random.randint(0, 2)

    if computerChoices[computerChoice] == 'rock' and userChoice.lower() == 'scissor':
        print("Computer won with rock.")
    elif computerChoices[computerChoice] == 'scissor' and userChoice.lower() == 'paper':
         print("Computer won with scissor.")
    elif computerChoices[computerChoice] == 'paper' and userChoice.lower() == 'rock':
        print("Computer won with paper.")

    elif computerChoices[computerChoice] == 'scissor' and userChoice.lower() == 'rock':
        print("You won with rock.")
    elif computerChoices[computerChoice] == 'paper' and userChoice.lower() == 'scissor':
        print("You won with scissor.")
    elif computerChoices[computerChoice] == 'rock' and userChoice.lower() == 'paper':
        print("You won with paper.")

    else:
        print("Tie!")
# TEST CASE - !!UNCOMMENT TO PLAY!!
# rockPaperSciessors()

# ------------ #

# 2. Write a program that takes a string as input. It should reverse the order of all the characters in the string and
# print it back out to the user. For example: AbC123 would be printed out as 321CbA

def reverseOrder(mainString):
    returnString = []
    for selectedCharNum in range(0, len(mainString)):
        returnString.append(str(mainString[len(mainString) - selectedCharNum - 1]))
    print(''.join(returnString))

# TEST CASE - !!UNCOMMENT TO USE!!
# reverseOrder(input("Enter a string..."))

# ------------ #

# 3. Write a program that ask the user to enter three words. Your program should then print True if the words were
# entered in alphabetical order. If the words were not in alphabetical order it should print False.

def reverseOrder(firstString, secondString, thirdString):
    enteredOrder = [firstString, secondString, thirdString]
    print("You Entered:")
    print(enteredOrder)

    defaultReturn = True
    alphaOrder = sorted(enteredOrder, key=str.lower)
    print("Should Be:")
    print(alphaOrder)

    for i in range(0, len(enteredOrder)):
        if enteredOrder[i] != alphaOrder[i]:
            return False
    return True

# TEST CASE - !!UNCOMMENT TO USE!!
# print(reverseOrder(
#     input("Enter First Word:"),
#     input("Enter Second Word:"),
#     input("Enter third Word:")))