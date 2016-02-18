# Loop through an inital list finding all numbers that are even
# save that in a variable, then loop through that list after asking the user
# for wut they want to find devisors for. Return that and print it.

# def squares(lowerBound, upperBound):
#     firstList =  [i for i in range(lowerBound, upperBound + 1) if i % 2 == 0]
#     devideInput = int(input("enter a num to divide?"))
#     return [i for i in firstList if i % devideInput == 0]
#
# print(squares(int(input("lower?")), int(input("upper?"))))


# nessted some lists in lists and found an answer.

file_contents = [line.strip() for line in open("i211-assets/words.txt", "r")]
print(file_contents)
values = ["a", "e", "i", "o", "u"]
print([i for b in file_contents for i in b.split(" ") if len([a for a in i if a in values]) > 1])


# print([i + i for i in range(10)])

# print([i for i in range(100) if i % 10 == 0]) len([a for a in i if len(a) < 4]) > 1

# ExampleArray = ["apple", "ball", "candle", "dog", "egg", "frogs"]
# print([i.upper() if len(i) < 4 else i for i in ExampleArray])


# print("".join(["-" if i.isalpha() else i for i in str(input("Add Something!!?"))]))