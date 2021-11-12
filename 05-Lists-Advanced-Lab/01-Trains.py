number_wagons = int(input())


list_train = [i*0 for i in range(number_wagons)]
while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split(' ')
    command = tokens[0]
    if command == 'add':
        list_train[-1] += int(tokens[1])
    elif command == 'insert':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        list_train[index] += people_to_insert
    elif command == 'leave':
        index = int(tokens[1])
        people_to_leave = int(tokens[2])
        list_train[index] -= people_to_leave


print(list_train)