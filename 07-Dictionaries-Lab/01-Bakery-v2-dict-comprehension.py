elements = input().split(' ')
bakery = {elements[index]: int(elements[index + 1]) for index in range(0, len(elements), 2)}
print(bakery)