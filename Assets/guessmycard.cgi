#! /usr/bin/env python

import cgi
import random

print('content-type: text/html\n')

#baseCard = 'KC'
baseRank = '10'
baseSuit = 'C'


form = cgi.FieldStorage()

userRank = form.getfirst('rank', 'J')
userSuit = form.getfirst('suit', 'D')

cardImage = 'cards/'+userRank+userSuit+'.jpg'

if userSuit == baseSuit:
    statusSuit = 'Correct suit!'
else:
    statusSuit = 'Incorrect suit'


if userRank == '10':
    statusRank = 'Correct Rank!'

elif userRank in ['2','3','4','5','6','7','8','9']:
    statusRank  = 'Too low'

elif userRank in ['J','Q','K','A']:
    statusRank = 'Too high'

if userSuit == baseSuit and userRank == baseRank:
    output = 'Congrats on Guessing correctly!'

else:
    output = """


<form method="post" action="guessmycard.cgi">

	<H2>Try to guess the card!</H2>

	<p>Rank:

		<select name="rank">

			<option>2</option>

			<option>3</option>

			<option>4</option>

			<option>5</option>

			<option>6</option>

			<option>7</option>

			<option>8</option>

			<option>9</option>

			<option>10</option>

			<option>J</option>

			<option>Q</option>

			<option>K</option>

			<option>A</option>

		</select>

	</p>

	<p>Suit:

		<br /><input type="radio" name="suit" value="C" checked />Clubs

		<br /><input type="radio" name="suit" value="D" />Diamonds

		<br /><input type="radio" name="suit" value="H" />Hearts

		<br /><input type="radio" name="suit" value="S" />Spades

	</p>

	<button type="submit">Submit</button>

</form>"""

html = """
<!doctype html>
    <html>
     <head><meta charset = "utf-8">
      <title>Guess the Card</title>
     </head>
      <body>
       <h2> You Guessed: </h2>
       
       <p><img src ="[source]" height = "300" </p>

       <h2> Suit: </h2>
       <p> [source2] </p>

       <h2> Rank: </h2>
       <p> [source3] </p>

       {source4}

    </body>
    </html>"""

print(html.format(source = cardImage, source2 = statusSuit, source3 = statusrank,source4 = output))



    
