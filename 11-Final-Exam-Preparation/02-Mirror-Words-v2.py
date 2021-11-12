import re

# r'(@|#)\w{3,}\1\1\w{3,}\1'
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

names = input()

matches = re.findall(pattern, names)
print(matches)

for i in matches:
    print(i)
