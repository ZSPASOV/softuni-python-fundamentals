number_sheep = int(input())
message = ''

for i in range(1, number_sheep + 1):
    message += f'{i} sheep...'

print(message)