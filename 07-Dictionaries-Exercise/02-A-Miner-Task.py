dictionary = {}
key = input()

while key != 'stop':
    value = int(input())
    if key not in dictionary.keys():
        dictionary[key] = 0
    dictionary[key] += value
    key = input()
for key, value in dictionary.items():
    print(f'{key} -> {value}')

