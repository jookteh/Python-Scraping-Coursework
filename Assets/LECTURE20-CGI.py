#! /usr/bin/env python
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()
html = """
<!doctype html>
<html>
    <head>
	   <meta charset="utf-8">
	   <title>Form in CGI</title>
    </head>
    <body>
	   <p>{content}</p>
    </body>
</html>"""


addedUp = 0
splitArray = form.getfirst('somethingThingsInArea','Who are you?').split("\r\n")

for num in splitArray:
    addedUp+=int(num)

print(html.format(content = addedUp))
