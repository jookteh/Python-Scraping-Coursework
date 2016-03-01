


import re
import urllib.request, random



def findStockInfo(webPageSite):
    webpage = urllib.request.urlopen(webPageSite)
    line = webpage.read().decode(errors="replace")

    print("Emails:", re.findall('[\w]*\@[\w]*\.[(com)(edu)]*', line))




#findVowels()

findStockInfo("http://finance.yahoo.com/q?s=GOOG")