# The split() function returns a list where the string has been split at each match

import re

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

text = 'Lorem1ipsum2dolor3sit4amet5test'
print(re.split(r'\d', text))