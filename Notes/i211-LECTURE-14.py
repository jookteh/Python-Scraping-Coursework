import xml.etree.ElementTree as ET

root = ET.parse("students.xml")
elements = root.findall("Student")

print("The students are:")

# for elem in list(elements):
#     if elem.tag == "name":
#         tempArray = list(elem)
#         print(tempArray[0].text, tempArray[1].text)

total = 0
for elem in elements:
    total+=int(elem.find("fees").text)

print("Total fees:$",total)

