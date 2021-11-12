factor = int(input())
count = int(input())
empty_list = []
number = 0
for _ in range(count):
    number += factor
    empty_list.append(number)

print(empty_list)