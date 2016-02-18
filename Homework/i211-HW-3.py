# Liam Bolling
# Feb 3, 2016

# 1. (40 points)
# Use a list comprehension to load the data from a file named “race.txt”.
# There’s a sample file on Oncourse with the data shown above.
fileContents = [line.strip().split(" ") for line in open("i211-assets/race.txt", "r")]
vowelList = ["a", "e", "i", "o", "u"]

# 2. (20 points)
# Print out the information read in from the file formatted as shown in the example.
for element in fileContents:
    print(element[0]+" traveled "+element[1]+" miles")

# 3. (20 points)
# Use a list comprehension to create a list of the names of the racers that begin with a vowel and print the list.
print("Names beginning with a vowel:",[i[0] for i in fileContents if i[0][0].lower() in vowelList])

# 4.  (20 points)
# Use a list comprehension to create a list of the names of those who have traveled more than 500 miles
# and print the list.
print("People who have traveled over 500 miles:",[i[0] for i in fileContents if int(i[1]) >= 500])


# ------Desired Output------
# Eruc traveled 231 miles
# Gagarin traveled 2083 miles
# Kalakaua traveled 419 miles
# Earheart traveled 970 miles
# Fosset traveled 745 miles
# Ignacio traveled 1104 miles
# Names beginning with a vowel: ['Eruc', 'Earheart', 'Ignacio']
# People who have traveled over 500 miles: ['Gagarin', 'Earheart', 'Fosset', 'Ignacio']


# ------Actual Output------
# Eruc traveled 231 miles
# Gagarin traveled 2083 miles
# Kalakaua traveled 419 miles
# Earheart traveled 970 miles
# Fosset traveled 745 miles
# Ignacio traveled 1104 miles
# Names beginning with a vowel: ['Eruc', 'Earheart', 'Ignacio']
# People who have traveled over 500 miles: ['Gagarin', 'Earheart', 'Fosset', 'Ignacio']