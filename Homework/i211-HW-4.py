# Liam Bolling
# 123

import os
import datetime
from time import gmtime, strftime

# Given
def pl_translate(word):
    if len(word) <= 1:
        return word+"yay"
    pre = word[0]
    suf = word[1:]
    if pre.upper() == pre:
        cap = True
    else:
        cap = False
    pig = suf + pre.lower() + "ay"
    if cap:
        pig = pig[0].upper() + pig[1:]
    return pig


# Phase 1 (30 points)
def pl_line(inputStr):
    finalInput = ""
    for word in inputStr.split(" "):
        if word[len(word) - 1:].isalnum():
            finalInput+=pl_translate(word) + " "
        else:
            finalInput+=pl_translate(word[:len(word) - 1]) + "."
    return finalInput


# Phase 2 (25 points)
def pl_file(inputFileName, outputFileName):

    try:
        file_contents = [line.strip(" ") for line in open(os.path.join(os.getcwd(), inputFileName), "r")]

        # Phase 4 (20 points)
        totalString = strftime("%Y-%m-%d %H:%M:%S")+"\n"

        for word in file_contents:
            totalString+=pl_line(word)

        # Phase 4 (20 points)
        totalString+="\nThank you for using the Pig Latin Translator"

        tempFile = open(os.path.join(os.getcwd(), "translations", outputFileName), 'w')
        tempFile.write(totalString)
        tempFile.close()
    except FileNotFoundError:
        print("DNE")


# Phase 3 (25 points)
def myProgram():
    stringAllFiles = ""
    print("available files:")

    for fileName in os.listdir(os.path.join(os.getcwd())):
        if os.path.isfile(os.path.join(os.path.join(os.getcwd(), fileName))):
            stringAllFiles+=fileName+" "

    print(stringAllFiles)
    tempFileName = input("which file they want to translate?")
    pl_file(tempFileName,tempFileName.split(".")[0]+"(pig)."+tempFileName.split(".")[1])


# Main
myProgram()
