n = int(input())
list_integers = []

for _ in range(n):
    number_for_list = int(input())
    list_integers.append(number_for_list)

command = input()
filtered = []

for i in list_integers:
    filter_passes = (
        (command == 'even' and i % 2 == 0) or
        (command == 'odd' and i % 2 != 0) or
        (command == 'negative' and i < 0) or
        (command == 'positive' and i >= 0)
    )
    if filter_passes:
        filtered.append(i)

print(filtered)
