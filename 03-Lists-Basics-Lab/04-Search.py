n = int(input())
search_word = input()
strings = []
filtered_strings = []

for _ in range(n):
    string = input()
    strings.append(string)
    if search_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)