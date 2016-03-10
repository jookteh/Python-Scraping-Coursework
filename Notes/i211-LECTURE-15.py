import re
import urllib.request, random

replacementText = "Avast, you scurvy dogs. You'll never get me peices of eight. Walk the plank!"

listr = re.findall("[A-Z][\w\s',]*[!.]", replacementText)
for elem in listr:
    print(elem,"Argg")

thisFile = open("pirate-letter.txt", 'r+')
content = thisFile.read()

print(re.findall("[A-Z][\w]*[\s] [\w]*[\s]*", content))

