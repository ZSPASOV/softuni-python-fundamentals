string = input()
new_string = input()
while True:
    new_string = new_string.replace(string, '')
    if string not in new_string:
        break
print(new_string)