from collections import defaultdict

dictionary = defaultdict(int)
key = input()

while key != 'stop':
    value = int(input())
    dictionary[key] += value
    key = input()
for key, value in dictionary.items():
    print(f'{key} -> {value}')

