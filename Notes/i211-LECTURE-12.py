import re
import urllib.request, random


def findVowels():
    test = "This is a *test* phrase meet ziim loon aaw"
    print("Words:", re.findall('[\w]*[aeiou][aeiou][\w]*', test))


def something(webPageSite):
    webpage = urllib.request.urlopen(webPageSite)
    line = webpage.read().decode(errors="replace")

    print("Emails:", re.findall('[\w]*\@[\w]*\.[(com)(edu)]*', line))




#findVowels()

something("http://www.soic.indiana.edu/about/contact/index.html")