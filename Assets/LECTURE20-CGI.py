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

print(html.format(content = int(form.getfirst('firstNum','Who are you?')) + int(form.getfirst('secondNum','Who are you?'))))
