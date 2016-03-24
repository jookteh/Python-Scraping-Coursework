#Stu Combs
#123
#group HW 2

import xml.etree.ElementTree as ET

#Part 1
print("Part 1")
print()
root = ET.parse("cd_catalog.xml")

cds = root.iter('CD')

cdCount = 0 #for part a
priceTotal = 0 #for part a

priceList = [] #for part b

released1987 = [] #for part c

columbia = [] #for part d

for disc in cds:
    cdCount += 1
    priceTotal += float(disc.find('PRICE').text)
    priceList.append(float(disc.find('PRICE').text))
    if disc.find('YEAR').text == '1987':
        released1987.append(disc.find('TITLE').text)
    if disc.find('COMPANY').text == 'Columbia':
        columbia.append(disc.find('ARTIST').text)
        
#output for a.
print("The total number of CDs is", cdCount)
print("The total price of all CDs is $" + format(priceTotal, '.2f'))

#output for b.
avgPrice = priceTotal/len(priceList)
print('The average price for a CD is $' + format(avgPrice, '.2f'))
print('The maximum price for CD is $' + format(max(priceList), '.2f'))
print('The minimun price for a CD is $' + format(min(priceList), '.2f'))

#output for c.
print('All the CDs released in 1987 are:')
for cd in released1987:
    print('\t' + cd)

#output for d.
print("The artists who released a CD through Columbia records are:")
for artist in columbia:
    print('\t' + artist)




#Part 2
print()
print("Part 2")
print()
#part a

def bookinfo(bookID):
    root = ET.parse("books.xml")
    books = root.iter('book')
    
    findbook = [(item.find('title').text, item.find('author').text, item.find('price').text) for item in books if item.attrib['id'] == bookID ]
    return findbook

root = ET.parse('books.xml')
books = root.iter('book')

bookList = [thing.attrib['id'] for thing in books]

[print(bookinfo(bookid)) for bookid in bookList]

#part b

root = ET.parse('books.xml')
books = root.iter('book')

print()
print("Total number of fantasy books released in November:", len([item.find('title').text for item in books if item.find('genre').text == "Fantasy" \
                                                                  and '11' in item.find('publish_date').text]))


#part c

root = ET.parse('books.xml')
books = root.iter('book')

print()
genres = [item.find('genre').text for item in books]
print(genres)










    
    
