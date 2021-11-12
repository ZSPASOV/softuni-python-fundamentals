import re

text = input()
pattern = r'(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})'
matches = re.fullmatch(pattern, text)
print(matches)
print(matches[4])
# for match in re.findall(pattern, text):
#     day, _, month, year = match
#     print(f'Day: {day}, Month: {month}, Year: {year}')


# \2 is a backreference to the second capturing group, in that case ([/\.-])