import os

# print(os.getcwd())
# home = os.getcwd()
# print(os.path.join(home, os.getcwd(), "i211-LAB6.py"))
# print(os.listdir(os.getcwd()))
# print(os.path.isdir(os.getcwd()))
# print(os.path.isfile(os.path.join(os.getcwd(), "i211-LAB6.py")))


def exampleDir():
    correctPath = os.path.join(os.getcwd(), "i211-assets", "Sample_Directory")
    dirsAtPath = []

    for element in os.listdir(correctPath):
        if os.path.isdir(os.path.join(correctPath, element)):
            dirsAtPath.append(element)

    print("Current Directory:")
    print(dirsAtPath)

    while True:
        tempVar = input("Select a directory: ")
        if os.path.isdir(os.path.join(correctPath, tempVar)):
            print("You Chose: ")
            print(os.path.join(correctPath, tempVar))
            return os.path.join(correctPath, tempVar)
        print("Doesn't exist.")


def listFiles(selectedDir):
    print("")
    print("Files in Directory:")
    for file in os.listdir(selectedDir):
        if os.path.isfile(os.path.join(selectedDir, file)):
            print(file)


selectedDir = exampleDir()
listFiles(selectedDir)



# for i in range(3):
#     f = open(os.path.join(os.getcwd(), "test"+i+".txt"), "w")
#     f.write("yeh")
#     f.close()
