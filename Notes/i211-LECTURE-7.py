file_contents = [line.strip() for line in open("i211-assets/CaP.txt", "r")]
print(file_contents)

import string

print([i for b in file_contents for i in b.split(" ") if len([a for a in i if a in values]) > 1])
print("".join([i for b in file_contents for i in b.split(" ") for i in b.lower() if i.isalpha() or i.isspace()]))

someCrap = ("".join([i for b in file_contents for i in b.split(" ") for i in b.lower() if i.isalpha() or i.isspace()])).split(" ")
print(someCrap)

print({word: someCrap.count(word) for word in someCrap if someCrap.count(word) > 99})

import os
correctPath = os.path.join(os.getcwd(), "i211-assets", "lab4_files")

print([fileName for fileName in os.listdir(correctPath) if os.path.getsize(os.path.join(correctPath, fileName)) < 5])
print([fileName for fileName in os.listdir(correctPath) if os.path.getsize(os.path.join(correctPath, fileName)) > 5])

smallFilesList = [os.rename(os.path.join(correctPath, fileName), os.path.join(correctPath, fileName.split(".")[0]+"_small.txt")) for fileName in os.listdir(correctPath) if os.path.getsize(os.path.join(correctPath, fileName)) < 5 and os.path.isfile(os.path.join(correctPath, fileName))]
largeFilesList = [os.rename(os.path.join(correctPath, fileName), os.path.join(correctPath, fileName.split(".")[0]+"_large.txt")) for fileName in os.listdir(correctPath) if os.path.getsize(os.path.join(correctPath, fileName)) > 5 and os.path.isfile(os.path.join(correctPath, fileName))]