# Liam Bolling
# March 3, 2016
# Homework 5? (I think)

import urllib
import datetime
import urllib.request, re

# PART 1
def getStockData(company = "GOOG"):

    url = "http://quote.yahoo.com/d/quotes.csv?s=" + company + "&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"
    webPage = urllib.request.urlopen(url)
    contents = webPage.read().decode(errors="replace").split(",")
    webPage.close()
    date = contents[2].replace('"',"").split("/")
    now = datetime.date(int(date[2]),int(date[0]),int(date[1]))

    # PART 3
    transdate = now.strftime("%b %d, %Y")

    print("The last trade for",company, "was $",contents[1],"and the change was $",contents[4],"on",transdate,". The open was $",contents[5], "and the previous close was $",contents[10],".")
    print("-"*10)


# PART 2
clist = ["PTR","CL","GOOG","AAPL","BIIB","PG","CMCSA","COST","UA","KO"]
for names in clist:
    getStockData(names)


# PART 4 - BONUS
def stocksymbol():
   webPage = urllib.request.urlopen("http://www.fool.com/the-25-best-companies-in-america/index.aspx")
   contents = webPage.read() .decode(errors="replace")
   webPage.close()

   NY = re.findall("NYSE: [A-Z.]+",contents)
   NAS = re.findall("Nasdaq: [A-Z.]+", contents)
   stocks = NY + NAS
   for stock in stocks:
       stock = stock.replace("NYSE: ","")
       stock = stock.replace("Nasdaq: ","")
       stock = stock.replace(".","-")
       getStockData(stock)
stocksymbol()