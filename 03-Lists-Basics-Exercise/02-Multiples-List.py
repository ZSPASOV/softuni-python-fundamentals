factor = int(input())
count = int(input())
empty_list = []

for i in range(factor, factor * count + 1, factor):
    empty_list.append(i)

print(empty_list)