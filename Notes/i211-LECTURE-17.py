# import webbrowser
#
# out = open("template2.html","w")
#
# html = """
# <html>
#     <head>
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>Content</h1>
#         <p>
#             Hello
#         </p>
#         <p>
#             Hello 2
#         </p>
#         <a href="#">Link Example</a>
#     </body>
# </html>
# """
#
# name = input("PLease enter name")
# message = "hello "+name
#
# out.write(html.format(content = message))
# out.close()
#
# webbrowser.open("template2.html")
#
# data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
#         ["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
#         ["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
#         ["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]
#
# out = open("template2.html","w")
#
# html = """
# <html>
#     <head>
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>Hello</h1>
#
#
#         <table style="width:100%;" border="1">
# """
#
#
#
# for element in data:
#     html+= """
#         <tr>
#         <td>"""+element[0]+"""</td>
#         <td>"""+element[1]+"""</td>
#         <td>"""+element[2]+"""</td>
#         </tr>
#     """
#
#
#
# html += """
#         </table>
#     </body>
# </html>
# """
#
# out.write(html)
# out.close()

# import re
# import urllib.request, random
#
# #out = open("template2.html","r+")
# #print(out)
#
# webpage = urllib.request.urlopen("http://bloomington.in.gov/sections/viewSection.php?section_id=170")
# outLines = webpage.read().decode(errors="replace")
#
# # outLines = out.read()
#
# row = outLines.split("<tr")
# returnArray = []
#
# for elem in row:
#     tempArray = re.findall("\<td[\w]*\>.*\<\/td\>", elem)
#     returnTemp = []
#     for elem_2 in tempArray:
#         returnTemp.append(elem_2[4:-5])
#     if len(returnTemp) != 0:
#         returnArray.append(returnTemp)
#
# print(returnArray)

# print(re.findall("\<tr[\w]*\> [\w]* \</tr\>", outLines))







