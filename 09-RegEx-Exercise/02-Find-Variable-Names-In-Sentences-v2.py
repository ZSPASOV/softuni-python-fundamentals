import re

# <variable> in that case is name of the group
# the whole match is group 0, first occurence of () is group 1
pattern = r'\b_(?P<variable>[a-zA-Z0-9]+)\b'

text = input()

matches = re.finditer(pattern, text)

all_variable_names = []

for match in matches:
    all_variable_names.append(match['variable'])

print(','.join(all_variable_names))