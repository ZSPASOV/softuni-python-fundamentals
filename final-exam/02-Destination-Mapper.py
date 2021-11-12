import re
# v1 80 tochki r'(=|\/)([A-Za-z]{3,})\1'
pattern = r'(=|\/)([A-Z]{1}[a-z]+})\1'
#([A-Z][a-z]{2})
names = input()

matches = re.findall(pattern, names)

locations = []
for m in matches:

    match = m[1]
    locations.append(match)

for_print = (', ').join(locations)
print(f'Destinations: {for_print}')

sum_for_print = 0

for i in locations:
    sum_for_print += len(i)
print(f'Travel Points: {sum_for_print}')
