import urllib.request, random
import webbrowser
#
# def link_finder(page):
#
#     print("Jumping from :" , page)
#
#     webpage = urllib.request.urlopen(page)
#     line = webpage.read().decode(errors="replace")
#     webpage.close()
#
#     line = line.replace(">", "<").split("<")
#     html = []
#
#     for item in line:
#         if "href" in item and "/wiki" in item.split("\"")[1] and ".org" not in item:
#             item = item.split("\"")
#             if len(item) > 1:
#                 html.append(item[1])
#
#
#     new = "http://en.wikipedia.org" + random.choice(html)
#     webbrowser.open_new_tab(new)
#     print("To :", new)
#
#     return new
#
#
# baseurl = input("Where would you like to start? ")
# jumps = int(input("How many jumps? "))
#
#
# for i in range(jumps):
#     baseurl = link_finder(baseurl)

# import sys
# import csv
#
# sys.path.append('../Assets/')
# import tools
#
# characters = (open("../Assets/star-wars.csv", "r"))
#
# people = list(csv.reader(characters))
# people = people[1:]
#
# print('-'*50)
# print("MAIN CHARACTERS")
# print("Star Wars: Episode VII: The Force Awakens (2015)")
# print('-'*50)
#
# for person in people:
#     print(person[0] + (" "*(30-len(person[0]))) + person[1] + (" "*(30-len(person[1]))) + person[2])
#
#

import os

def something(webPageSite):
    webpage = urllib.request.urlopen(webPageSite)
    line = webpage.read().decode(errors="replace")
    webpage.close()

    quickFix = webPageSite.split("/")

    line = line.replace(">", "<").split("<")
    html = ""
    counter = 0

    for item in line:
        if "href" in item and "/wiki" in item.split("\"")[1] and ".org" not in item:
            item = item.split("\"")
            if len(item) > 1:
                html+=item[1]+"\n"
                counter+=1

    tempFile = open(os.path.join(os.getcwd(), quickFix[2]+".txt"), 'w')
    tempFile.write(html)
    tempFile.close()
    print(counter)



something("https://en.wikipedia.org/wiki/Star_Wars:_The_Force_Awakens")

# tools.table_print(("Company","Website"), listofINCompanies, 50)

