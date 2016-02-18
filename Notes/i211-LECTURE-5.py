# file_contents = [line.strip() for line in open("i211-assets/words.txt", "r")]
# print(file_contents)
# values = ["a", "e", "i", "o", "u"]
# print([i for b in file_contents for i in b.split(" ") if len([a for a in i if a in values]) > 1])

# trans_dict = {
#     "1": "i",
#     "3": "e",
#     "4": "a",
#     "5": "s",
#     "7": "t"
# }

# trans_input = input("Well: ")
# trans_input = "7h15 15 4 t357"
#
# print("".join([i if i.isalpha() or i == " " else trans_dict[i] for i in trans_input]))

file_contents = [line.strip() for line in open("i211-assets/100numbers.txt", "r")]
print(file_contents)

newDict = {num : file_contents.count(num) for num in file_contents}
print(newDict)
# print([i if i not in newDict else newDict[i] for i in file_contents])


