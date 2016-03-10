import xml.etree.ElementTree as ET

# def id_find(inputNum):
#     root = ET.parse("students.xml")
#     elements = root.findall("Student")
#
#     for elem in elements:
#         if elem.find("id").text == inputNum:
#             print(elem.find("name/first").text+" "+elem.find("name/last").text)

# id_find("001987283")


def fee_find(fullName):
    root = ET.parse("students.xml")
    elements = root.findall("Student")

    fullNameArray = fullName.split(" ")

    for elem in elements:
        if elem.find("name/first").text == fullNameArray[0] and elem.find("name/last").text == fullNameArray[1]:
            return elem.find("name/first").text+" "+elem.find("name/last").text+" "+elem.find("fees").text+" "+elem.find("fees").attrib["c"]+" "+elem.find("fees").attrib["units"]
    return "Not found"


print(fee_find("Jack Sparrow"))
print(fee_find("wkefhk"))