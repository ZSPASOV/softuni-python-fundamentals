# Python has a built-in package called re
# It can be used to work with Regular Expressions
# Import the re module
# Use it to search in text

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)