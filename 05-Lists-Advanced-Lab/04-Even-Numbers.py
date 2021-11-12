list_of_numbers = input().split(', ')
print([index for index, n in enumerate(list_of_numbers) if int(n) > 0 and int(n) % 2 == 0])
