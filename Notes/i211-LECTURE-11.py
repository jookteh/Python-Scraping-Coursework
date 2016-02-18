import urllib.request, random
import webbrowser

def link_finder(page):

    print("Jumping from :" , page)

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


    new = "http://en.wikipedia.org" + random.choice(html)
    webbrowser.open_new_tab(new)
    print("To :", new)

    return new


baseurl = input("Where would you like to start? ")
jumps = int(input("How many jumps? "))


for i in range(jumps):
    baseurl = link_finder(baseurl)
