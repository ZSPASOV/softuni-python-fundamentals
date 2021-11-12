empty_list = []
total_electrons = int(input())
index = -1
while total_electrons > 0:
    index += 1
    value = 2 * (index + 1) ** 2
    if total_electrons >= value:
        empty_list.append(value)
    else:
        empty_list.append(total_electrons)
    total_electrons -= value

print(empty_list)
