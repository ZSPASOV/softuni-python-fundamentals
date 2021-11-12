# Python has a built-in package called re
# It can be used to work with Regular Expressions
# Import the re module
# Use it to search in text

import re

txt = "The rain in Spain"
# r string for example would count \n as \n literally, instead of a new line
# search pattern in that case is a r string
search_pattern = r'^The.*Spain$'
x = re.search(search_pattern, txt)
print(x)