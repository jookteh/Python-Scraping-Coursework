# Liam Bolling
# ljbollin
# March 10, 2016

import re
import urllib.request, random
import webbrowser

# SECTION 1
def NewsArticleFunction(url):
    print("Searching:",url)

    # Get the web page
    webpage = urllib.request.urlopen(url)
    line = webpage.read().decode(errors="replace")

    # This will search for anything that has the itemprop of a headline and print the name of the title
    titleData = re.findall('\<span itemprop="headline">[A-Za-z0-9\=\>\/" \,\'\:\$]*', line)

    # Now print out every title
    for elem in titleData:
        print("\n",elem.split(">")[1])



#SECTION 2
def NewsArticleFunction_FindStuff(url):
    print("Searching:",url)

    # Get the web page
    webpage = urllib.request.urlopen(url)
    line = webpage.read().decode(errors="replace")

    # This will search for anything that has the itemprop of a headline and print the name of the title
    crap = re.findall('\<span itemprop="headline">[A-Za-z0-9\=\>\/" \,\'\:\$]*', line)

    word = str(input("Please enter a word to search for:"))

    for elem in crap:
        temp = elem.split(">")[1]

        # Only if the string contains the word, do we print it...
        if word.lower() in temp.lower():
            print("\n",elem.split(">")[1])



# BONUS
def NewsArticleFunction_FindStuff_BONUS(url):
    print("Searching:",url)

    webpage = urllib.request.urlopen(url)
    line = webpage.read().decode(errors="replace")
    crap = re.findall('\<article class\=\"news item\" itemscope\=\"itemscope\"\>.* ', line)


    for elem in crap:
        print(elem)
    #
    # word = str(input("Please enter a word to search for:"))
    #
    # for elem in crap:
    #     temp = elem.split(">")[1]
    #     if word.lower() in temp.lower():
    #         print("\n",elem.split(">")[1])
    #         webbrowser.open(elem.split(">")[1])



# SECTION 1
NewsArticleFunction("https://www.indiana.edu/news-events/index.html")

# SECTION 2
NewsArticleFunction_FindStuff("https://www.indiana.edu/news-events/index.html")

# SECTION 3 - BONUS
NewsArticleFunction_FindStuff_BONUS("https://www.indiana.edu/news-events/index.html")