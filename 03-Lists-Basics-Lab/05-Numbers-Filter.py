n = int(input())
list_integers = []

for _ in range(n):
    number_for_list = int(input())
    list_integers.append(number_for_list)

command = input()
for i in range(len(list_integers) - 1, -1, -1):
    if command == 'even' and list_integers[i] % 2 != 0:
        list_integers.remove(list_integers[i])
    if command == 'odd' and list_integers[i] % 2 != 1:
        list_integers.remove(list_integers[i])
    if command == 'negative' and list_integers[i] >= 0:
        list_integers.remove(list_integers[i])
    if command == 'positive' and list_integers[i] < 0:
        list_integers.remove(list_integers[i])

print(list_integers)
