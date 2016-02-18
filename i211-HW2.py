# Liam Bolling
# January 26, 2016


# ----------------------


# Write a program to implement a rock paper scissors game using your algorithm from HW1.

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

# RUN:
# rockPaperSciessors()

# OUTPUT
# Rock, paper or scissor?rock
# You won with rock.


# ----------------------


# 2
# Write a function that takes a one letter abbreviation for a day of the week and returns the full day.
# You may not use lists or tuples as part of your solution. Make sure you can handle invalid inputs. -1 point
# if your function is more than 5 lines long.
# print(fullweek("R"))
# >>>
# Thursday

# Did this outside the function. Needs to be somehwere...
weekDay_abrs = {
    "m": "Monday",
    "t": "Tuesday",
    "w": "Wednesday",
    "r": "Thursday",
    "f": "Friday",
    "s": "Saturday",
    "u": "Sunday"
}

# Less than 5 lines...
def fullweek(abrString):
    if abrString.lower() in weekDay_abrs:
        return weekDay_abrs[abrString]
    else:
        return "Abbreviation not found..."

# RUN:
# print("Possible abbreviations: M, T, W, R, F, S, U")
# print(fullweek(str(input("Enter a weekday abbreviation... "))))

# OUTPUT:
# Possible abbreviations: M, T, W, R, F, S, U
# Enter a weekday abbreviation... m
# Monday


# ----------------------


# 3
# Write a function that keeps the user in a loop, asking them to enter a one letter abbreviation for the day of the
# week or DONE. As long as they don’t say done, try and translate the abbreviations. If they say DONE, stop.

def weekAbbrLoops():
    while True:
        tempStore = str(input("enter a one letter abbreviation"))
        if tempStore == "DONE":
            print("Done!")
            break
        else:
            print(fullweek(tempStore))


# RUN:
# weekAbbrLoops()

# OUTPUT:
# enter a one letter abbreviationw
# Wednesday
# enter a one letter abbreviationf
# Friday
# enter a one letter abbreviationv
# Abbreviation not found...
# enter a one letter abbreviationDONE
# Done!


# ----------------------


# Write a function exclamation() that takes a string as its input and returns a version of the string with every
# vowel replaced with 4 copies of itself and an exclamation point added to the end of the string.
# print(exclamation(“argh”)
# >>>
# aaaargh!

vowels = ["a", "e", "i", "o", "u"]

def exclamation(inputString):
    returnString = []
    for lettr in inputString:
        if lettr in vowels:
            returnString.append(str(lettr) + str(lettr) + str(lettr) + str(lettr))
        else:
            returnString.append(str(lettr))
    returnString.append("!")
    return ''.join(returnString)

# RUN:
# print(exclamation("argh"))
#
# OUPUT:
# aaaargh!