number_of_commands = int(input())
registered_users = {}
for _ in range(number_of_commands):
    command_list = input().split(' ')
    action = command_list[0]
    person = command_list[1]


    if action == 'register':
        license_plate_number = command_list[2]

        if person in registered_users.keys():
            print(f"ERROR: already registered with plate number {registered_users[person]}")
            continue
        registered_users[person] = license_plate_number
        print(f"{person} registered {registered_users[person]} successfully")

    if action == 'unregister':
        if person not in registered_users.keys():
            print(f"ERROR: user {person} not found")
            continue
        registered_users.pop(person)
        print(f"{person} unregistered successfully")


for key, value in registered_users.items():
    print(f"{key} => {value}")




