import re

# pattern = r'\b_(?P<variable>[a-zA-Z0-9]+)\b'
# ?P<variable> is just the name of the group, otherwise it is group 1 if it is unnamed
# the whole match is group 0, first occurence of () is group 1
pattern = r'\b_([a-zA-Z0-9]+)\b'

text = input()

matches = re.finditer(pattern, text)

all_variable_names = []

for match in matches:
    all_variable_names.append(match.group(1))

print(','.join(all_variable_names))