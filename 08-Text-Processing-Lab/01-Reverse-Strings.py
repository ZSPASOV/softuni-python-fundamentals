def reverse(string):
    return ''.join(reversed(string))
    #return string[::-1] - this is a second option, there are others too
    # for char in reversed(string):
    #     s += char
    # return s  - this is a third option

words = []
while True:
    command = input()
    if command == 'end':
        break
    words.append(command)

for word in words:
    print(f'{word} = {reverse(word)}')