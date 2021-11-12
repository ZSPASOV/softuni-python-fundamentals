import re

txt = '''The Rain in Spain
The Rain in Spain'''
# r string for example would count \n as \n literally, instead of a new line
# search pattern in that case is a r string
search_pattern = r'^The.*Spain$'
# if MULTILINE is not used None would be returned
x = re.search(search_pattern, txt, re.MULTILINE)
print(x)

# the search function searches for only first match,
# in that case only the first The Rain in Spain will be returned as a match