number_wagons = int(input())

list_train = [0] * number_wagons

def add_to_train(train, num):
    train[-1] += num


def insert_in_train(train, index, num):
    train[index] +=num


def leave_in_train(train, index, num):
    train[index] -=num
while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split(' ')
    command = tokens[0]
    if command == 'add':
        add_to_train(list_train, int(tokens[1]))
    elif command == 'insert':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        insert_in_train(list_train, index, people_to_insert)
    elif command == 'leave':
        index = int(tokens[1])
        people_to_leave = int(tokens[2])
        leave_in_train(list_train, index, people_to_leave)


print(list_train)