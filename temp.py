nestedCrap = [
    ["T", "MJ", "P", 1982],
    ["BB", "ACDC", "R", 1980],
    ["DSM", "PF", "R", 1973],
    ["TB", "WH", "RB", 1992]
]

# output = "{0:>25} {1:>15} {2:>15} {3:>15}"
# print(output.format("Title", "Artist", "Genre", "Year"))
# print("-"*100)
# for element in nestedCrap:
#     print(output.format(element[0], element[1], element[2], element[3]))



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


finalArray = []
headers = ["Score", "Name"]

maxLen = 0

for i in range(4):
    name = input("Name?")
    score = input("Score?")
    finalArray.append([score, name])

    if maxLen < len(score):
        maxScoreLen = len(score)

    if maxLen < len(name):
        maxScoreLen = len(name)

    table_print(headers, finalArray, maxLen)