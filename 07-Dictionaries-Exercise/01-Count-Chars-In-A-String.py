letters = input()
dictionary = {}

for i in letters:
    if i == ' ':
        continue
    if i not in dictionary.keys():
        dictionary[i] = 0
    dictionary[i] += 1

for key, value in dictionary.items():
    print(f'{key} -> {value}')