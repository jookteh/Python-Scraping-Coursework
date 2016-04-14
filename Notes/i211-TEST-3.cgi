#! /usr/bin/env python
print('Content-type: text/html\n')
import cgi
form = cgi.FieldStorage()

# This is huge. Can we make smaller next test? PLzzzz
translationDict = {
    "baby":"lapse",
    "bird":"wilin",
    "book":"parma",
    "bridge":"yanta",
    "candle":"liikuma",
    "cat":"meoi",
    "cloth":"lanne",
    "cup":"yulma",
    "dog":"huo",
    "dragon":"fenume",
    "eye":"hen",
    "foot":"taal",
    "hand":"quaare",
    "moon":"silmo",
    "mouth":"anto",
    "plant":"olva",
    "road":"malle",
    "ship":"lunte",
    "tree":"alda",
    "wall":"ramba"
}

# Translated the words and returns if it was correct + the key of correct value
def guessTranslation(originalWord,wordAttempt):
    # Go through and find the values
    for key,value in translationDict.items():
        if value == originalWord:
            if wordAttempt == key:
                return [True, key]
            else:
                return [False, key]
    # Just in case they don't type anything?
    return [False, None]

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Elvish Language Practice</title></head>
    <body>
        <img src="img/{keyPhoto}.jpg" height="300" alt="{keyPhoto}">
	{resultStatement}
	<form method="post" action="i211-TEST-3.cgi">
            <p>Select a word to translate:
            <select name="word">
                <option>alda</option>
                <option>anto</option>
                <option>fenume</option>
                <option>hen</option>
                <option>huo</option>
                <option>lanne</option>
                <option>lapse</option>
                <option>liikuma</option>
                <option>lunte</option>
                <option>malle</option>
                <option>meoi</option>
                <option>olva</option>
                <option>parma</option>
                <option>quaare</option>
                <option>ramba</option>
                <option>silmo</option>
                <option>taal</option>
                <option>wilin</option>
                <option>yanta</option>
                <option>yulma</option>
            </select>
            </p>
            <p>Enter your translation: <input type="text" name="guess"></p>
        <button type="submit">Submit</button>
        </form>
    </body>
</html>
"""

# Get some values from the user
originalWord = form.getfirst('word', 'None')
wordAttempt = form.getfirst('guess', 'None')

# Store results in here for reference below
results = guessTranslation(originalWord, wordAttempt)

# If they guessed wrong, but we have an answer
if results[0] == False and results[1] != None:
    print(html.format(keyPhoto=results[1], resultStatement="<h2>Sorry, the correct word was "+str(results[1])+"</h2>"))
elif results[0] == True:
    # Correct answer
    print(html.format(keyPhoto=results[1], resultStatement="<h2>That's correct!</h2>"))
else:
    # Don't know how they would hit this
    print(html.format(keyPhoto=results[1], resultStatement="<h2></h2>"))