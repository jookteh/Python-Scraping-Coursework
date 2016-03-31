# Liam Bolling
# Group: 123

#! /usr/bin/env python
print('Content-type: text/html\n')
import cgi
form = cgi.FieldStorage()

# Prints some html for the page
html = """
<!doctype html>
<html>
    <head>
	   <meta charset="utf-8">
	   <title>Form in CGI</title>
    </head>
    <body>
        <h1>Your ciphered message</h1>
	   <p>{content}</p>
       <a href="http://cgi.soic.indiana.edu/~ljbollin/lecture20/i211-HW-6.html"></a>
    </body>
</html>"""


# This will be out main logic of encrypt/decrypt. Default is to encrypt
def ceaserCiphererWord(word, key, direction=True):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    returnWord = ""
    for letter in word:
        # if we encrypt, we treverse by adding. Else by subtraction
        if direction:
            addedValues = alphabet.index(letter) + key
        else:
            addedValues = alphabet.index(letter) - key

        # Checking for overflow
        if addedValues > 25:
            addedValues = addedValues - 26
        if addedValues < 0:
            addedValues = 26 - addedValues

        # Add to final string
        returnWord += alphabet[addedValues]
    return returnWord


# Encrypts a string
def ceaserCipherer_Encrypt(inputString, inputKey):
    inputStringArray = inputString.split(" ")
    finalString = ""

    for word in inputStringArray:
        finalString += " "+ceaserCiphererWord(word,inputKey)

    return finalString


# Decrypts a string
def ceaserCipherer_Decrypt(inputString, inputKey):
    inputStringArray = inputString.split(" ")
    finalString = ""

    for word in inputStringArray:
        finalString += " "+ceaserCiphererWord(word,inputKey, False)

    return finalString


# Gets some defaults
radioValue = form.getfirst('direction', 'hello')
messageValue = form.getfirst('message', 'hello')
keyValue = form.getfirst('key', 'hello')


if str(radioValue) == "encrypt":
    print(html.format(content = ceaserCipherer_Encrypt(str(messageValue), int(keyValue))))
else if str(radioValue) == "decrypt":
    print(html.format(content = ceaserCipherer_Decrypt(str(messageValue), int(keyValue))))
else:
    print(html.format(content = "Error - Missing radio value")))
