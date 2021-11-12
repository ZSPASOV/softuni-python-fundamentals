n = int(input())
list_integers = []

for _ in range(n):
    number_for_list = int(input())
    list_integers.append(number_for_list)

command = input()
filtered = []

for i in list_integers:
    if command == 'even' and i % 2 == 0:
        filtered.append(i)
    elif command == 'odd' and i % 2 != 0:
        filtered.append(i)
    elif command == 'negative' and i < 0:
        filtered.append(i)
    elif command == 'positive' and i >= 0:
        filtered.append(i)

print(filtered)
