number_sheep = int(input())
message = ''
sheep = 0

while sheep < number_sheep:
    message += f'{sheep + 1} sheep...'
    sheep += 1

print(message)