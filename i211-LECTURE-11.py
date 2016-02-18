import urllib.request, random

def link_finder(page):

    webpage = urllib.request.urlopen(page)
    line = webpage.read().decode(errors="replace")
    webpage.close()

    line = line.replace(">", "<").split("<")
    html = []

    for item in line:
        if "href" in item and "/wiki" in item.split("\"")[1] and ".org" not in item:
            item = item.split("\"")
            if len(item) > 1:
                html.append(item[1])
    return html

baseurl = input("Where would you like to start? ")
jumps = int(input("How many jumps? "))
html = link_finder(baseurl)

for i in range(jumps):
    print("Jumping from :" , baseurl)
    new = "http://en.wikipedia.org" + random.choice(html)

    print("To :", new)
    baseurl = new
