import re
import urllib.request, random

thisFile = open("quote.txt", 'r+')
content = thisFile.read()
print(content)


print("Words:", re.findall('[A-Z][\w]*', content))

print("Words:", re.findall('[\w]*ing', content))

print("Words:", re.findall('[\w]*[aA][\w]*[aA][\w]*', content))

print("Words:", re.findall(',[^.!?,]+,', content))

print("Words:", len(re.findall('[vV][\w]*', content)))

