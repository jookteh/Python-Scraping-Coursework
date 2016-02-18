#--------------------------------------------------------------
#               Official Tools Module for I210
#                           Version 2
#--------------------------------------------------------------

#---------------------------------------------------------------------
#To use this file, place it in the same directory as your python code,
#then add the line:
#               from tools import *
#to the top of your python code. You can then use these functions.
#
#As you write new functions, add them to this file! If you keep this
#up-to-date and organized, it will help you tremendously!
#---------------------------------------------------------------------

#------------------------------
# string manipulation functions
#------------------------------

#prints out a birthday greeting, demonstrates default values
def birthday(name="Joe", age=21):
    print("Happy Birthday", name, "! You're", age, "!")

#Places dashes around every character of the string and returns it
def dasher(string):
    return "-" + "-".join(list(string)) + "-"

#pads a string out to 20 characters with dashes
def dasher2(string):
    if len(string) > 20:
        string = "Error"
    dashes =(20 - len(string))

    half = int(dashes/2)

    formatted = "-" * half + string + "-" * half

    if (dashes % 2 == 1):
        formatted += "-"
    return formatted

#works like dasher2, but allows you to specify a length
#20 is the default
def dasher3(string, length = 20):
    if len(string) > length:
        string = "Error"
    dashes =(length - len(string))

    half = int(dashes/2)

    formatted = "-" * half + string + "-" * half

    if (dashes % 2 == 1):
        formatted += "-"
    return formatted



#------------------------------
# number manipulation functions
#------------------------------

#returns the sum and product of two numbers
def addmult(num1, num2):
    add = num1 + num2
    mult = num1 * num2
    return add, mult

#returns True if a number is odd, False otherwise
def odd(number):
    return number % 2 == 1

#returns True if the difference between two numbers is odd, False otherwise
def odd_diff(num1, num2):
    difference = num1 - num2
    return odd(difference)

#returns the sum of a list of numbers
def summation(numbers):
    total = 0
    for num in numbers:
	    total += num
    return total

#returns the average of a list of numbers
def mean(numbers):
    total = 0.0
    for num in numbers:
            total += num
    return total/len(numbers)



#------------------------------
# list manipulation functions
#------------------------------


def swap(a_list, x, y):
    """x and y should be ints that are valid index positions."""
    a_list[x], a_list[y] = a_list[y], a_list[x]




#------------------------------
# printing functions (no return)
#------------------------------

#this function prints all numbers between low and high that are
#divisible by the factor given.
def print_range(low, high, factor):
    for num in range(low, high):
        if num % factor == 0:
            print(num, "is divisible by", factor)


# this function prints out data with headers in a nicely padded format
# headers should be a list or tuple
# data should be a list of tuples or lists
# padding is the maximum column width for all the columns.

def table_print(headers, data, padding):
    # We build up the output formatting string
    # It has this general look, but for any number of columns
    # output = "{0:>" + str(padding) + "} {1:>" + str(padding) + "}"
    output = []
    for i in range(len(headers)):
        output.append("{" + str(i) + ":<" + str(padding) + "}")
    output = " ".join(output)

    # Print the headers
    print(output.format(*headers))

    # Print as many dashes as there are columns
    # Times the padding value (plus 1 for each space)
    print(("-" * (padding) * len(headers)) + ("-" * (len(headers) - 1)))

    # Print out the data values
    for item in data:
        print(output.format(*item))
    print()

#------------------------------
# validation functions
#------------------------------



def valid_int(description):       #we are going to do this enough to warrant a function
    while True:
        try:
            valid = int(input("Please enter " + description + " (int): "))
        except:
            print("That's not an integer.")
        else:
            return valid


def open_file(filename):

    lines = []
    while True:
        try:
            in_file = open(filename, "r")
        except:
            filename = input("That filename doesn't exist. Please enter a filename: ")
        else:
            break

    lines = in_file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    in_file.close()
    return lines


#-----------------------------
# test code goes here
#-----------------------------

if __name__ == "__main__":
    print("Testing dasher:", dasher("this is a test") == "-t-h-i-s- -i-s- -a- -t-e-s-t-")
    print("Testing odd_diff:", odd_diff(18,9))

    nums = [1,2,3,4]

    print("Testing summation:", summation(nums) == 10)
    print("Testing mean:", mean(nums) == 2.5)


