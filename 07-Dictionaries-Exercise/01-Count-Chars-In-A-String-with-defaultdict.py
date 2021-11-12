from collections import defaultdict

letters = input()
dictionary = defaultdict(int) # it creates a dictionary with the default value of int, which is 0

for i in letters:
    if i == ' ':
        continue
    dictionary[i] += 1

for key, value in dictionary.items():
    print(f'{key} -> {value}')