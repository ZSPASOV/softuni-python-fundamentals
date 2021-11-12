# The findall() function returns a list containing all matches
import re

str = 'The rain in Spain'
x = re.findall('ai', str)
print(x)

# The list contains the matches in order they are found
# If no matches are found, an empty list is returned