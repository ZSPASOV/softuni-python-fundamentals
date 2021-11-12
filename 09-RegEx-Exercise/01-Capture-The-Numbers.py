import re

pattern = '\d+'

while True:
    text = input()

    if not text:
        break

    matches = re.findall(pattern, text)

    for match in matches:
        print(match, end=' ')

# note - the while True cycle is because the console input is on many lines
# when we don`t have a line anymore it will be not text and it will break
# findall returns the match only, for that exercise that is enough, so we use findall instead of finditer
